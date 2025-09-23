"""
Agent Orchestrator - Central coordination system for multi-agent workflows

This module implements the core orchestration logic for managing multiple
AI agents powered by Microsoft Foundry Local.
"""

import asyncio
import logging
import time
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, field
from enum import Enum
import json

from foundry_local import FoundryLocalManager
import openai
from pydantic import BaseModel, Field

from .base_agent import BaseAgent
from .coordination.task_router import TaskRouter
from .coordination.result_merger import ResultMerger
from .coordination.context_manager import ContextManager
from .coordination.workflow_engine import WorkflowEngine
from .tools.function_registry import FunctionRegistry
from .utils.foundry_client import FoundryClientManager
from .utils.logging_config import setup_logging


class TaskStatus(Enum):
    """Task execution status."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class WorkflowType(Enum):
    """Supported workflow types."""
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"
    DYNAMIC = "dynamic"
    HYBRID = "hybrid"


@dataclass
class TaskResult:
    """Result from a task execution."""
    task_id: str
    agent_id: str
    status: TaskStatus
    result: Any = None
    error_message: Optional[str] = None
    execution_time: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)


@dataclass
class OrchestrationMetrics:
    """Performance metrics for the orchestrator."""
    tasks_completed: int = 0
    tasks_failed: int = 0
    total_execution_time: float = 0.0
    agent_utilization: Dict[str, float] = field(default_factory=dict)
    average_response_time: float = 0.0
    success_rate: float = 0.0


class OrchestrationConfig(BaseModel):
    """Configuration for the orchestrator."""
    max_concurrent_agents: int = Field(default=4, ge=1, le=10)
    agent_pool_size: int = Field(default=8, ge=2, le=20)
    task_queue_size: int = Field(default=100, ge=10, le=1000)
    timeout_seconds: int = Field(default=300, ge=30, le=3600)
    enable_caching: bool = Field(default=True)
    cache_ttl: int = Field(default=3600, ge=300, le=86400)
    log_level: str = Field(default="INFO")
    enable_metrics: bool = Field(default=True)
    quality_threshold: float = Field(default=0.8, ge=0.0, le=1.0)


class AgentOrchestrator:
    """
    Central orchestrator for managing multiple AI agents powered by Foundry Local.
    
    This class provides intelligent task routing, agent coordination, result synthesis,
    and workflow management capabilities following Microsoft's best practices.
    """
    
    def __init__(self, config: Optional[OrchestrationConfig] = None):
        """
        Initialize the agent orchestrator.
        
        Args:
            config: Configuration for the orchestrator
        """
        self.config = config or OrchestrationConfig()
        
        # Setup logging
        self.logger = setup_logging(self.config.log_level)
        self.logger.info("Initializing Agent Orchestrator...")
        
        # Core components
        self.foundry_client = FoundryClientManager()
        self.task_router = TaskRouter()
        self.result_merger = ResultMerger()
        self.context_manager = ContextManager()
        self.workflow_engine = WorkflowEngine()
        self.function_registry = FunctionRegistry()
        
        # Agent management
        self.agents: Dict[str, BaseAgent] = {}
        self.agent_capabilities: Dict[str, List[str]] = {}
        self.agent_workload: Dict[str, int] = {}
        
        # Task management
        self.active_tasks: Dict[str, TaskResult] = {}
        self.task_queue: asyncio.Queue = asyncio.Queue(maxsize=self.config.task_queue_size)
        self.task_history: List[TaskResult] = []
        
        # Performance tracking
        self.metrics = OrchestrationMetrics()
        self.start_time = time.time()
        
        # Synchronization
        self.agent_lock = asyncio.Lock()
        self.task_lock = asyncio.Lock()
        
        self.logger.info("Agent Orchestrator initialized successfully")
    
    async def __aenter__(self):
        """Async context manager entry."""
        await self.initialize()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.cleanup()
    
    async def initialize(self):
        """Initialize all components and start the orchestrator."""
        try:
            self.logger.info("Starting orchestrator initialization...")
            
            # Initialize Foundry Local client
            await self.foundry_client.initialize()
            
            # Initialize core components
            await self.task_router.initialize()
            await self.result_merger.initialize()
            await self.context_manager.initialize()
            await self.workflow_engine.initialize()
            await self.function_registry.initialize()
            
            self.logger.info("Orchestrator initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize orchestrator: {e}")
            raise
    
    async def cleanup(self):
        """Clean up resources and stop all agents."""
        try:
            self.logger.info("Starting orchestrator cleanup...")
            
            # Cancel all active tasks
            for task_id in list(self.active_tasks.keys()):
                await self.cancel_task(task_id)
            
            # Stop all agents
            for agent_id in list(self.agents.keys()):
                await self.remove_agent(agent_id)
            
            # Cleanup components
            await self.foundry_client.cleanup()
            
            self.logger.info("Orchestrator cleanup completed")
            
        except Exception as e:
            self.logger.error(f"Error during cleanup: {e}")
    
    async def add_agent(self, agent: BaseAgent) -> str:
        """
        Add an agent to the orchestrator.
        
        Args:
            agent: The agent to add
            
        Returns:
            The agent ID
        """
        async with self.agent_lock:
            agent_id = agent.agent_id
            
            if agent_id in self.agents:
                raise ValueError(f"Agent {agent_id} already exists")
            
            # Initialize the agent
            await agent.initialize(self.foundry_client)
            
            # Register agent
            self.agents[agent_id] = agent
            self.agent_capabilities[agent_id] = agent.get_capabilities()
            self.agent_workload[agent_id] = 0
            
            # Register agent's tools
            for tool_name, tool_func in agent.get_tools().items():
                await self.function_registry.register_tool(
                    name=tool_name,
                    function=tool_func,
                    agent_id=agent_id,
                    metadata=agent.get_tool_metadata(tool_name)
                )
            
            self.logger.info(f"Added agent: {agent_id} with capabilities: {agent.get_capabilities()}")
            return agent_id
    
    async def remove_agent(self, agent_id: str):
        """
        Remove an agent from the orchestrator.
        
        Args:
            agent_id: ID of the agent to remove
        """
        async with self.agent_lock:
            if agent_id not in self.agents:
                raise ValueError(f"Agent {agent_id} not found")
            
            agent = self.agents[agent_id]
            
            # Cancel any tasks assigned to this agent
            for task_id, task_result in list(self.active_tasks.items()):
                if task_result.agent_id == agent_id:
                    await self.cancel_task(task_id)
            
            # Unregister agent's tools
            await self.function_registry.unregister_agent_tools(agent_id)
            
            # Cleanup agent
            await agent.cleanup()
            
            # Remove from tracking
            del self.agents[agent_id]
            del self.agent_capabilities[agent_id]
            del self.agent_workload[agent_id]
            
            self.logger.info(f"Removed agent: {agent_id}")
    
    async def execute_task(
        self,
        task: str,
        task_type: Optional[str] = None,
        agent_id: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> TaskResult:
        """
        Execute a single task using the orchestrator.
        
        Args:
            task: Task description or specification
            task_type: Optional task type hint
            agent_id: Optional specific agent to use
            context: Optional context for the task
            metadata: Optional metadata for the task
            
        Returns:
            TaskResult with execution details
        """
        task_id = f"task_{int(time.time() * 1000000)}"
        
        try:
            self.logger.info(f"Executing task {task_id}: {task[:100]}...")
            
            # Route task to appropriate agent
            if agent_id and agent_id in self.agents:
                selected_agent = self.agents[agent_id]
            else:
                selected_agent = await self.task_router.route_task(
                    task=task,
                    task_type=task_type,
                    available_agents=self.agents,
                    agent_capabilities=self.agent_capabilities,
                    agent_workload=self.agent_workload
                )
            
            if not selected_agent:
                raise Exception("No suitable agent found for task")
            
            # Create task result
            task_result = TaskResult(
                task_id=task_id,
                agent_id=selected_agent.agent_id,
                status=TaskStatus.IN_PROGRESS,
                metadata=metadata or {}
            )
            
            self.active_tasks[task_id] = task_result
            self.agent_workload[selected_agent.agent_id] += 1
            
            # Update context
            if context:
                await self.context_manager.update_context(task_id, context)
            
            # Execute task
            start_time = time.time()
            
            try:
                result = await asyncio.wait_for(
                    selected_agent.execute_task(
                        task=task,
                        context=await self.context_manager.get_context(task_id),
                        metadata=metadata
                    ),
                    timeout=self.config.timeout_seconds
                )
                
                execution_time = time.time() - start_time
                
                # Update task result
                task_result.status = TaskStatus.COMPLETED
                task_result.result = result
                task_result.execution_time = execution_time
                
                # Update metrics
                self.metrics.tasks_completed += 1
                self.metrics.total_execution_time += execution_time
                
                self.logger.info(f"Task {task_id} completed in {execution_time:.2f}s")
                
            except asyncio.TimeoutError:
                task_result.status = TaskStatus.FAILED
                task_result.error_message = f"Task timed out after {self.config.timeout_seconds}s"
                self.metrics.tasks_failed += 1
                
            except Exception as e:
                task_result.status = TaskStatus.FAILED
                task_result.error_message = str(e)
                task_result.execution_time = time.time() - start_time
                self.metrics.tasks_failed += 1
                self.logger.error(f"Task {task_id} failed: {e}")
            
            # Cleanup
            finally:
                self.agent_workload[selected_agent.agent_id] -= 1
                if task_id in self.active_tasks:
                    del self.active_tasks[task_id]
                self.task_history.append(task_result)
            
            return task_result
            
        except Exception as e:
            self.logger.error(f"Error executing task {task_id}: {e}")
            return TaskResult(
                task_id=task_id,
                agent_id="unknown",
                status=TaskStatus.FAILED,
                error_message=str(e)
            )
    
    async def execute_workflow(
        self,
        task: str,
        workflow_type: WorkflowType = WorkflowType.DYNAMIC,
        quality_gates: Optional[List[str]] = None,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Execute a complex workflow using multiple agents.
        
        Args:
            task: Main task description
            workflow_type: Type of workflow to execute
            quality_gates: Quality checkpoints to enforce
            context: Initial context for the workflow
            
        Returns:
            Comprehensive workflow results
        """
        workflow_id = f"workflow_{int(time.time() * 1000000)}"
        
        try:
            self.logger.info(f"Starting workflow {workflow_id}: {workflow_type.value}")
            
            # Create workflow plan
            workflow_plan = await self.workflow_engine.create_workflow_plan(
                task=task,
                workflow_type=workflow_type,
                available_agents=list(self.agents.keys()),
                agent_capabilities=self.agent_capabilities
            )
            
            # Execute workflow
            workflow_results = await self.workflow_engine.execute_workflow(
                workflow_id=workflow_id,
                workflow_plan=workflow_plan,
                orchestrator=self,
                quality_gates=quality_gates or [],
                initial_context=context or {}
            )
            
            # Synthesize final results
            final_results = await self.result_merger.synthesize_workflow_results(
                workflow_results=workflow_results,
                task=task,
                context=context or {}
            )
            
            self.logger.info(f"Workflow {workflow_id} completed successfully")
            return final_results
            
        except Exception as e:
            self.logger.error(f"Workflow {workflow_id} failed: {e}")
            raise
    
    async def execute_parallel(
        self,
        tasks: List[tuple],
        max_concurrent: Optional[int] = None
    ) -> List[TaskResult]:
        """
        Execute multiple tasks in parallel.
        
        Args:
            tasks: List of (task_description, agent_class, task_type) tuples
            max_concurrent: Maximum concurrent executions
            
        Returns:
            List of task results
        """
        max_concurrent = max_concurrent or self.config.max_concurrent_agents
        
        async def execute_single_task(task_info):
            task_desc, agent_class, task_type = task_info
            
            # Find appropriate agent
            suitable_agents = [
                agent for agent in self.agents.values()
                if isinstance(agent, agent_class)
            ]
            
            if not suitable_agents:
                # Try to create new agent if needed
                agent = agent_class()
                await self.add_agent(agent)
                suitable_agents = [agent]
            
            # Execute with least loaded agent
            selected_agent = min(
                suitable_agents,
                key=lambda a: self.agent_workload[a.agent_id]
            )
            
            return await self.execute_task(
                task=task_desc,
                task_type=task_type,
                agent_id=selected_agent.agent_id
            )
        
        # Execute with concurrency limit
        semaphore = asyncio.Semaphore(max_concurrent)
        
        async def limited_execute(task_info):
            async with semaphore:
                return await execute_single_task(task_info)
        
        self.logger.info(f"Executing {len(tasks)} tasks in parallel (max concurrent: {max_concurrent})")
        results = await asyncio.gather(*[limited_execute(task) for task in tasks])
        
        return results
    
    async def cancel_task(self, task_id: str) -> bool:
        """
        Cancel an active task.
        
        Args:
            task_id: ID of the task to cancel
            
        Returns:
            True if task was cancelled, False if not found
        """
        async with self.task_lock:
            if task_id not in self.active_tasks:
                return False
            
            task_result = self.active_tasks[task_id]
            task_result.status = TaskStatus.CANCELLED
            
            # Notify agent to cancel task
            if task_result.agent_id in self.agents:
                agent = self.agents[task_result.agent_id]
                await agent.cancel_task(task_id)
                self.agent_workload[task_result.agent_id] -= 1
            
            # Move to history
            del self.active_tasks[task_id]
            self.task_history.append(task_result)
            
            self.logger.info(f"Cancelled task: {task_id}")
            return True
    
    async def get_performance_metrics(self) -> OrchestrationMetrics:
        """Get current performance metrics."""
        if self.metrics.tasks_completed > 0:
            self.metrics.average_response_time = (
                self.metrics.total_execution_time / self.metrics.tasks_completed
            )
            
            total_tasks = self.metrics.tasks_completed + self.metrics.tasks_failed
            self.metrics.success_rate = self.metrics.tasks_completed / total_tasks if total_tasks > 0 else 0.0
        
        # Calculate agent utilization
        total_uptime = time.time() - self.start_time
        for agent_id, agent in self.agents.items():
            if hasattr(agent, 'total_active_time'):
                self.metrics.agent_utilization[agent_id] = (
                    agent.total_active_time / total_uptime if total_uptime > 0 else 0.0
                )
        
        return self.metrics
    
    def get_status(self) -> Dict[str, Any]:
        """Get current orchestrator status."""
        return {
            "active_agents": len(self.agents),
            "active_tasks": len(self.active_tasks),
            "total_tasks_completed": self.metrics.tasks_completed,
            "total_tasks_failed": self.metrics.tasks_failed,
            "uptime_seconds": time.time() - self.start_time,
            "agent_workload": dict(self.agent_workload),
            "available_capabilities": list(
                set().union(*self.agent_capabilities.values())
            ) if self.agent_capabilities else []
        }
    
    async def register_tools(self, tools: List[Dict[str, Any]]):
        """
        Register external tools with the orchestrator.
        
        Args:
            tools: List of tool definitions following Microsoft function calling schema
        """
        for tool in tools:
            await self.function_registry.register_external_tool(tool)
            self.logger.info(f"Registered external tool: {tool['name']}")
    
    async def configure_agents(self, agent_configs: Dict[str, Dict[str, Any]]):
        """
        Configure agent settings.
        
        Args:
            agent_configs: Configuration for each agent type
        """
        for agent_id, agent in self.agents.items():
            agent_type = agent.__class__.__name__
            if agent_type in agent_configs:
                await agent.update_config(agent_configs[agent_type])
                self.logger.info(f"Updated configuration for agent: {agent_id}")
    
    async def analyze_task_requirements(self, task: str) -> List[str]:
        """
        Analyze a task and determine required agent types.
        
        Args:
            task: Task description
            
        Returns:
            List of recommended agent class names
        """
        return await self.task_router.analyze_task_requirements(
            task=task,
            available_capabilities=self.agent_capabilities
        )
"""
Multi-Agent Orchestration System for Microsoft Foundry Local

This package provides a comprehensive framework for building and managing
multi-agent AI systems using Microsoft Foundry Local, following official
patterns and best practices.
"""

from .orchestrator import AgentOrchestrator
from .base_agent import BaseAgent, tool
from .specialized_agents import (
    CodeAgent,
    ResearchAgent, 
    DataAgent,
    WritingAgent,
    SolverAgent
)

__version__ = "1.0.0"
__author__ = "Microsoft EdgeAI for Beginners"
__license__ = "MIT"

__all__ = [
    "AgentOrchestrator",
    "BaseAgent", 
    "tool",
    "CodeAgent",
    "ResearchAgent",
    "DataAgent", 
    "WritingAgent",
    "SolverAgent"
]
"""
Foundry Local REST API Client

This module provides a direct HTTP client for Microsoft Foundry Local,
following official patterns and best practices from the Microsoft repository.
"""

import asyncio
import json
import logging
import time
from typing import Dict, List, Optional, AsyncGenerator, Any
from dataclasses import dataclass
from enum import Enum

import aiohttp
import requests
from foundry_local import FoundryLocalManager
from tenacity import retry, stop_after_attempt, wait_exponential
from pydantic import BaseModel, Field


# Configuration and Data Models
class ResponseStatus(Enum):
    SUCCESS = "success"
    ERROR = "error"
    TIMEOUT = "timeout"
    RETRY = "retry"


@dataclass
class CompletionResponse:
    """Response from completion API."""
    content: str
    status: ResponseStatus
    model: str
    tokens_used: int = 0
    response_time: float = 0.0
    error_message: Optional[str] = None


@dataclass
class HealthStatus:
    """Health status of Foundry Local service."""
    status: str
    loaded_models: List[str]
    memory_usage: float
    uptime: float
    version: str


class CompletionRequest(BaseModel):
    """Request model for completions."""
    prompt: str = Field(..., description="The prompt to complete")
    model: str = Field(default="phi-4-mini", description="Model to use")
    max_tokens: int = Field(default=500, description="Maximum tokens to generate")
    temperature: float = Field(default=0.7, description="Sampling temperature")
    stream: bool = Field(default=False, description="Enable streaming responses")
    system_prompt: Optional[str] = Field(None, description="System prompt")


class FoundryAPIClient:
    """
    Direct REST API client for Microsoft Foundry Local.
    
    This client provides low-level HTTP access to Foundry Local services,
    following Microsoft's official patterns and best practices.
    """
    
    def __init__(
        self,
        model_alias: str = "phi-4-mini",
        timeout: int = 30,
        max_retries: int = 3,
        log_level: str = "INFO"
    ):
        """
        Initialize the Foundry API client.
        
        Args:
            model_alias: Default model to use for completions
            timeout: Request timeout in seconds
            max_retries: Number of retry attempts
            log_level: Logging level
        """
        self.model_alias = model_alias
        self.timeout = timeout
        self.max_retries = max_retries
        
        # Setup logging
        logging.basicConfig(level=getattr(logging, log_level.upper()))
        self.logger = logging.getLogger(__name__)
        
        # Initialize Foundry Local Manager
        self.manager = FoundryLocalManager()
        self.endpoint = None
        self.api_key = None
        self._session = None
        
        # Performance tracking
        self.request_count = 0
        self.total_response_time = 0.0
        
    async def __aenter__(self):
        """Async context manager entry."""
        await self.initialize()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
        
    async def initialize(self):
        """Initialize the API client and start Foundry Local service."""
        try:
            self.logger.info("Initializing Foundry Local API client...")
            
            # Initialize the manager with model
            model_info = await asyncio.to_thread(self.manager.init, self.model_alias)
            self.endpoint = self.manager.endpoint
            self.api_key = self.manager.api_key
            
            # Create HTTP session
            self._session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=self.timeout),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}"
                }
            )
            
            self.logger.info(f"Client initialized with model: {model_info.id}")
            self.logger.info(f"Endpoint: {self.endpoint}")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize client: {e}")
            raise
    
    async def close(self):
        """Close the HTTP session."""
        if self._session:
            await self._session.close()
            self._session = None
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    async def complete(self, request: CompletionRequest) -> CompletionResponse:
        """
        Generate a completion using the Foundry Local API.
        
        Args:
            request: The completion request
            
        Returns:
            CompletionResponse with the generated content
        """
        start_time = time.time()
        
        try:
            # Prepare the request payload
            messages = []
            if request.system_prompt:
                messages.append({"role": "system", "content": request.system_prompt})
            messages.append({"role": "user", "content": request.prompt})
            
            payload = {
                "model": await self._get_model_id(request.model),
                "messages": messages,
                "max_tokens": request.max_tokens,
                "temperature": request.temperature,
                "stream": False  # Non-streaming for this method
            }
            
            self.logger.debug(f"Sending completion request: {json.dumps(payload, indent=2)}")
            
            # Make the API request
            async with self._session.post(
                f"{self.endpoint}/v1/chat/completions",
                json=payload
            ) as response:
                
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"API request failed: {response.status} - {error_text}")
                
                result = await response.json()
                
                # Extract completion content
                content = result["choices"][0]["message"]["content"]
                tokens_used = result.get("usage", {}).get("total_tokens", 0)
                
                response_time = time.time() - start_time
                self._update_stats(response_time)
                
                self.logger.info(f"Completion successful in {response_time:.2f}s")
                
                return CompletionResponse(
                    content=content,
                    status=ResponseStatus.SUCCESS,
                    model=request.model,
                    tokens_used=tokens_used,
                    response_time=response_time
                )
                
        except Exception as e:
            response_time = time.time() - start_time
            self.logger.error(f"Completion failed: {e}")
            
            return CompletionResponse(
                content="",
                status=ResponseStatus.ERROR,
                model=request.model,
                response_time=response_time,
                error_message=str(e)
            )
    
    async def stream_complete(
        self, 
        request: CompletionRequest
    ) -> AsyncGenerator[CompletionResponse, None]:
        """
        Generate a streaming completion using the Foundry Local API.
        
        Args:
            request: The completion request
            
        Yields:
            CompletionResponse chunks as they are generated
        """
        start_time = time.time()
        
        try:
            # Prepare the request payload
            messages = []
            if request.system_prompt:
                messages.append({"role": "system", "content": request.system_prompt})
            messages.append({"role": "user", "content": request.prompt})
            
            payload = {
                "model": await self._get_model_id(request.model),
                "messages": messages,
                "max_tokens": request.max_tokens,
                "temperature": request.temperature,
                "stream": True
            }
            
            self.logger.debug(f"Starting streaming completion: {json.dumps(payload, indent=2)}")
            
            # Make the streaming API request
            async with self._session.post(
                f"{self.endpoint}/v1/chat/completions",
                json=payload
            ) as response:
                
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"Streaming API request failed: {response.status} - {error_text}")
                
                # Process streaming response
                async for line in response.content:
                    line = line.decode('utf-8').strip()
                    
                    if line.startswith('data: '):
                        data = line[6:]  # Remove 'data: ' prefix
                        
                        if data == '[DONE]':
                            break
                        
                        try:
                            chunk_data = json.loads(data)
                            delta = chunk_data["choices"][0].get("delta", {})
                            content = delta.get("content", "")
                            
                            if content:
                                response_time = time.time() - start_time
                                
                                yield CompletionResponse(
                                    content=content,
                                    status=ResponseStatus.SUCCESS,
                                    model=request.model,
                                    response_time=response_time
                                )
                        
                        except json.JSONDecodeError:
                            # Skip malformed JSON chunks
                            continue
                
                total_time = time.time() - start_time
                self._update_stats(total_time)
                self.logger.info(f"Streaming completion finished in {total_time:.2f}s")
                
        except Exception as e:
            self.logger.error(f"Streaming completion failed: {e}")
            yield CompletionResponse(
                content="",
                status=ResponseStatus.ERROR,
                model=request.model,
                response_time=time.time() - start_time,
                error_message=str(e)
            )
    
    async def health_check(self) -> HealthStatus:
        """
        Check the health status of the Foundry Local service.
        
        Returns:
            HealthStatus with service information
        """
        try:
            # Get service status
            async with self._session.get(f"{self.endpoint}/health") as response:
                if response.status == 200:
                    health_data = await response.json()
                else:
                    # Fallback to basic status check
                    health_data = {"status": "running"}
            
            # Get loaded models
            loaded_models = await asyncio.to_thread(self.manager.list_cached_models)
            model_names = [model.name for model in loaded_models] if loaded_models else []
            
            return HealthStatus(
                status=health_data.get("status", "unknown"),
                loaded_models=model_names,
                memory_usage=health_data.get("memory_usage", 0.0),
                uptime=health_data.get("uptime", 0.0),
                version=health_data.get("version", "unknown")
            )
            
        except Exception as e:
            self.logger.error(f"Health check failed: {e}")
            return HealthStatus(
                status="error",
                loaded_models=[],
                memory_usage=0.0,
                uptime=0.0,
                version="unknown"
            )
    
    async def list_available_models(self) -> List[Dict[str, Any]]:
        """
        List all available models in the Foundry Local catalog.
        
        Returns:
            List of model information dictionaries
        """
        try:
            models = await asyncio.to_thread(self.manager.list_catalog_models)
            return [
                {
                    "id": model.id,
                    "name": model.name,
                    "size_mb": getattr(model, 'file_size_mb', 0),
                    "provider": getattr(model, 'provider', 'unknown'),
                    "task": getattr(model, 'task', 'text-generation')
                }
                for model in models
            ]
        except Exception as e:
            self.logger.error(f"Failed to list models: {e}")
            return []
    
    async def load_model(self, model_alias: str, force_download: bool = False) -> bool:
        """
        Load a model into the Foundry Local service.
        
        Args:
            model_alias: Model alias or ID to load
            force_download: Whether to force download if not cached
            
        Returns:
            True if successful, False otherwise
        """
        try:
            self.logger.info(f"Loading model: {model_alias}")
            model_info = await asyncio.to_thread(self.manager.init, model_alias)
            self.logger.info(f"Model loaded successfully: {model_info.id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to load model {model_alias}: {e}")
            return False
    
    async def _get_model_id(self, model_alias: str) -> str:
        """Get the actual model ID from alias."""
        try:
            model_info = await asyncio.to_thread(self.manager.get_model_info, model_alias)
            return model_info.id if model_info else model_alias
        except:
            return model_alias
    
    def _update_stats(self, response_time: float):
        """Update performance statistics."""
        self.request_count += 1
        self.total_response_time += response_time
    
    @property
    def average_response_time(self) -> float:
        """Get average response time."""
        if self.request_count == 0:
            return 0.0
        return self.total_response_time / self.request_count
    
    def get_stats(self) -> Dict[str, Any]:
        """Get client performance statistics."""
        return {
            "requests_made": self.request_count,
            "total_response_time": self.total_response_time,
            "average_response_time": self.average_response_time,
            "endpoint": self.endpoint,
            "model": self.model_alias
        }


# Convenience functions for quick usage
async def quick_complete(prompt: str, model: str = "phi-4-mini") -> str:
    """
    Quick completion function for simple use cases.
    
    Args:
        prompt: The prompt to complete
        model: Model to use
        
    Returns:
        Generated completion text
    """
    async with FoundryAPIClient(model_alias=model) as client:
        request = CompletionRequest(prompt=prompt, model=model)
        response = await client.complete(request)
        return response.content


async def quick_stream(prompt: str, model: str = "phi-4-mini"):
    """
    Quick streaming completion for simple use cases.
    
    Args:
        prompt: The prompt to complete
        model: Model to use
        
    Yields:
        Generated text chunks
    """
    async with FoundryAPIClient(model_alias=model) as client:
        request = CompletionRequest(prompt=prompt, model=model, stream=True)
        async for chunk in client.stream_complete(request):
            if chunk.status == ResponseStatus.SUCCESS:
                yield chunk.content
#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import sys
import re
import json
import subprocess
from typing import Dict, Any, Optional
from openai import OpenAI

try:
    from foundry_local import FoundryLocalManager
    FOUNDRY_SDK_AVAILABLE = True
except ImportError:
    FOUNDRY_SDK_AVAILABLE = False


class ModelRouter:
    """Intelligent model router that selects appropriate models for different task types."""
    
    def __init__(self):
        self.client = None
        self.base_url = None
        self.tools = self._load_tool_registry()
        self._initialize_client()
    
    def _load_tool_registry(self) -> Dict[str, Dict[str, Any]]:
        """Load tool registry from environment or use defaults."""
        default_tools = {
            "general": {
                "model": os.environ.get("GENERAL_MODEL", "phi-4-mini"),
                "notes": "Fast general-purpose chat and Q&A",
                "temperature": 0.7
            },
            "reasoning": {
                "model": os.environ.get("REASONING_MODEL", "deepseek-r1-7b"),
                "notes": "Step-by-step analysis and logical reasoning",
                "temperature": 0.3
            },
            "code": {
                "model": os.environ.get("CODE_MODEL", "qwen2.5-7b"),
                "notes": "Code generation, debugging, and technical tasks",
                "temperature": 0.2
            },
            "creative": {
                "model": os.environ.get("CREATIVE_MODEL", "phi-4-mini"),
                "notes": "Creative writing and storytelling",
                "temperature": 0.9
            }
        }
        
        # Check for environment override
        tools_env = os.environ.get("TOOL_REGISTRY")
        if tools_env:
            try:
                custom_tools = json.loads(tools_env)
                return custom_tools
            except json.JSONDecodeError:
                print("Warning: Invalid TOOL_REGISTRY JSON, using defaults")
        
        return default_tools
    
    def _discover_base_url(self, default: str = "http://localhost:8000") -> str:
        """Discover Foundry Local service URL."""
        env_url = os.environ.get("BASE_URL")
        if env_url:
            return env_url
        
        try:
            # Try to get URL from Foundry CLI
            result = subprocess.run(
                ["foundry", "service", "status"],
                capture_output=True, text=True, timeout=3
            )
            if result.returncode == 0:
                match = re.search(r"https?://[\w\.-]+(?::\d+)?", result.stdout)
                if match:
                    return match.group(0)
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
            pass
        
        return default
    
    def _initialize_client(self):
        """Initialize OpenAI client with Foundry Local or fallback configuration."""
        if FOUNDRY_SDK_AVAILABLE:
            try:
                # Try to use any available model for client initialization
                first_model = next(iter(self.tools.values()))["model"]
                manager = FoundryLocalManager(first_model)
                
                self.client = OpenAI(
                    base_url=manager.endpoint,
                    api_key=manager.api_key
                )
                self.base_url = manager.endpoint
                print(f"Initialized Foundry Local SDK")
                return
            except Exception as e:
                print(f"Warning: Could not use Foundry SDK ({e}), falling back to manual configuration")
        
        # Fallback to manual configuration
        self.base_url = self._discover_base_url()
        api_key = os.environ.get("API_KEY", "")
        
        self.client = OpenAI(
            base_url=f"{self.base_url}/v1",
            api_key=api_key
        )
        print(f"Initialized manual configuration at {self.base_url}")
    
    def check_service_health(self) -> Dict[str, Any]:
        """Check Foundry Local service health and available models."""
        try:
            # Try to list models
            models_response = self.client.models.list()
            available_models = [model.id for model in models_response.data]
            
            return {
                "status": "healthy",
                "base_url": self.base_url,
                "available_models": available_models,
                "tools_configured": list(self.tools.keys())
            }
        except Exception as e:
            return {
                "status": "error",
                "base_url": self.base_url,
                "error": str(e)
            }
    
    def select_tool(self, user_query: str) -> str:
        """Select the most appropriate tool based on the user query."""
        query_lower = user_query.lower()
        
        # Code-related keywords
        code_keywords = ["code", "python", "function", "class", "method", "bug", "debug", 
                        "programming", "script", "algorithm", "implementation", "refactor"]
        if any(keyword in query_lower for keyword in code_keywords):
            return "code"
        
        # Reasoning keywords
        reasoning_keywords = ["why", "how", "explain", "step-by-step", "reason", "analyze", 
                             "think", "logic", "because", "cause", "compare", "evaluate"]
        if any(keyword in query_lower for keyword in reasoning_keywords):
            return "reasoning"
        
        # Creative keywords
        creative_keywords = ["story", "poem", "creative", "imagine", "write", "tale", 
                           "narrative", "fiction", "character", "plot"]
        if any(keyword in query_lower for keyword in creative_keywords):
            return "creative"
        
        # Default to general
        return "general"
    
    def chat(self, model: str, content: str, max_tokens: int = 300, temperature: Optional[float] = None) -> str:
        """Send chat completion request to the specified model."""
        try:
            params = {
                "model": model,
                "messages": [{"role": "user", "content": content}],
                "max_tokens": max_tokens
            }
            
            if temperature is not None:
                params["temperature"] = temperature
            
            response = self.client.chat.completions.create(**params)
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response with model {model}: {str(e)}"
    
    def route_and_run(self, prompt: str) -> Dict[str, Any]:
        """Route the prompt to the appropriate model and generate response."""
        tool_key = self.select_tool(prompt)
        tool_config = self.tools[tool_key]
        model = tool_config["model"]
        temperature = tool_config.get("temperature", 0.7)
        
        print(f"Selected tool: {tool_key} (model: {model})")
        
        answer = self.chat(
            model=model, 
            content=prompt, 
            max_tokens=400, 
            temperature=temperature
        )
        
        return {
            "tool": tool_key,
            "model": model,
            "tool_description": tool_config["notes"],
            "temperature": temperature,
            "answer": answer
        }


def main():
    """Main function for the model router."""
    router = ModelRouter()
    
    # Check service health
    health = router.check_service_health()
    print(f"Service Health: {json.dumps(health, indent=2)}")
    
    if health["status"] == "error":
        print(f"Warning: Service health check failed. Proceeding anyway...")
    
    # Get user prompt
    user_prompt = " ".join(sys.argv[1:]) or "Write three benefits of on-device AI in JSON format."
    print(f"\nUser Prompt: {user_prompt}")
    
    # Route and execute
    try:
        result = router.route_and_run(user_prompt)
        print(f"\nResult: {json.dumps(result, indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

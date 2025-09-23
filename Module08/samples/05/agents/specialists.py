#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from openai import OpenAI
from typing import List, Dict, Any

try:
    from foundry_local import FoundryLocalManager
    FOUNDRY_SDK_AVAILABLE = True
except ImportError:
    FOUNDRY_SDK_AVAILABLE = False


class FoundryClient:
    """Shared client for all specialist agents."""
    
    def __init__(self):
        self.client = None
        self.model_name = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize OpenAI client with Foundry Local or fallback configuration."""
        alias = os.environ.get("MODEL", "phi-4-mini")
        
        if FOUNDRY_SDK_AVAILABLE:
            try:
                # Use FoundryLocalManager for proper service management
                manager = FoundryLocalManager(alias)
                model_info = manager.get_model_info(alias)
                
                # Configure OpenAI client to use local Foundry service
                self.client = OpenAI(
                    base_url=manager.endpoint,
                    api_key=manager.api_key  # API key is not required for local usage
                )
                self.model_name = model_info.id
                print(f"Initialized Foundry Local with model: {self.model_name}")
                return
            except Exception as e:
                print(f"Warning: Could not use Foundry SDK ({e}), falling back to manual configuration")
        
        # Fallback to manual configuration
        base_url = os.environ.get("BASE_URL", "http://localhost:8000")
        api_key = os.environ.get("API_KEY", "")
        self.model_name = alias
        
        self.client = OpenAI(
            base_url=f"{base_url}/v1",
            api_key=api_key
        )
        print(f"Initialized manual configuration with model: {self.model_name}")
    
    def chat(self, messages: List[Dict[str, str]], max_tokens: int = 300, temperature: float = 0.4) -> str:
        """Send chat completion request to the model."""
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"


# Global client instance
_client = FoundryClient()


class RetrievalAgent:
    """Agent specialized in retrieving relevant information from knowledge sources."""
    
    SYSTEM = "You are a specialized retrieval agent. Your job is to extract and retrieve the most relevant information from knowledge sources based on a given query. Focus on key facts, data points, and contextual information that would be useful for decision-making."
    
    def run(self, query: str) -> str:
        """Retrieve relevant information based on the query."""
        messages = [
            {"role": "system", "content": self.SYSTEM},
            {"role": "user", "content": f"Query: {query}\n\nRetrieve the most relevant key facts, data points, and contextual information that would help answer this query or support decision-making around it."}
        ]
        return _client.chat(messages)


class ReasoningAgent:
    """Agent specialized in step-by-step analysis and reasoning."""
    
    SYSTEM = "You are a specialized reasoning agent. Your job is to analyze inputs step-by-step and produce structured, logical conclusions. Break down complex problems into manageable parts and provide clear reasoning for your conclusions."
    
    def run(self, context: str, question: str) -> str:
        """Analyze context and question to produce structured conclusions."""
        messages = [
            {"role": "system", "content": self.SYSTEM},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}\n\nAnalyze this step-by-step and provide a structured, logical conclusion with clear reasoning."}
        ]
        return _client.chat(messages, max_tokens=400)


class ExecutionAgent:
    """Agent specialized in creating actionable execution plans."""
    
    SYSTEM = "You are a specialized execution agent. Your job is to transform decisions and conclusions into concrete, actionable steps. Always format your response as valid JSON with an array of action items. Each action should be specific, measurable, and achievable."
    
    def run(self, decision: str) -> str:
        """Transform decision into actionable steps in JSON format."""
        messages = [
            {"role": "system", "content": self.SYSTEM},
            {"role": "user", "content": f"Decision/Conclusion:\n{decision}\n\nCreate 3-5 specific, actionable steps to implement this decision. Format as JSON with this structure:\n{{\"actions\": [{{\"step\": 1, \"description\": \"...\", \"priority\": \"high/medium/low\", \"timeline\": \"...\"}}]}}"}
        ]
        return _client.chat(messages, max_tokens=400, temperature=0.3)

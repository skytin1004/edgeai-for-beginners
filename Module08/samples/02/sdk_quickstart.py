#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import sys
from openai import OpenAI

try:
    from foundry_local import FoundryLocalManager
    FOUNDRY_SDK_AVAILABLE = True
except ImportError:
    FOUNDRY_SDK_AVAILABLE = False


def create_azure_client():
    """Create Azure OpenAI client."""
    azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    azure_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    azure_api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")
    
    if not azure_endpoint or not azure_api_key:
        raise ValueError("Azure OpenAI endpoint and API key are required")
    
    model = os.environ.get("MODEL", "your-deployment-name")
    client = OpenAI(
        base_url=f"{azure_endpoint}/openai",
        api_key=azure_api_key,
        default_query={"api-version": azure_api_version},
    )
    
    return client, model


def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    alias = os.environ.get("MODEL", "phi-4-mini")
    
    if FOUNDRY_SDK_AVAILABLE:
        try:
            # Use FoundryLocalManager for proper service management
            manager = FoundryLocalManager(alias)
            model_info = manager.get_model_info(alias)
            
            # Configure OpenAI client to use local Foundry service
            client = OpenAI(
                base_url=manager.endpoint,
                api_key=manager.api_key  # API key is not required for local usage
            )
            
            return client, model_info.id
        except Exception as e:
            print(f"Warning: Could not use Foundry SDK ({e}), falling back to manual configuration")
    
    # Fallback to manual configuration
    base_url = os.environ.get("BASE_URL", "http://localhost:8000")
    api_key = os.environ.get("API_KEY", "")
    model = os.environ.get("MODEL", "phi-4-mini")
    
    client = OpenAI(
        base_url=f"{base_url}/v1",
        api_key=api_key
    )
    
    return client, model


def main():
    """SDK integration example for Azure OpenAI and Foundry Local."""
    # Mode selection:
    # - Azure OpenAI: set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY
    # - Foundry Local (default): uses FoundryLocalManager or fallback configuration
    
    azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    azure_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    
    try:
        if azure_endpoint and azure_api_key:
            print("Using Azure OpenAI...")
            client, model = create_azure_client()
        else:
            print("Using Foundry Local...")
            client, model = create_foundry_client()
        
        print(f"Model: {model}")
        
        # Create chat completion with streaming
        print("\nGenerating response...")
        stream = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "Say hello from the SDK quickstart and explain what Foundry Local is."}],
            max_tokens=200,
            stream=True
        )
        
        print("\nResponse:")
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="", flush=True)
        print("\n")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

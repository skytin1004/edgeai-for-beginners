#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import sys
from openai import OpenAI
from foundry_local import FoundryLocalManager


def main():
    """Quick chat example using Foundry Local and OpenAI SDK."""
    # Get user prompt from command line or use default
    prompt = " ".join(sys.argv[1:]) or "Say hello from Foundry Local."
    
    # Check if using Azure OpenAI or Foundry Local
    azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    azure_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    azure_api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")
    
    if azure_endpoint and azure_api_key:
        # Azure OpenAI path
        model = os.environ.get("MODEL", "your-deployment-name")
        client = OpenAI(
            base_url=f"{azure_endpoint}/openai",
            api_key=azure_api_key,
            default_query={"api-version": azure_api_version},
        )
        print(f"Using Azure OpenAI with model: {model}")
    else:
        # Foundry Local path with SDK management
        alias = os.environ.get("MODEL", "phi-4-mini")
        try:
            # Use FoundryLocalManager for proper service management
            manager = FoundryLocalManager(alias)
            model_info = manager.get_model_info(alias)
            
            # Configure OpenAI client to use local Foundry service
            client = OpenAI(
                base_url=manager.endpoint,
                api_key=manager.api_key  # API key is not required for local usage
            )
            model = model_info.id
            print(f"Using Foundry Local with model: {model}")
        except Exception as e:
            # Fallback to manual configuration if SDK not available
            base_url = os.environ.get("BASE_URL", "http://localhost:8000")
            api_key = os.environ.get("API_KEY", "")
            model = os.environ.get("MODEL", "phi-4-mini")
            
            client = OpenAI(
                base_url=f"{base_url}/v1",
                api_key=api_key
            )
            print(f"Using manual configuration with model: {model}")
    
    try:
        # Create chat completion
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=128
        )
        
        # Print the response
        print("\nResponse:")
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

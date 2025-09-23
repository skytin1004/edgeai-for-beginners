#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import chainlit as cl
from openai import OpenAI

try:
    from foundry_local import FoundryLocalManager
    FOUNDRY_SDK_AVAILABLE = True
except ImportError:
    FOUNDRY_SDK_AVAILABLE = False

# Global variables for client and model
client = None
model_name = None


async def initialize_client():
    """Initialize OpenAI client with Foundry Local or fallback configuration."""
    global client, model_name
    
    # replace this with model name not alias
    alias = os.environ.get("MODEL", "Phi-4-mini-instruct-cuda-gpu")
    
    if FOUNDRY_SDK_AVAILABLE:
        try:
            # Use FoundryLocalManager for proper service management
            manager = FoundryLocalManager(alias)
            model_info = manager.get_model_info(alias)
            
            # Configure OpenAI client to use local Foundry service
            client = OpenAI(
                base_url=manager.endpoint,
                api_key=manager.api_key or "not-required"  # Ensure API key is not None
            )
            model_name = model_info.id if model_info else alias
            print(f"Initialized Foundry Local with model: {model_name}")
            return True
        except Exception as e:
            print(f"Warning: Could not use Foundry SDK ({e}), falling back to manual configuration")
    
    # Fallback to manual configuration
    base_url = os.environ.get("BASE_URL", "http://localhost:51211")
    api_key = os.environ.get("API_KEY", "not-required")
    model_name = alias
    
    client = OpenAI(
        base_url=f"{base_url}/v1",
        api_key=api_key
    )
    print(f"Initialized manual configuration with model: {model_name}")
    return True



@cl.on_chat_start
async def start():
    """Initialize the chat session."""
    global client, model_name
    
    if client is None:
        try:
            await initialize_client()
        except Exception as e:
            error_msg = f"❌ **Initialization Error**\n\nCould not initialize the AI client. Please ensure Foundry Local is running.\n\n**Error:** {str(e)}"
            await cl.Message(content=error_msg).send()
            return
    
    welcome_msg = f"""🤖 **Welcome to Foundry Local Chat!**
    
**Model:** {model_name or 'Unknown'}
**Powered by:** Microsoft Foundry Local

You can ask me anything and I'll respond using the local AI model. The conversation supports:
- ✅ Natural language processing
- ✅ Code generation and explanation
- ✅ Question answering
- ✅ Creative writing

Try asking me something!"""
    
    await cl.Message(content=welcome_msg).send()


@cl.on_message
async def main(message: cl.Message):
    """Handle incoming messages and generate responses."""
    global client, model_name
    
    if client is None:
        await cl.Message(content="❌ Error: Client not initialized. Please restart the application.").send()
        return
    
    try:
        # Show typing indicator
        msg = cl.Message(content="")
        await msg.send()
        
        # Create streaming response
        stream = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local. Provide clear, accurate, and helpful responses."},
                {"role": "user", "content": message.content}
            ],
            max_tokens=500,
            temperature=0.7,
            stream=True
        )
        
        # Stream the response
        for chunk in stream:
            if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
                delta_content = chunk.choices[0].delta.content
                if delta_content is not None:
                    await msg.stream_token(delta_content)
        
        # Finalize the message
        await msg.update()
        
    except Exception as e:
        error_msg = f"❌ **Error generating response:**\n\n{str(e)}\n\n💡 **Troubleshooting:**\n1. Ensure Foundry Local is running: `foundry service status`\n2. Check if model is loaded: `foundry service ps`\n3. Verify endpoint: `curl http://localhost:51211/v1/models`"
        await cl.Message(content=error_msg).send()


# Note: Client initialization happens in @cl.on_chat_start to ensure async context
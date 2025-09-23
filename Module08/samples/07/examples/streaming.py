#!/usr/bin/env python3
"""
Streaming Response Example for Foundry Local API Client

This example demonstrates real-time streaming responses from Foundry Local,
perfect for chat applications and real-time content generation.
"""

import asyncio
import sys
import os
import time
from typing import AsyncGenerator

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api_client import FoundryAPIClient, CompletionRequest, quick_stream
from rich.console import Console
from rich.live import Live
from rich.text import Text
from rich.panel import Panel


# Initialize rich console for better output
console = Console()


async def basic_streaming_example():
    """Demonstrate basic streaming with the API client."""
    console.print("\n🌊 Basic Streaming Example", style="bold blue")
    console.print("=" * 50)
    
    # Method 1: Using the convenience function
    console.print("\n📝 Method 1: Quick Streaming Function", style="bold")
    
    prompt = "Write a short story about a robot learning to paint."
    console.print(f"Prompt: {prompt}", style="cyan")
    console.print("\n💭 Response:", style="green")
    
    response_text = ""
    try:
        async for chunk in quick_stream(prompt, model="phi-4-mini"):
            response_text += chunk
            console.print(chunk, end="", style="white")
        console.print()  # New line after completion
    except Exception as e:
        console.print(f"\n❌ Error: {e}", style="red")
    
    # Method 2: Using the full API client
    console.print(f"\n📝 Method 2: Full API Client Streaming", style="bold")
    
    async with FoundryAPIClient(model_alias="phi-4-mini") as client:
        request = CompletionRequest(
            prompt="Explain the benefits of edge computing in 3 paragraphs.",
            model="phi-4-mini",
            max_tokens=400,
            temperature=0.7,
            system_prompt="You are a technical writer who explains complex topics clearly."
        )
        
        console.print(f"Prompt: {request.prompt}", style="cyan")
        console.print("\n💭 Streaming Response:", style="green")
        
        full_response = ""
        start_time = time.time()
        chunk_count = 0
        
        try:
            async for response in client.stream_complete(request):
                if response.status.value == "success":
                    full_response += response.content
                    chunk_count += 1
                    console.print(response.content, end="", style="white")
                else:
                    console.print(f"\n❌ Error in chunk: {response.error_message}", style="red")
                    break
            
            end_time = time.time()
            console.print(f"\n\n📊 Stats: {chunk_count} chunks in {end_time - start_time:.2f}s", style="yellow")
            
        except Exception as e:
            console.print(f"\n❌ Exception: {e}", style="red")


async def interactive_chat_example():
    """Demonstrate an interactive chat session with streaming."""
    console.print("\n💬 Interactive Chat with Streaming", style="bold blue")
    console.print("=" * 50)
    console.print("Type your questions (or 'quit' to exit)", style="yellow")
    
    async with FoundryAPIClient(model_alias="phi-4-mini") as client:
        chat_history = []
        
        while True:
            # Get user input
            try:
                user_input = console.input("\n👤 You: ")
                if user_input.lower() in ['quit', 'exit', 'q']:
                    break
                
                if not user_input.strip():
                    continue
                
                chat_history.append(f"User: {user_input}")
                
                # Create request with chat context
                context = "\n".join(chat_history[-6:])  # Keep last 6 exchanges
                request = CompletionRequest(
                    prompt=user_input,
                    model="phi-4-mini",
                    max_tokens=300,
                    temperature=0.8,
                    system_prompt=f"You are a helpful assistant. Previous conversation context:\n{context}"
                )
                
                # Stream response
                console.print("🤖 Assistant: ", end="", style="green")
                assistant_response = ""
                
                async for response in client.stream_complete(request):
                    if response.status.value == "success":
                        assistant_response += response.content
                        console.print(response.content, end="", style="white")
                    else:
                        console.print(f"❌ Error: {response.error_message}", style="red")
                        break
                
                if assistant_response:
                    chat_history.append(f"Assistant: {assistant_response}")
                
                console.print()  # New line after response
                
            except KeyboardInterrupt:
                console.print("\n👋 Chat session ended.", style="yellow")
                break
            except Exception as e:
                console.print(f"\n❌ Error: {e}", style="red")


async def live_updating_display():
    """Demonstrate live updating display with rich."""
    console.print("\n📺 Live Updating Display Example", style="bold blue")
    console.print("=" * 50)
    
    async with FoundryAPIClient(model_alias="phi-4-mini") as client:
        request = CompletionRequest(
            prompt="Write a detailed explanation of how neural networks learn, including the role of backpropagation.",
            model="phi-4-mini",
            max_tokens=600,
            temperature=0.7
        )
        
        # Use Rich Live to update display in real-time
        with Live(console=console, refresh_per_second=10) as live:
            accumulated_text = ""
            start_time = time.time()
            
            async for response in client.stream_complete(request):
                if response.status.value == "success":
                    accumulated_text += response.content
                    
                    # Create a panel with the current text
                    panel = Panel(
                        Text(accumulated_text),
                        title="🧠 Neural Network Explanation",
                        title_align="left",
                        border_style="blue"
                    )
                    
                    live.update(panel)
                    
                    # Small delay to make the streaming visible
                    await asyncio.sleep(0.05)
                else:
                    live.update(Panel(f"❌ Error: {response.error_message}", border_style="red"))
                    break
            
            end_time = time.time()
            
            # Final update with stats
            final_panel = Panel(
                Text(accumulated_text) + Text(f"\n\n⏱️ Generated in {end_time - start_time:.2f} seconds", style="italic cyan"),
                title="🧠 Neural Network Explanation - Complete",
                title_align="left",
                border_style="green"
            )
            
            live.update(final_panel)
            
            # Keep the display for a moment
            await asyncio.sleep(2)


async def multiple_concurrent_streams():
    """Demonstrate handling multiple concurrent streaming requests."""
    console.print("\n🚀 Multiple Concurrent Streams Example", style="bold blue")
    console.print("=" * 50)
    
    prompts = [
        "Explain quantum computing in simple terms.",
        "What are the key principles of sustainable software development?",
        "Describe the future of artificial intelligence in healthcare."
    ]
    
    async def stream_single_prompt(client: FoundryAPIClient, prompt: str, stream_id: int) -> str:
        """Stream a single prompt and collect the full response."""
        request = CompletionRequest(
            prompt=prompt,
            model="phi-4-mini",
            max_tokens=200,
            temperature=0.7
        )
        
        console.print(f"\n🔄 Stream {stream_id} starting: {prompt[:50]}...", style="cyan")
        
        full_response = ""
        start_time = time.time()
        
        try:
            async for response in client.stream_complete(request):
                if response.status.value == "success":
                    full_response += response.content
                else:
                    console.print(f"❌ Stream {stream_id} error: {response.error_message}", style="red")
                    return ""
            
            end_time = time.time()
            console.print(f"✅ Stream {stream_id} completed in {end_time - start_time:.2f}s", style="green")
            return full_response
            
        except Exception as e:
            console.print(f"❌ Stream {stream_id} exception: {e}", style="red")
            return ""
    
    async with FoundryAPIClient(model_alias="phi-4-mini") as client:
        # Start all streams concurrently
        start_time = time.time()
        
        tasks = [
            stream_single_prompt(client, prompt, i + 1)
            for i, prompt in enumerate(prompts)
        ]
        
        # Wait for all to complete
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        end_time = time.time()
        
        # Display results
        console.print(f"\n📊 All streams completed in {end_time - start_time:.2f}s", style="yellow")
        
        for i, (prompt, result) in enumerate(zip(prompts, results)):
            if isinstance(result, str) and result:
                console.print(f"\n📝 Stream {i + 1} Result:", style="bold")
                console.print(f"Q: {prompt}", style="cyan")
                console.print(f"A: {result[:150]}...", style="white")
            else:
                console.print(f"\n❌ Stream {i + 1} failed: {result}", style="red")


async def token_by_token_analysis():
    """Demonstrate analyzing tokens as they arrive."""
    console.print("\n🔍 Token-by-Token Analysis Example", style="bold blue")
    console.print("=" * 50)
    
    async with FoundryAPIClient(model_alias="phi-4-mini") as client:
        request = CompletionRequest(
            prompt="List the top 5 programming languages for AI development and explain why each is useful.",
            model="phi-4-mini",
            max_tokens=400,
            temperature=0.5
        )
        
        console.print(f"Prompt: {request.prompt}", style="cyan")
        console.print("\n📊 Token Analysis:", style="yellow")
        
        word_count = 0
        sentence_count = 0
        accumulated_text = ""
        start_time = time.time()
        
        async for response in client.stream_complete(request):
            if response.status.value == "success":
                chunk = response.content
                accumulated_text += chunk
                
                # Count words and sentences in this chunk
                words_in_chunk = len(chunk.split())
                sentences_in_chunk = chunk.count('.') + chunk.count('!') + chunk.count('?')
                
                word_count += words_in_chunk
                sentence_count += sentences_in_chunk
                
                # Display token with analysis
                console.print(chunk, end="", style="white")
                
                # Periodic stats update
                if word_count > 0 and word_count % 20 == 0:  # Every 20 words
                    elapsed = time.time() - start_time
                    wpm = (word_count / elapsed) * 60 if elapsed > 0 else 0
                    console.print(f" [📊 {word_count} words, {wpm:.1f} WPM]", style="dim yellow", end="")
            
            else:
                console.print(f"\n❌ Error: {response.error_message}", style="red")
                break
        
        # Final statistics
        end_time = time.time()
        total_time = end_time - start_time
        final_wpm = (word_count / total_time) * 60 if total_time > 0 else 0
        
        console.print(f"\n\n📈 Final Statistics:", style="bold yellow")
        console.print(f"   Total Words: {word_count}")
        console.print(f"   Total Sentences: {sentence_count}")
        console.print(f"   Generation Time: {total_time:.2f}s")
        console.print(f"   Average Speed: {final_wpm:.1f} words/minute")
        console.print(f"   Characters: {len(accumulated_text)}")


async def main():
    """Run all streaming examples."""
    console.print("🌊 Foundry Local API Client - Streaming Examples", style="bold magenta")
    console.print("=" * 60)
    
    examples = [
        ("Basic Streaming", basic_streaming_example),
        ("Live Display", live_updating_display),
        ("Multiple Concurrent Streams", multiple_concurrent_streams),
        ("Token Analysis", token_by_token_analysis),
        ("Interactive Chat", interactive_chat_example),  # Run last as it's interactive
    ]
    
    try:
        for name, example_func in examples:
            console.print(f"\n🎯 Running: {name}", style="bold blue")
            await example_func()
            
            if name != "Interactive Chat":  # Don't wait after interactive chat
                console.print("\n⏸️  Press Enter to continue to next example...")
                input()
        
        console.print("\n✅ All streaming examples completed!", style="bold green")
        console.print("\n🎓 Next Steps:", style="yellow")
        console.print("   - Try batch processing: python examples/batch_processing.py")
        console.print("   - Check production patterns: python examples/production.py")
        
    except KeyboardInterrupt:
        console.print("\n⏹️  Examples interrupted by user.", style="yellow")
    except Exception as e:
        console.print(f"\n❌ Unexpected error: {e}", style="red")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
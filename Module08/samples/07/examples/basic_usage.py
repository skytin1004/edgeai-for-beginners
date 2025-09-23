#!/usr/bin/env python3
"""
Basic Usage Example for Foundry Local API Client

This example demonstrates the simplest way to use the Foundry Local API client
for text completion tasks.
"""

import asyncio
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api_client import FoundryAPIClient, CompletionRequest, quick_complete


async def basic_completion_example():
    """Demonstrate basic completion with the API client."""
    print("🚀 Basic Foundry Local API Client Example")
    print("=" * 50)
    
    # Method 1: Using the convenience function
    print("\n📝 Method 1: Quick Completion Function")
    try:
        response = await quick_complete(
            prompt="Explain what machine learning is in simple terms.",
            model="phi-4-mini"
        )
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Method 2: Using the full API client
    print("\n📝 Method 2: Full API Client")
    async with FoundryAPIClient(model_alias="phi-4-mini") as client:
        try:
            # Create a completion request
            request = CompletionRequest(
                prompt="What are the benefits of edge AI computing?",
                model="phi-4-mini",
                max_tokens=300,
                temperature=0.7,
                system_prompt="You are a helpful AI assistant that explains technical concepts clearly."
            )
            
            # Get the completion
            response = await client.complete(request)
            
            if response.status.value == "success":
                print(f"✅ Success!")
                print(f"📄 Content: {response.content}")
                print(f"🔢 Tokens Used: {response.tokens_used}")
                print(f"⏱️  Response Time: {response.response_time:.2f}s")
            else:
                print(f"❌ Error: {response.error_message}")
        
        except Exception as e:
            print(f"❌ Exception: {e}")


async def multiple_completions_example():
    """Demonstrate multiple completions with the same client."""
    print("\n🔄 Multiple Completions Example")
    print("=" * 50)
    
    questions = [
        "What is artificial intelligence?",
        "How does neural network training work?",
        "What are the advantages of running AI models locally?",
        "Explain the difference between CPU and GPU for AI workloads."
    ]
    
    async with FoundryAPIClient(model_alias="phi-4-mini") as client:
        for i, question in enumerate(questions, 1):
            print(f"\n📝 Question {i}: {question}")
            
            request = CompletionRequest(
                prompt=question,
                model="phi-4-mini",
                max_tokens=150,
                temperature=0.5
            )
            
            response = await client.complete(request)
            
            if response.status.value == "success":
                print(f"💡 Answer: {response.content[:200]}...")
                print(f"⏱️  Time: {response.response_time:.2f}s")
            else:
                print(f"❌ Error: {response.error_message}")
        
        # Show performance stats
        stats = client.get_stats()
        print(f"\n📊 Performance Statistics:")
        print(f"   Total Requests: {stats['requests_made']}")
        print(f"   Average Response Time: {stats['average_response_time']:.2f}s")


async def system_prompt_example():
    """Demonstrate using system prompts for role-based responses."""
    print("\n🎭 System Prompt Example")
    print("=" * 50)
    
    scenarios = [
        {
            "role": "Technical Expert",
            "system_prompt": "You are a senior software engineer with expertise in AI and machine learning. Provide detailed, technical explanations.",
            "question": "How does backpropagation work in neural networks?"
        },
        {
            "role": "Simple Explainer",
            "system_prompt": "You are a teacher explaining concepts to beginners. Use simple language and analogies.",
            "question": "How does backpropagation work in neural networks?"
        },
        {
            "role": "Business Advisor",
            "system_prompt": "You are a business consultant focused on practical applications and ROI.",
            "question": "What are the business benefits of implementing edge AI?"
        }
    ]
    
    async with FoundryAPIClient(model_alias="phi-4-mini") as client:
        for scenario in scenarios:
            print(f"\n🎯 Role: {scenario['role']}")
            print(f"❓ Question: {scenario['question']}")
            
            request = CompletionRequest(
                prompt=scenario['question'],
                model="phi-4-mini",
                max_tokens=200,
                temperature=0.7,
                system_prompt=scenario['system_prompt']
            )
            
            response = await client.complete(request)
            
            if response.status.value == "success":
                print(f"💬 Response: {response.content}")
            else:
                print(f"❌ Error: {response.error_message}")


async def health_and_models_example():
    """Demonstrate health checking and model management."""
    print("\n🏥 Health Check and Model Management Example")
    print("=" * 50)
    
    async with FoundryAPIClient(model_alias="phi-4-mini") as client:
        # Check service health
        print("\n🔍 Checking service health...")
        health = await client.health_check()
        print(f"   Status: {health.status}")
        print(f"   Loaded Models: {', '.join(health.loaded_models) if health.loaded_models else 'None'}")
        print(f"   Memory Usage: {health.memory_usage:.1f}%")
        
        # List available models
        print("\n📋 Available models in catalog...")
        models = await client.list_available_models()
        for model in models[:5]:  # Show first 5 models
            print(f"   - {model['name']} ({model['id']}) - {model['size_mb']}MB")
        
        if len(models) > 5:
            print(f"   ... and {len(models) - 5} more models")


async def error_handling_example():
    """Demonstrate error handling and recovery."""
    print("\n🚨 Error Handling Example")
    print("=" * 50)
    
    async with FoundryAPIClient(model_alias="phi-4-mini") as client:
        # Test with invalid model
        print("\n🧪 Testing with invalid model...")
        request = CompletionRequest(
            prompt="Test prompt",
            model="non-existent-model",
            max_tokens=50
        )
        
        response = await client.complete(request)
        if response.status.value == "error":
            print(f"✅ Error handled gracefully: {response.error_message}")
        
        # Test with very long prompt (potential timeout)
        print("\n🧪 Testing with very long prompt...")
        long_prompt = "Explain artificial intelligence. " * 1000  # Very long prompt
        
        request = CompletionRequest(
            prompt=long_prompt,
            model="phi-4-mini",
            max_tokens=100
        )
        
        response = await client.complete(request)
        if response.status.value == "success":
            print("✅ Long prompt handled successfully")
        else:
            print(f"⚠️  Long prompt failed: {response.error_message}")


async def main():
    """Run all examples."""
    print("🎯 Foundry Local API Client - Basic Usage Examples")
    print("=" * 60)
    
    try:
        await basic_completion_example()
        await multiple_completions_example()
        await system_prompt_example()
        await health_and_models_example()
        await error_handling_example()
        
        print("\n✅ All examples completed successfully!")
        print("\n🎓 Next Steps:")
        print("   - Try the streaming example: python examples/streaming.py")
        print("   - Explore batch processing: python examples/batch_processing.py")
        print("   - Check production patterns: python examples/production.py")
        
    except KeyboardInterrupt:
        print("\n⏹️  Examples interrupted by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
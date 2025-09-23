#!/usr/bin/env python3
"""
Basic Foundry Local Tools Example

This example demonstrates the simplest way to create and use tools
powered by Microsoft Foundry Local.
"""

import asyncio
import sys
import os
from typing import Dict, Any, List

# Add parent directory for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from foundry_local import FoundryLocalManager
import openai
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Initialize rich console
console = Console()


class SimpleFoundryTool:
    """A simple wrapper for creating Foundry Local tools."""
    
    def __init__(self, name: str, description: str, model: str = "phi-4-mini"):
        """
        Initialize a Foundry tool.
        
        Args:
            name: Tool name
            description: Tool description
            model: Foundry Local model to use
        """
        self.name = name
        self.description = description
        self.model = model
        self.manager = None
        self.client = None
        
    async def initialize(self):
        """Initialize the Foundry Local connection."""
        try:
            self.manager = FoundryLocalManager()
            model_info = await asyncio.to_thread(self.manager.init, self.model)
            
            self.client = openai.OpenAI(
                base_url=self.manager.endpoint,
                api_key=self.manager.api_key
            )
            
            console.print(f"✅ Tool '{self.name}' initialized with model: {model_info.id}")
            return True
            
        except Exception as e:
            console.print(f"❌ Failed to initialize tool '{self.name}': {e}")
            return False
    
    async def call(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """
        Call the tool with a prompt.
        
        Args:
            prompt: Input prompt for the tool
            **kwargs: Additional parameters
            
        Returns:
            Tool response
        """
        try:
            if not self.client:
                await self.initialize()
            
            # Get model ID
            model_id = await asyncio.to_thread(self.manager.get_model_info, self.model)
            
            # Create request
            messages = [
                {"role": "system", "content": f"You are {self.description}"},
                {"role": "user", "content": prompt}
            ]
            
            # Call Foundry Local
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model=model_id.id,
                messages=messages,
                max_tokens=kwargs.get('max_tokens', 500),
                temperature=kwargs.get('temperature', 0.7)
            )
            
            content = response.choices[0].message.content
            
            return {
                "success": True,
                "result": content,
                "tool": self.name,
                "model": self.model,
                "tokens_used": response.usage.total_tokens if response.usage else 0
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "tool": self.name
            }


# Define example tools
async def create_example_tools() -> List[SimpleFoundryTool]:
    """Create a set of example tools."""
    
    tools = [
        SimpleFoundryTool(
            name="code_reviewer",
            description="a code review expert that analyzes code quality and suggests improvements",
            model="phi-4-mini"
        ),
        SimpleFoundryTool(
            name="content_summarizer", 
            description="a content summarization specialist that creates concise summaries",
            model="qwen2.5-0.5b"
        ),
        SimpleFoundryTool(
            name="technical_writer",
            description="a technical documentation expert that creates clear technical content",
            model="phi-3.5-mini"
        ),
        SimpleFoundryTool(
            name="problem_solver",
            description="a problem-solving assistant that breaks down complex problems",
            model="phi-4-mini"
        )
    ]
    
    # Initialize all tools
    for tool in tools:
        await tool.initialize()
    
    return tools


async def demonstrate_basic_tool_usage():
    """Demonstrate basic tool usage patterns."""
    console.print("\n🔧 Basic Tool Usage Demonstration", style="bold blue")
    console.print("=" * 50)
    
    # Create tools
    tools = await create_example_tools()
    
    # Example 1: Code Review
    console.print(Panel("\n📝 Example 1: Code Review Tool", border_style="green"))
    
    code_to_review = """
def calculate_average(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum / len(numbers)
"""
    
    code_reviewer = next(tool for tool in tools if tool.name == "code_reviewer")
    result = await code_reviewer.call(
        f"Please review this Python code and suggest improvements:\n\n{code_to_review}"
    )
    
    if result["success"]:
        console.print("✅ Code Review Result:", style="green")
        console.print(result["result"])
        console.print(f"Tokens used: {result['tokens_used']}")
    else:
        console.print(f"❌ Error: {result['error']}", style="red")
    
    console.print("\n" + "─" * 50)
    
    # Example 2: Content Summarization
    console.print(Panel("\n📄 Example 2: Content Summarization Tool", border_style="blue"))
    
    long_content = """
    Artificial Intelligence (AI) is transforming the way we work, learn, and interact with technology. 
    Edge AI, in particular, represents a significant shift from cloud-based processing to local, 
    on-device computation. This approach offers several advantages including reduced latency, 
    improved privacy, and decreased bandwidth usage. Microsoft Foundry Local is an example of 
    this trend, allowing developers to run powerful AI models directly on local hardware. 
    This capability enables real-time processing, offline functionality, and better data privacy. 
    As edge computing continues to evolve, we can expect to see more sophisticated AI applications 
    running locally, from smart cameras to autonomous vehicles to intelligent personal assistants.
    """
    
    summarizer = next(tool for tool in tools if tool.name == "content_summarizer")
    result = await summarizer.call(
        f"Please create a concise summary of this content:\n\n{long_content}"
    )
    
    if result["success"]:
        console.print("✅ Summary Result:", style="green")
        console.print(result["result"])
        console.print(f"Tokens used: {result['tokens_used']}")
    else:
        console.print(f"❌ Error: {result['error']}", style="red")
    
    console.print("\n" + "─" * 50)


async def demonstrate_tool_composition():
    """Demonstrate combining multiple tools for complex tasks."""
    console.print("\n🔄 Tool Composition Demonstration", style="bold magenta")
    console.print("=" * 50)
    
    tools = await create_example_tools()
    
    # Complex task: Analyze a technical problem and create documentation
    problem_description = """
    Our web application is experiencing slow response times during peak hours. 
    Users report that page load times increase from 2 seconds to over 10 seconds 
    when traffic is high. We suspect database connection pooling issues, but we're 
    not sure how to diagnose and fix the problem.
    """
    
    console.print(Panel("🎯 Complex Task: Performance Problem Analysis", border_style="yellow"))
    console.print(f"Problem: {problem_description}")
    
    # Step 1: Problem analysis
    console.print("\n📋 Step 1: Problem Analysis")
    problem_solver = next(tool for tool in tools if tool.name == "problem_solver")
    
    analysis_result = await problem_solver.call(
        f"Analyze this performance problem and suggest a systematic approach to diagnose and solve it:\n\n{problem_description}"
    )
    
    if analysis_result["success"]:
        console.print("✅ Analysis Complete:")
        analysis = analysis_result["result"]
        console.print(analysis[:300] + "..." if len(analysis) > 300 else analysis)
        
        # Step 2: Create documentation
        console.print("\n📝 Step 2: Creating Technical Documentation")
        tech_writer = next(tool for tool in tools if tool.name == "technical_writer")
        
        doc_result = await tech_writer.call(
            f"Create a technical troubleshooting guide based on this analysis:\n\n{analysis}"
        )
        
        if doc_result["success"]:
            console.print("✅ Documentation Created:")
            documentation = doc_result["result"]
            console.print(documentation[:400] + "..." if len(documentation) > 400 else documentation)
            
            # Step 3: Create summary
            console.print("\n📄 Step 3: Creating Executive Summary") 
            summarizer = next(tool for tool in tools if tool.name == "content_summarizer")
            
            summary_result = await summarizer.call(
                f"Create an executive summary of this technical analysis and solution:\n\n{documentation}"
            )
            
            if summary_result["success"]:
                console.print("✅ Executive Summary:")
                console.print(summary_result["result"])
                
                # Show composition results
                console.print("\n📊 Tool Composition Results:", style="bold green")
                table = Table(title="Tool Chain Execution")
                table.add_column("Step", style="cyan")
                table.add_column("Tool", style="yellow")
                table.add_column("Tokens", style="magenta")
                table.add_column("Status", style="green")
                
                table.add_row("1", "Problem Solver", str(analysis_result["tokens_used"]), "✅ Success")
                table.add_row("2", "Technical Writer", str(doc_result["tokens_used"]), "✅ Success")
                table.add_row("3", "Content Summarizer", str(summary_result["tokens_used"]), "✅ Success")
                
                total_tokens = (analysis_result["tokens_used"] + 
                              doc_result["tokens_used"] + 
                              summary_result["tokens_used"])
                table.add_row("Total", "All Tools", str(total_tokens), "✅ Complete")
                
                console.print(table)
            
        else:
            console.print(f"❌ Documentation failed: {doc_result['error']}", style="red")
    else:
        console.print(f"❌ Analysis failed: {analysis_result['error']}", style="red")


async def demonstrate_parallel_tool_execution():
    """Demonstrate running multiple tools in parallel."""
    console.print("\n⚡ Parallel Tool Execution Demonstration", style="bold cyan")
    console.print("=" * 50)
    
    tools = await create_example_tools()
    
    # Define parallel tasks
    tasks = [
        ("code_reviewer", "Review this function for performance issues: def fibonacci(n): return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)"),
        ("technical_writer", "Write documentation for a REST API endpoint that returns user profile information"),
        ("problem_solver", "How would you approach debugging intermittent network timeouts in a distributed system?"),
        ("content_summarizer", "Summarize the key benefits of microservices architecture versus monolithic architecture")
    ]
    
    console.print(f"🚀 Executing {len(tasks)} tools in parallel...")
    
    # Execute all tasks concurrently
    async def execute_task(tool_name: str, prompt: str):
        tool = next(t for t in tools if t.name == tool_name)
        start_time = asyncio.get_event_loop().time()
        
        result = await tool.call(prompt)
        
        execution_time = asyncio.get_event_loop().time() - start_time
        result["execution_time"] = execution_time
        result["task_prompt"] = prompt[:50] + "..." if len(prompt) > 50 else prompt
        
        return result
    
    # Run all tasks in parallel
    results = await asyncio.gather(*[
        execute_task(tool_name, prompt) for tool_name, prompt in tasks
    ])
    
    # Display results
    table = Table(title="Parallel Tool Execution Results")
    table.add_column("Tool", style="cyan")
    table.add_column("Task", style="white")
    table.add_column("Time (s)", style="yellow")
    table.add_column("Tokens", style="magenta") 
    table.add_column("Status", style="green")
    
    total_tokens = 0
    successful_tasks = 0
    
    for result in results:
        status = "✅ Success" if result["success"] else "❌ Failed"
        tokens = result.get("tokens_used", 0)
        total_tokens += tokens
        
        if result["success"]:
            successful_tasks += 1
        
        table.add_row(
            result["tool"],
            result["task_prompt"],
            f"{result.get('execution_time', 0):.2f}",
            str(tokens),
            status
        )
    
    console.print(table)
    
    # Summary
    console.print(f"\n📊 Execution Summary:", style="bold yellow")
    console.print(f"   Successful tasks: {successful_tasks}/{len(tasks)}")
    console.print(f"   Total tokens used: {total_tokens}")
    console.print(f"   Average tokens per task: {total_tokens / len(tasks):.1f}")


async def demonstrate_streaming_tools():
    """Demonstrate streaming tool responses."""
    console.print("\n🌊 Streaming Tool Responses Demonstration", style="bold green")
    console.print("=" * 50)
    
    # Note: This is a simplified streaming demo
    # Full streaming implementation would require more complex client setup
    
    console.print("📝 Generating code documentation with streaming...")
    
    code_sample = """
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
"""
    
    # Simulate streaming response (in real implementation, this would stream from Foundry Local)
    console.print("🤖 Technical Writer Tool Response:")
    console.print("─" * 40)
    
    streaming_text = f"""
# Binary Search Function Documentation

## Overview
This function implements the binary search algorithm to find a target value in a sorted array.

## Parameters
- `arr`: A sorted list of comparable elements
- `target`: The value to search for in the array

## Returns
- `int`: The index of the target element if found, or -1 if not found

## Algorithm
The function uses the divide-and-conquer approach:
1. Initialize left and right pointers
2. Calculate the middle index
3. Compare middle element with target
4. Adjust search bounds based on comparison
5. Repeat until found or search space exhausted

## Time Complexity
- **Best Case**: O(1) - target is at the middle
- **Average Case**: O(log n) 
- **Worst Case**: O(log n)

## Space Complexity
O(1) - constant extra space used

## Example Usage
```python
numbers = [1, 3, 5, 7, 9, 11, 13]
index = binary_search(numbers, 7)  # Returns 3
index = binary_search(numbers, 6)  # Returns -1
```
"""
    
    # Simulate streaming by printing chunks with delays
    import time
    chunks = streaming_text.split('\n')
    
    for chunk in chunks:
        if chunk.strip():  # Skip empty lines
            console.print(chunk)
            await asyncio.sleep(0.1)  # Simulate streaming delay
    
    console.print("\n✅ Streaming documentation complete!")


async def demonstrate_tool_error_handling():
    """Demonstrate proper error handling with tools."""
    console.print("\n🚨 Tool Error Handling Demonstration", style="bold red")
    console.print("=" * 50)
    
    # Create a tool that will fail
    failing_tool = SimpleFoundryTool(
        name="failing_tool",
        description="a tool that demonstrates error handling",
        model="non-existent-model"  # This will cause an error
    )
    
    console.print("🧪 Testing error scenarios...")
    
    # Test 1: Invalid model
    console.print("\n📋 Test 1: Invalid model name")
    result = await failing_tool.call("This should fail")
    
    if not result["success"]:
        console.print("✅ Error handled correctly:", style="green")
        console.print(f"   Error: {result['error']}")
    
    # Test 2: Network timeout simulation
    console.print("\n📋 Test 2: Tool recovery and retry")
    
    valid_tool = SimpleFoundryTool(
        name="recovery_tool",
        description="a tool that demonstrates recovery",
        model="phi-4-mini"
    )
    
    # Try to use tool and handle initialization
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            console.print(f"   Attempt {retry_count + 1}/{max_retries}")
            
            result = await valid_tool.call("Simple test prompt")
            
            if result["success"]:
                console.print("✅ Tool recovered successfully!", style="green")
                console.print(f"   Result: {result['result'][:100]}...")
                break
            else:
                console.print(f"❌ Attempt {retry_count + 1} failed: {result['error']}")
                
        except Exception as e:
            console.print(f"❌ Exception on attempt {retry_count + 1}: {e}")
        
        retry_count += 1
        if retry_count < max_retries:
            console.print("   Retrying in 2 seconds...")
            await asyncio.sleep(2)
    
    if retry_count >= max_retries:
        console.print("❌ All retry attempts exhausted", style="red")
    
    console.print("\n💡 Error Handling Best Practices:")
    console.print("   1. Always check tool.success before using results")
    console.print("   2. Implement retry logic with exponential backoff")
    console.print("   3. Log errors for debugging and monitoring")
    console.print("   4. Provide fallback mechanisms when possible")
    console.print("   5. Validate inputs before calling tools")


async def main():
    """Run all basic tool demonstrations."""
    console.print("🔧 Foundry Local Tools - Basic Examples", style="bold magenta")
    console.print("=" * 60)
    
    examples = [
        ("Basic Tool Usage", demonstrate_basic_tool_usage),
        ("Tool Composition", demonstrate_tool_composition), 
        ("Parallel Execution", demonstrate_parallel_tool_execution),
        ("Streaming Responses", demonstrate_streaming_tools),
        ("Error Handling", demonstrate_tool_error_handling)
    ]
    
    try:
        for name, demo_func in examples:
            console.print(f"\n🎯 Running: {name}", style="bold blue")
            await demo_func()
            
            console.print("\n⏸️  Press Enter to continue to next example...")
            input()
        
        console.print("\n✅ All basic tool examples completed!", style="bold green")
        console.print("\n🎓 Next Steps:", style="yellow")
        console.print("   - Try the LangChain integration: python examples/langchain_demo.py")
        console.print("   - Explore REST API server: python examples/rest_api_server.py")
        console.print("   - Check CLI application: python examples/cli_application.py")
        console.print("   - Test Jupyter notebook: jupyter notebook examples/jupyter_notebook.ipynb")
        
    except KeyboardInterrupt:
        console.print("\n⏹️  Examples interrupted by user.", style="yellow")
    except Exception as e:
        console.print(f"\n❌ Unexpected error: {e}", style="red")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
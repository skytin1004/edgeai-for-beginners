#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
from typing import Dict, Any
from .specialists import RetrievalAgent, ReasoningAgent, ExecutionAgent


class Coordinator:
    """Multi-agent coordinator that orchestrates specialist agents to handle complex tasks."""
    
    def __init__(self):
        """Initialize the coordinator with specialist agents."""
        self.retrieval = RetrievalAgent()
        self.reasoning = ReasoningAgent()
        self.execution = ExecutionAgent()
    
    def handle(self, user_goal: str) -> Dict[str, Any]:
        """
        Orchestrate multiple agents to handle a complex user goal.
        
        Args:
            user_goal: The user's high-level goal or request
            
        Returns:
            Dictionary containing the goal, context, decision, and actions
        """
        print(f"🎯 **Coordinator:** Processing goal: {user_goal}")
        
        # Step 1: Retrieve relevant context
        print("📚 **Step 1:** Retrieving context...")
        context = self.retrieval.run(user_goal)
        print(f"Context: {context[:100]}...")
        
        # Step 2: Analyze and reason about the context
        print("🧠 **Step 2:** Analyzing and reasoning...")
        decision = self.reasoning.run(context, user_goal)
        print(f"Decision: {decision[:100]}...")
        
        # Step 3: Create actionable execution plan
        print("⚡ **Step 3:** Creating execution plan...")
        actions = self.execution.run(decision)
        print(f"Actions: {actions[:100]}...")
        
        result = {
            "goal": user_goal,
            "context": context,
            "decision": decision,
            "actions": actions,
            "agent_flow": ["retrieval", "reasoning", "execution"]
        }
        
        return result
    
    def handle_with_feedback(self, user_goal: str, feedback_rounds: int = 1) -> Dict[str, Any]:
        """
        Handle a goal with multiple feedback rounds for refinement.
        
        Args:
            user_goal: The user's high-level goal or request
            feedback_rounds: Number of feedback rounds to perform
            
        Returns:
            Dictionary containing the refined result
        """
        result = self.handle(user_goal)
        
        for round_num in range(feedback_rounds):
            print(f"🔄 **Feedback Round {round_num + 1}:**")
            
            # Use reasoning agent to refine the execution plan
            refinement_prompt = f"""
            Original Goal: {user_goal}
            Current Decision: {result['decision']}
            Current Actions: {result['actions']}
            
            Review the above and suggest improvements or refinements to make the execution plan more effective.
            """
            
            refined_decision = self.reasoning.run(result['context'], refinement_prompt)
            refined_actions = self.execution.run(refined_decision)
            
            result['decision'] = refined_decision
            result['actions'] = refined_actions
            result['refinement_rounds'] = round_num + 1
        
        return result


def main():
    """Main function demonstrating the multi-agent coordinator."""
    print("🤖 **Multi-Agent Coordinator Demo**")
    print("=" * 50)
    
    # Ensure Foundry Local is running with a model
    print("📋 **Prerequisites:** Ensure 'foundry model run phi-4-mini' is running\n")
    
    # Create coordinator
    coord = Coordinator()
    
    # Example goals to demonstrate different capabilities
    example_goals = [
        "Create a plan to onboard 5 new customers this month",
        "Develop a strategy to improve team productivity by 20%",
        "Design a customer feedback collection system",
        "Plan a product launch for a new AI tool"
    ]
    
    # Process first example with detailed output
    goal = example_goals[0]
    print(f"🎯 **Processing Goal:** {goal}")
    print("-" * 50)
    
    try:
        result = coord.handle(goal)
        
        print("\n📊 **Final Result:**")
        print("=" * 50)
        print(f"**Goal:** {result['goal']}")
        print(f"\n**Context:** {result['context']}")
        print(f"\n**Decision:** {result['decision']}")
        print(f"\n**Actions:** {result['actions']}")
        
        # Try to parse actions as JSON if possible
        try:
            actions_json = json.loads(result['actions'])
            print(f"\n**Formatted Actions:**")
            print(json.dumps(actions_json, indent=2))
        except (json.JSONDecodeError, TypeError):
            pass
        
    except Exception as e:
        print(f"❌ **Error:** {e}")
        print("\nPlease ensure:")
        print("1. Foundry Local service is running")
        print("2. A model is loaded (e.g., 'foundry model run phi-4-mini')")
        print("3. The required dependencies are installed")


if __name__ == "__main__":
    main()

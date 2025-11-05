"""
Web Search Agent using OpenAI Agents SDK

This script demonstrates how to create an agent that takes a user query,
generates 2 optimized search queries with reasoning, and performs web searches.
"""

from agents import Agent, WebSearchTool, trace, Runner
import json


class WebSearchQueryOptimizer:
    """
    A class to optimize search queries by generating multiple variations
    with different search strategies.
    """

    def __init__(self):
        self.agent = Agent(
            name="Search Query Optimizer",
            instructions="""
            You are a search query optimization expert. When given a user query,
            your task is to:
            1. Analyze the user's intent and information needs
            2. Generate exactly 2 optimized search queries
            3. Provide clear reasoning for each query

            Your response should be in JSON format:
            {
                "queries": [
                    {
                        "query": "optimized search query 1",
                        "reason": "explanation for why this query is effective"
                    },
                    {
                        "query": "optimized search query 2",
                        "reason": "explanation for why this query is effective"
                    }
                ]
            }

            Strategy guidelines:
            - Query 1: Should be broad and comprehensive to capture general information
            - Query 2: Should be specific and targeted to find detailed/technical information
            - Use relevant keywords, synonyms, and search operators when helpful
            - Consider the user's likely intent (tutorial, documentation, news, research, etc.)
            """,
            tools=[],
        )

    def generate_queries(self, user_query: str) -> dict:
        """
        Generate 2 optimized search queries from the user's input.

        Args:
            user_query: The original user query

        Returns:
            Dictionary containing the optimized queries and reasoning
        """
        prompt = f"""
        User's original query: "{user_query}"

        Please generate 2 optimized search queries with reasoning.
        """

        result = Runner.run(self.agent, prompt)

        # Parse the agent's response to extract queries
        try:
            # Extract JSON from the response
            response_text = result.messages[-1].content

            # Try to parse as JSON
            if isinstance(response_text, str):
                # Find JSON in the response
                start_idx = response_text.find('{')
                end_idx = response_text.rfind('}') + 1
                if start_idx != -1 and end_idx > start_idx:
                    json_str = response_text[start_idx:end_idx]
                    return json.loads(json_str)

            return response_text
        except Exception as e:
            print(f"Error parsing response: {e}")
            return {"error": str(e), "raw_response": response_text}


class WebSearchAgent:
    """
    Main web search agent that coordinates query optimization and search execution.
    """

    def __init__(self):
        self.optimizer = WebSearchQueryOptimizer()
        self.search_agent = Agent(
            name="Web Search Agent",
            instructions="""
            You are a web search specialist. Use the web search tool to find
            relevant information and provide comprehensive summaries of the results.
            """,
            tools=[WebSearchTool()],
        )

    @trace
    def search(self, user_query: str):
        """
        Execute the complete web search workflow:
        1. Generate optimized queries
        2. Display queries with reasoning
        3. Execute searches
        4. Return results

        Args:
            user_query: The user's original search query
        """
        print(f"\n{'='*80}")
        print(f"ORIGINAL QUERY: {user_query}")
        print(f"{'='*80}\n")

        # Step 1: Generate optimized queries
        print("🔍 Generating optimized search queries...\n")
        optimized_data = self.optimizer.generate_queries(user_query)

        if "error" in optimized_data:
            print(f"Error: {optimized_data['error']}")
            return

        queries = optimized_data.get("queries", [])

        # Step 2: Display queries with reasoning
        print("📋 OPTIMIZED SEARCH QUERIES:\n")
        for i, query_info in enumerate(queries, 1):
            print(f"Query #{i}:")
            print(f"  Search: \"{query_info['query']}\"")
            print(f"  Reason: {query_info['reason']}\n")

        # Step 3: Execute searches
        print(f"\n{'='*80}")
        print("🌐 EXECUTING WEB SEARCHES")
        print(f"{'='*80}\n")

        results = []
        for i, query_info in enumerate(queries, 1):
            print(f"\n--- Search #{i}: {query_info['query']} ---\n")

            search_prompt = f"Search for: {query_info['query']}"
            result = Runner.run(self.search_agent, search_prompt)

            results.append({
                "query": query_info['query'],
                "reason": query_info['reason'],
                "result": result
            })

            # Display the search result
            if hasattr(result, 'messages') and result.messages:
                print(f"Results: {result.messages[-1].content}\n")

        return results


def main():
    """
    Main function to demonstrate the web search agent.
    """
    # Example usage
    agent = WebSearchAgent()

    # Example query - replace with actual user input
    example_query = "How to train machine learning models on limited data"

    print("""
╔══════════════════════════════════════════════════════════════════╗
║         OpenAI Web Search Agent - Query Optimizer              ║
╚══════════════════════════════════════════════════════════════════╝

This agent demonstrates:
1. Taking a user query
2. Generating 2 optimized search queries with reasoning
3. Executing web searches using OpenAI Agents SDK
    """)

    # Execute the search
    results = agent.search(example_query)

    print(f"\n{'='*80}")
    print("✅ SEARCH COMPLETE")
    print(f"{'='*80}")


if __name__ == "__main__":
    main()

"""
Example usage of the Web Search Agent

This script demonstrates different ways to use the web search agent
with various types of queries.
"""

from web_search_agent import WebSearchAgent
import os


def example_1_technical_query():
    """
    Example 1: Technical/Programming Query
    Shows how the agent handles technical searches
    """
    print("\n" + "="*80)
    print("EXAMPLE 1: Technical Query")
    print("="*80)

    agent = WebSearchAgent()
    query = "Python asyncio best practices for concurrent API calls"
    results = agent.search(query)

    return results


def example_2_research_query():
    """
    Example 2: Research Query
    Shows how the agent handles research-oriented searches
    """
    print("\n" + "="*80)
    print("EXAMPLE 2: Research Query")
    print("="*80)

    agent = WebSearchAgent()
    query = "Impact of climate change on coral reef ecosystems"
    results = agent.search(query)

    return results


def example_3_how_to_query():
    """
    Example 3: How-to Query
    Shows how the agent handles tutorial/guide searches
    """
    print("\n" + "="*80)
    print("EXAMPLE 3: How-to Query")
    print("="*80)

    agent = WebSearchAgent()
    query = "How to deploy a Docker container to AWS ECS"
    results = agent.search(query)

    return results


def custom_query():
    """
    Interactive example - takes user input
    """
    print("\n" + "="*80)
    print("CUSTOM QUERY")
    print("="*80)

    query = input("\nEnter your search query: ")
    agent = WebSearchAgent()
    results = agent.search(query)

    return results


def demonstrate_query_optimization():
    """
    Shows why the agent generates 2 different queries:

    Query 1 Strategy - Broad Search:
    - Captures general information and overview
    - Uses broader terms to ensure comprehensive coverage
    - Good for understanding the big picture
    - Example: "machine learning small datasets" (broad)

    Query 2 Strategy - Specific/Technical Search:
    - Targets specific techniques, solutions, or implementations
    - Uses technical terminology and specific keywords
    - Good for finding detailed solutions and best practices
    - Example: "few-shot learning techniques data augmentation" (specific)

    This dual-query approach ensures:
    - Complete coverage of the topic (broad + specific)
    - Different perspectives (general info + technical details)
    - Better chance of finding both introductory and advanced resources
    """
    print("""
╔══════════════════════════════════════════════════════════════════╗
║            Web Search Query Optimization Strategy               ║
╚══════════════════════════════════════════════════════════════════╝

WHY 2 QUERIES?
--------------

The agent generates 2 different search queries to maximize search effectiveness:

1️⃣  BROAD QUERY (Query 1)
   Purpose: Capture comprehensive, general information
   Strategy:
   - Uses broader, more common terminology
   - Targets overview articles, guides, and introductions
   - Good for understanding context and basics
   - Catches popular resources and mainstream information

   Example for "train models on limited data":
   → "machine learning small datasets techniques"

2️⃣  SPECIFIC/TECHNICAL QUERY (Query 2)
   Purpose: Find detailed, technical, or specialized information
   Strategy:
   - Uses specific technical terms and jargon
   - Targets in-depth articles, research papers, and documentation
   - Good for finding advanced solutions and best practices
   - Catches specialized resources and expert content

   Example for "train models on limited data":
   → "few-shot learning data augmentation transfer learning"

BENEFITS:
---------
✓ Comprehensive coverage (general + specific)
✓ Different result sets (broader range of sources)
✓ Multiple perspectives (beginner + expert level)
✓ Better recall (less likely to miss relevant info)
✓ Redundancy protection (if one query fails, other may succeed)

    """)


if __name__ == "__main__":
    import sys

    # Display the query optimization strategy
    demonstrate_query_optimization()

    print("\nSelect an example to run:")
    print("1. Technical/Programming Query")
    print("2. Research Query")
    print("3. How-to/Tutorial Query")
    print("4. Enter custom query")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        example_1_technical_query()
    elif choice == "2":
        example_2_research_query()
    elif choice == "3":
        example_3_how_to_query()
    elif choice == "4":
        custom_query()
    elif choice == "5":
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice. Please run again and select 1-5.")

# Web Search Agent with Query Optimization

An intelligent web search agent built using the OpenAI Agents SDK that optimizes search queries by generating 2 strategic variations with clear reasoning.

## Overview

This agent implements a dual-query search strategy that:
1. Takes a user's original search query
2. Generates 2 optimized search queries with different strategies
3. Provides clear reasoning for each query
4. Executes web searches using both queries
5. Returns comprehensive results

## Why 2 Queries?

The agent uses a **two-pronged search strategy** to maximize search effectiveness:

### Query 1: Broad & Comprehensive Search
**Purpose:** Capture general information and overview content

**Strategy:**
- Uses broader, more common terminology
- Targets overview articles, guides, and tutorials
- Good for understanding context and fundamentals
- Catches popular resources and mainstream information

**Example:**
- Original: "How to train machine learning models on limited data"
- Query 1: `"machine learning small datasets techniques"`
- Reason: "Broad search to capture general techniques and overview articles about working with limited data in machine learning"

### Query 2: Specific & Technical Search
**Purpose:** Find detailed, technical, or specialized information

**Strategy:**
- Uses specific technical terms and jargon
- Targets in-depth articles, research papers, and documentation
- Good for finding advanced solutions and best practices
- Catches specialized resources and expert content

**Example:**
- Original: "How to train machine learning models on limited data"
- Query 2: `"few-shot learning data augmentation transfer learning"`
- Reason: "Specific technical search targeting advanced techniques like few-shot learning, data augmentation, and transfer learning that are specifically used for limited data scenarios"

## Benefits of Dual-Query Approach

✅ **Comprehensive Coverage:** Combines general + specific information
✅ **Diverse Results:** Different query formulations yield different result sets
✅ **Multiple Perspectives:** Captures both beginner and expert-level content
✅ **Better Recall:** Less likely to miss relevant information
✅ **Redundancy Protection:** If one query underperforms, the other may succeed

## Installation

```bash
# Install required dependencies
pip install -r requirements.txt

# Set up your OpenAI API key
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

### Basic Usage

```python
from web_search_agent import WebSearchAgent

# Create an agent instance
agent = WebSearchAgent()

# Execute a search
results = agent.search("Your search query here")
```

### Running Examples

```bash
# Run the main agent with default example
python web_search_agent.py

# Run interactive examples
python example_usage.py
```

## Code Structure

### `web_search_agent.py`

Main implementation with two key classes:

#### `WebSearchQueryOptimizer`
- Analyzes user intent and information needs
- Generates 2 optimized search queries
- Provides reasoning for each query
- Uses strategic guidelines for query formulation

#### `WebSearchAgent`
- Coordinates the entire search workflow
- Manages query optimization and search execution
- Uses `WebSearchTool` from OpenAI Agents SDK
- Returns structured results

### `example_usage.py`

Demonstration script with:
- Multiple example scenarios (technical, research, how-to queries)
- Interactive custom query mode
- Detailed explanation of the optimization strategy

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│  User Query: "How to train ML models on limited data"      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│           WebSearchQueryOptimizer                           │
│  • Analyzes intent                                          │
│  • Generates 2 queries                                      │
│  • Provides reasoning                                       │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────┬──────────────────────────────────┐
│     Query 1 (Broad)      │    Query 2 (Specific)            │
├──────────────────────────┼──────────────────────────────────┤
│ "machine learning small  │ "few-shot learning data          │
│  datasets techniques"    │  augmentation transfer learning" │
│                          │                                  │
│ Reason: Captures general │ Reason: Targets specific         │
│ techniques and overview  │ technical methods for limited    │
│ articles                 │ data scenarios                   │
└──────────────────────────┴──────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              WebSearchAgent                                 │
│  • Executes both searches using WebSearchTool               │
│  • Collects and structures results                          │
│  • Returns comprehensive findings                           │
└─────────────────────────────────────────────────────────────┘
```

## OpenAI Agents SDK Components Used

- **`Agent`**: Core agent class for creating specialized agents
- **`WebSearchTool`**: Tool for executing web searches
- **`Runner`**: Executes agent tasks and manages workflow
- **`trace`**: Decorator for tracing agent execution (useful for debugging)

## Example Output

```
================================================================================
ORIGINAL QUERY: How to train machine learning models on limited data
================================================================================

🔍 Generating optimized search queries...

📋 OPTIMIZED SEARCH QUERIES:

Query #1:
  Search: "machine learning small datasets techniques"
  Reason: Broad search to capture general techniques and overview articles about
          working with limited data in machine learning

Query #2:
  Search: "few-shot learning data augmentation transfer learning"
  Reason: Specific technical search targeting advanced techniques like few-shot
          learning, data augmentation, and transfer learning that are specifically
          used for limited data scenarios

================================================================================
🌐 EXECUTING WEB SEARCHES
================================================================================

--- Search #1: machine learning small datasets techniques ---
[Search results displayed here...]

--- Search #2: few-shot learning data augmentation transfer learning ---
[Search results displayed here...]

================================================================================
✅ SEARCH COMPLETE
================================================================================
```

## Customization

You can customize the query generation strategy by modifying the instructions in the `WebSearchQueryOptimizer` class:

```python
self.agent = Agent(
    name="Search Query Optimizer",
    instructions="""
    [Modify these instructions to change query generation strategy]
    """,
    tools=[],
)
```

## Key Features

1. **Intelligent Query Optimization:** Automatically transforms user queries into effective search queries
2. **Dual-Strategy Approach:** Combines broad and specific searches for comprehensive results
3. **Transparent Reasoning:** Explains why each query was generated
4. **Built with OpenAI Agents SDK:** Leverages powerful agent framework
5. **Extensible Design:** Easy to customize and extend

## Use Cases

- **Research:** Gather both overview and detailed information on topics
- **Technical Searches:** Find both introductory and advanced technical content
- **Problem Solving:** Discover multiple approaches to solving problems
- **Learning:** Access both beginner-friendly and expert-level resources

## Requirements

- Python 3.8+
- OpenAI API key
- `openai-agents` package

## License

This code is part of the DrivenData competition-winners repository. See LICENSE file for details.

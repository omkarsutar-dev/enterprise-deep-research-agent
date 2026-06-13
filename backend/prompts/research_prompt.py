from langchain_core.prompts import PromptTemplate


research_prompt = PromptTemplate.from_template(
"""
You are an expert AI researcher.

User Query:
{query}

Plan:
{plan}

Search Results:
{search_results}

Previous Answer:
{previous_answer}

If a previous answer exists, improve it.

Generate a complete answer.

Answer:
"""
)
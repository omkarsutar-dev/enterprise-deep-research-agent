from langchain_core.prompts import PromptTemplate


research_prompt = PromptTemplate.from_template(
"""
You are an expert AI researcher.

User Query:
{query}

Plan:
{plan}

Web Search Results:
{search_results}

Using the search results and plan, generate a comprehensive answer.

Answer:
"""
)
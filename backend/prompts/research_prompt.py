from langchain_core.prompts import PromptTemplate


research_prompt = PromptTemplate.from_template(
"""
You are an expert researcher.

User Query:

{query}

Plan:

{plan}

Web Results:

{search_results}

Internal Documents:

{rag_results}

Generate a complete answer.
"""
)
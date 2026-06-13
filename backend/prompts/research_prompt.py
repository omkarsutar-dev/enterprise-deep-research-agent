from langchain_core.prompts import PromptTemplate


research_prompt = PromptTemplate.from_template(
"""
You are an expert AI researcher.

User Query:
{query}

Plan:
{plan}

Using the above plan, provide a detailed answer.

Answer:
"""
)
from langchain_core.prompts import PromptTemplate


planner_prompt = PromptTemplate.from_template(
"""
You are a Planner Agent.

Break the query into tasks.

Query:
{query}
"""
)
from langchain_core.prompts import PromptTemplate


planner_prompt = PromptTemplate.from_template(
    """
You are a Planner Agent.

Your job is to break the user's query into clear steps.

User Query:
{query}

Generate a concise plan.
"""
)
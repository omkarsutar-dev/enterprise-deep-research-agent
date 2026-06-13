from langchain_core.prompts import PromptTemplate


planner_prompt = PromptTemplate.from_template(
"""
You are a Planner Agent.

Long-Term Memory:

{long_term_memory}

Session History:

{chat_history}

Current Query:

{query}

Break the query into tasks.
"""
)
from langchain_core.prompts import PromptTemplate


planner_prompt = PromptTemplate.from_template(
"""
You are a Planner Agent.

Previous Conversation:

{chat_history}

Current Query:

{query}

Break the task into steps.
"""
)
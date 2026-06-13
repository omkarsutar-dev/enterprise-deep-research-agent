from langchain_core.prompts import PromptTemplate


critic_prompt = PromptTemplate.from_template(
"""
Evaluate the answer.

Query:
{query}

Answer:
{answer}

Provide:

- strengths
- weaknesses
- suggestions
- score (0-10)
"""
)
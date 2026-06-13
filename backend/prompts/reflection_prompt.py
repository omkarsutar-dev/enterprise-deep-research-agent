from langchain_core.prompts import PromptTemplate


reflection_prompt = PromptTemplate.from_template(
"""
You are a Reflection Agent.

User Query:
{query}

Original Answer:
{answer}

Critique:
{critique}

Improve the answer by:

- Addressing weaknesses
- Filling missing information
- Enhancing clarity
- Producing a more complete answer

Improved Answer:
"""
)
from langchain_core.prompts import PromptTemplate


critic_prompt = PromptTemplate.from_template(
"""
You are a Critic Agent.

Evaluate the answer below.

User Query:
{query}

Answer:
{answer}

Check:

1. Accuracy
2. Completeness
3. Missing details
4. Hallucinations

Provide:

- Strengths
- Weaknesses
- Suggestions
- Overall Score out of 10

Critique:
"""
)
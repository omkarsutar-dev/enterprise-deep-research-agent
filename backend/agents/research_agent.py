from backend.prompts.research_prompt import research_prompt
from backend.llms.openai_llm import llm


def research_agent(state):

    query = state["query"]
    plan = state["plan"]

    chain = research_prompt | llm

    response = chain.invoke(
        {
            "query": query,
            "plan": plan
        }
    )

    return {
        "answer": response.content
    }
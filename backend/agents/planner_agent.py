from backend.prompts.planner_prompt import planner_prompt
from backend.llms.openai_llm import llm


def planner_agent(state):

    query = state["query"]

    chain = planner_prompt | llm

    response = chain.invoke(
        {
            "query": query
        }
    )

    return {
        "plan": response.content
    }
from backend.prompts.planner_prompt import planner_prompt
from backend.llms.openai_llm import llm
from backend.models.planner_model import PlannerOutput


structured_llm = llm.with_structured_output(
    PlannerOutput
)


def planner_agent(state):

    query = state["query"]

    chain = planner_prompt | structured_llm

    response = chain.invoke(
        {
            "query": query
        }
    )

    return {
        "plan": response.tasks
    }
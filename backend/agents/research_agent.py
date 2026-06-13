from backend.prompts.research_prompt import research_prompt
from backend.llms.openai_llm import llm
from backend.tools.tavily_tool import tavily_search


def research_agent(state):

    query = state["query"]

    plan = state["plan"]

    previous_answer = state.get(
        "improved_answer",
        ""
    )

    search_results = tavily_search(
        query
    )

    chain = research_prompt | llm

    response = chain.invoke(
        {
            "query": query,
            "plan": plan,
            "search_results": search_results,
            "previous_answer": previous_answer
        }
    )

    return {
        "search_results": search_results,
        "answer": response.content
    }
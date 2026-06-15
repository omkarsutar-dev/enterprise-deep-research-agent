from backend.tools.tavily_tool import tavily_search
from backend.tools.rag_tool import rag_search
from backend.prompts.research_prompt import research_prompt
from backend.llms.openai_llm import llm


def research_agent(state):

    query = state["query"]

    web_results = tavily_search(
        query
    )

    rag_results = rag_search(
        query
    )

    chain = research_prompt | llm

    response = chain.invoke(

        {

            "query": query,

            "plan": state["plan"],

            "search_results": web_results,

            "rag_results": rag_results

        }

    )

    return {

        "search_results": web_results,

        "rag_results": rag_results,

        "answer": response.content

    }
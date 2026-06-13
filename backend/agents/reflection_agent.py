from backend.prompts.reflection_prompt import reflection_prompt
from backend.llms.openai_llm import llm


def reflection_agent(state):

    query = state["query"]

    answer = state["answer"]

    critique = state["critique"]

    chain = reflection_prompt | llm

    response = chain.invoke(
        {
            "query": query,
            "answer": answer,
            "critique": critique
        }
    )

    return {
        "improved_answer": response.content
    }
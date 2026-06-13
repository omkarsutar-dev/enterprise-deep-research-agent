from backend.prompts.reflection_prompt import reflection_prompt
from backend.llms.openai_llm import llm


def reflection_agent(state):

    chain = reflection_prompt | llm

    response = chain.invoke(
        {
            "query": state["query"],
            "answer": state["answer"],
            "critique": state["critique"]
        }
    )

    return {
        "improved_answer": response.content,
        "retry_count": state["retry_count"] + 1
    }
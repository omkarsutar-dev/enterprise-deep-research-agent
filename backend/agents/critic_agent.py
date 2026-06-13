from backend.prompts.critic_prompt import critic_prompt
from backend.llms.openai_llm import llm


def critic_agent(state):

    query = state["query"]

    answer = state["answer"]

    chain = critic_prompt | llm

    response = chain.invoke(
        {
            "query": query,
            "answer": answer
        }
    )

    return {
        "critique": response.content
    }
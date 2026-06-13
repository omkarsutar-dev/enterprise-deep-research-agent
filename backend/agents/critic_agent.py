from backend.prompts.critic_prompt import critic_prompt
from backend.llms.openai_llm import llm
from backend.models.critic_model import CriticOutput


structured_llm = llm.with_structured_output(
    CriticOutput
)


def critic_agent(state):

    chain = critic_prompt | structured_llm

    response = chain.invoke(
        {
            "query": state["query"],
            "answer": state["answer"]
        }
    )

    return {
        "critique": response
    }
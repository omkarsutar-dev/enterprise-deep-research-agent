from backend.models.critic_model import CriticOutput


def critic_router(state):

    critique: CriticOutput = state["critique"]

    score = critique.score

    print(f"Critic Score: {score}")

    if score < 8:
        return "reflection"

    return "end"
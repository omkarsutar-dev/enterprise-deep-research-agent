from typing import TypedDict

from backend.models.critic_model import CriticOutput


class GraphState(TypedDict):

    query: str

    plan: list

    search_results: list

    answer: str

    critique: CriticOutput

    improved_answer: str

    retry_count: int
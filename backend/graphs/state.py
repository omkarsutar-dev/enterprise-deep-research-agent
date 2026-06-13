from typing import TypedDict
from backend.models.critic_model import CriticOutput


class GraphState(TypedDict):

    session_id: str

    query: str

    chat_history: list

    plan: list

    search_results: list

    answer: str

    critique: CriticOutput

    improved_answer: str

    retry_count: int
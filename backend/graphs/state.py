from typing import TypedDict
from backend.models.critic_model import CriticOutput


class GraphState(TypedDict):

    session_id: str

    query: str

    chat_history: list

    long_term_memory: dict

    plan: list

    search_results: list

    rag_results: list

    answer: str

    critique: CriticOutput

    improved_answer: str

    retry_count: int
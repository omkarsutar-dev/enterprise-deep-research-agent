from typing import TypedDict


class GraphState(TypedDict):
    query: str
    plan: str
    answer: str
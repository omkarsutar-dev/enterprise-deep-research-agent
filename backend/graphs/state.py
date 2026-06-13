from typing import TypedDict


class GraphState(TypedDict):

    query: str

    plan: str

    search_results: list

    answer: str
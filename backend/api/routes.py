from fastapi import APIRouter

from backend.graphs.graph_builder import graph

router = APIRouter()


@router.post("/chat")
def chat(query: str):

    result = graph.invoke(
        {
            "query": query
        }
    )

    return result
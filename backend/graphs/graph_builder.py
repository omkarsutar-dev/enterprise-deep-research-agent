from langgraph.graph import StateGraph, END

from backend.graphs.state import GraphState
from backend.agents.planner_agent import planner_agent
from backend.agents.research_agent import research_agent


builder = StateGraph(GraphState)

builder.add_node(
    "planner",
    planner_agent
)

builder.add_node(
    "research",
    research_agent
)

builder.set_entry_point(
    "planner"
)

builder.add_edge(
    "planner",
    "research"
)

builder.add_edge(
    "research",
    END
)

graph = builder.compile()
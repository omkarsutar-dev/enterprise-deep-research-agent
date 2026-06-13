from langgraph.graph import StateGraph, END

from backend.graphs.state import GraphState

from backend.graphs.router import critic_router

from backend.agents.planner_agent import planner_agent
from backend.agents.research_agent import research_agent
from backend.agents.critic_agent import critic_agent
from backend.agents.reflection_agent import reflection_agent


builder = StateGraph(GraphState)

builder.add_node(
    "planner",
    planner_agent
)

builder.add_node(
    "research",
    research_agent
)

builder.add_node(
    "critic",
    critic_agent
)

builder.add_node(
    "reflection",
    reflection_agent
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
    "critic"
)

builder.add_conditional_edges(
    "critic",
    critic_router,
    {
        "reflection": "reflection",
        "end": END
    }
)

builder.add_edge(
    "reflection",
    "research"
)

graph = builder.compile()
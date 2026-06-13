from langgraph.graph import StateGraph, END

from backend.graphs.state import GraphState

from backend.graphs.router import critic_router

from backend.agents.planner_agent import planner_agent
from backend.agents.research_agent import research_agent
from backend.agents.critic_agent import critic_agent
from backend.agents.reflection_agent import reflection_agent
from backend.agents.memory_agent import memory_agent
from backend.agents.update_memory_agent import update_memory_agent


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

builder.add_node(
    "memory",
    memory_agent
)

builder.add_node(
    "update_memory",
    update_memory_agent
)

builder.set_entry_point(
    "memory"
)

# builder.set_entry_point(
#     "planner"
# )

builder.add_edge(
    "memory",
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
        "end": "update_memory"
    }
)

builder.add_edge(
    "reflection",
    "research"
)

builder.add_edge(
    "update_memory",
    END
)

graph = builder.compile()
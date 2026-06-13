def planner_agent(state):

    query = state["query"]

    plan = (
    "1. Understand the query.\n"
    "2. Gather information.\n"
    "3. Produce final response.\n\n"
    f"User Query:\n{query}")

    return {
        "plan": plan
    }
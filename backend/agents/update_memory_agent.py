from backend.memory.session_memory import conversation_store


def update_memory_agent(state):

    session_id = state["session_id"]

    history = conversation_store.get(
        session_id,
        []
    )

    history.append(
        {
            "query": state["query"],
            "answer": state["answer"]
        }
    )

    conversation_store[session_id] = history

    return {}
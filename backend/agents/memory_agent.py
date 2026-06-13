from backend.memory.session_memory import conversation_store


def memory_agent(state):

    session_id = state["session_id"]

    history = conversation_store.get(
        session_id,
        []
    )

    return {
        "chat_history": history
    }
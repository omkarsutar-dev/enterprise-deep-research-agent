from backend.memory.session_memory import conversation_store

from backend.memory.long_term_memory import load_memory


def memory_agent(state):

    session_id = state["session_id"]

    history = conversation_store.get(
        session_id,
        []
    )

    memory_db = load_memory()

    profile = memory_db.get(
        session_id,
        {}
    )

    return {

        "chat_history": history,

        "long_term_memory": profile
    }
from backend.memory.long_term_memory import (
    load_memory,
    save_memory
)


def update_long_term_memory_agent(state):

    session_id = state["session_id"]

    memory_db = load_memory()

    memory_db[session_id] = {

        "last_query": state["query"],

        "last_answer": state["answer"],

        "topics_of_interest": [
            state["query"]
        ]
    }

    save_memory(
        memory_db
    )

    return {}
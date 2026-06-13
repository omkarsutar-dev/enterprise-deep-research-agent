MAX_RETRIES = 2


def critic_router(state):

    score = state["critique"].score

    retry_count = state["retry_count"]

    print(
        f"Score={score}, Retry={retry_count}"
    )

    if score >= 8:
        return "end"

    if retry_count >= MAX_RETRIES:
        return "end"

    return "reflection"
from backend.rag.retriever import retriever


def rag_search(query):

    docs = retriever.invoke(
        query
    )

    return [
        doc.page_content
        for doc in docs
    ]
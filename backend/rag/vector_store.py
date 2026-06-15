from langchain_openai import OpenAIEmbeddings

from langchain_chroma import Chroma


embeddings = OpenAIEmbeddings()


vector_store = Chroma(

    persist_directory="backend/vector_store",

    embedding_function=embeddings

)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()


loader = PyPDFLoader(
    "backend/documents/rag.pdf"
)

documents = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(
    documents
)


embeddings = OpenAIEmbeddings()


vector_store = Chroma.from_documents(

    documents=chunks,

    embedding=embeddings,

    persist_directory="backend/vector_store"

)

print(
    "Vector DB created."
)
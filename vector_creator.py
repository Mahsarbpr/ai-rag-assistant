from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from config import EMBEDDING_MODEL

# Vector Creator: Create vectorstore from document chunks for similarity search later on in the RAG process
def create_vectorstore(chunks: list[Document]) -> FAISS:

    embeddings = HuggingFaceEmbeddings(
        model_name= EMBEDDING_MODEL
    )

    return FAISS.from_documents(chunks, embeddings)
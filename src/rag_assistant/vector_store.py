from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from rag_assistant.config import EMBEDDING_MODEL

# Vector Creator: Create vectorstore from document chunks for similarity search later on in the RAG process
def create_vectorstore(chunks: list[Document]) -> FAISS:

    embeddings = HuggingFaceEmbeddings(
        model_name= EMBEDDING_MODEL
    )

    return FAISS.from_documents(chunks, embeddings)

# Save the created vectorstore to disk   and load it back when needed. This allows us to avoid reprocessing documents 
# and creating the vectorstore from scratch every time we run the application, improving efficiency.
def save_vectorstore(vectorstore: FAISS, path: str) -> None:
    vectorstore.save_local(path)

# Load the vectorstore from disk if it exists and can be loaded (i.e. data has not changed since last index creation)
def load_vectorstore(path: str) -> FAISS:
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True,
    )
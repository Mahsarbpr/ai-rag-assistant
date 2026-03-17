from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM


def main() -> None:
    # 1. Sample document text
    text = """
    Azure Maia is Microsoft's in-house AI accelerator designed for frontier AI workloads.
    It focuses on performance, scalability, and cost efficiency for large-scale AI systems.
    Technical Program Managers on Azure Maia work across software and hardware teams to
    coordinate integration, remove blockers, and drive launch readiness.
    """

    # 2. Wrap text as a document
    documents = [Document(page_content=text)]

    # 3. Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    # 4. Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 5. Store chunks in FAISS
    vector_store = FAISS.from_documents(chunks, embeddings)

    # 6. Ask a question
    query = "What is Azure Maia designed for?"

    # 7. Retrieve relevant chunks
    retrieved_docs = vector_store.similarity_search(query, k=2)
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)

    # 8. Load local model via Ollama
    llm = OllamaLLM(model="phi3")

    # 9. Build prompt
    prompt = f"""
You are answering questions using only the provided context.

Context:
{context}

Question:
{query}

Answer in 2-4 sentences. If the answer is not in the context, say "I don't know based on the provided context."
"""

    # 10. Generate answer
    answer = llm.invoke(prompt)

    print("\n" + "=" * 80)
    print("QUESTION:")
    print(query)

    print("\n" + "=" * 80)
    print("RETRIEVED CONTEXT:")
    print(context)

    print("\n" + "=" * 80)
    print("LLM ANSWER:")
    print(answer)
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
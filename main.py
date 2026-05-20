from src.rag_assistant.rag_pipeline import RAGPipeline
from src.rag_assistant.display import print_answer_and_sources

def main() -> None:

    rag = RAGPipeline()
    rag.load_or_build_vectorstore()
    question_1 = input("Enter your question: ")
    result = rag.ask_question(question_1)
    print_answer_and_sources(result)
    

if __name__ == "__main__":
    main()
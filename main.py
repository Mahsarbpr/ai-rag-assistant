from rag_pipeline import RAGPipeline
from display import print_answer_and_sources

def main() -> None:

    rag = RAGPipeline()
    rag.load_and_process_documents()
    question_1 = input("Enter your question: ")
    result = rag.ask_question(question_1)
    print_answer_and_sources(result)
    

if __name__ == "__main__":
    main()
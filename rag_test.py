
from load_text_pdf_documents import load_documents
from text_splitter import split_documents
from vector_creator import create_vectorstore
from rag_service import find_answer_to_question
from config import DATA_FOLDER

def main() -> None:
    # 1. Load documents from data folder
    documents = load_documents(DATA_FOLDER)
    # 2. Split documents into chunks
    chunks = split_documents(documents)
    
    # 3. Create vectorstore from chunks
    vectorstore = create_vectorstore(chunks)

    # 4. Ask a question
    question = input("Enter your question: ")
    
    # 5. Get answer and sources
    result = find_answer_to_question(vectorstore, question)

    print("\n--- Answer ---")
    print(result["answer"])

    print("\n--- Sources ---")
    for source in result["sources"]:
        print(source)
    
    


    

    
    

if __name__ == "__main__":
    main()

from load_text_pdf_documents import load_documents
from text_splitter import split_documents
from vector_creator import create_vectorstore
from rag_service import find_answer_to_question
from config import DATA_FOLDER, LLM_MODEL
from langchain_ollama import OllamaLLM

class RAGPipeline:
    def __init__(self, data_folder: str = DATA_FOLDER, model_name: str = LLM_MODEL):
        self.data_folder = data_folder
        self.documents = []
        self.chunks = []
        self.vectorstore = None
        self.model_name = model_name
        self.llm = OllamaLLM(model = self.model_name)

    def load_and_process_documents(self) -> None:
        self.documents = load_documents(self.data_folder)
        self.chunks = split_documents(self.documents)
        self.vectorstore = create_vectorstore(self.chunks)

    def ask_question(self, question: str) -> dict:
        if not self.vectorstore:
            raise ValueError("Vectorstore not created. Please load and process documents first.")
        
        return find_answer_to_question(self.vectorstore, self.llm, question)

            
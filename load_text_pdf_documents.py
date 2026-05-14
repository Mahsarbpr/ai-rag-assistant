from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document

def load_txt_file(file_path: Path) -> Document:
    """Load a .txt file and return it as a LangChain Document."""
    text = file_path.read_text(encoding="utf-8")
    return Document(
        page_content=text,
        metadata={"source": str(file_path), "file_name": file_path.name, "type": "txt"},
    )


def load_pdf_file(file_path: Path) -> list[Document]:
    """Load a PDF file and return one Document per page."""
    reader = PdfReader(str(file_path))
    documents = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text and text.strip():
            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": str(file_path),
                        "file_name": file_path.name,
                        "type": "pdf",
                        "page": page_number,
                    },
                )
            )

    return documents


def load_documents(data_folder: str = "data") -> list[Document]:
    """Load all supported documents from the data folder."""
    folder = Path(data_folder)

    if not folder.exists():
        raise FileNotFoundError(f"Data folder '{data_folder}' does not exist.")

    all_documents = []

    for file_path in folder.iterdir():
        if file_path.suffix.lower() == ".txt":
            all_documents.append(load_txt_file(file_path))
        elif file_path.suffix.lower() == ".pdf":
            all_documents.extend(load_pdf_file(file_path))

    return all_documents
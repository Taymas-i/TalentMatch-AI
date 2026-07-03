import pdfplumber
from docx import Document
from pathlib import Path
from app.core.exceptions import FileParsingError

def extract_text_from_pdf(file_path: str) -> str:
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        if not text.strip():
            raise FileParsingError(
                "No extractable text found. The PDF may be scanned/image-based."
            )
        return text.strip()

    except Exception as e:
        if isinstance(e, FileParsingError):
            raise
        raise FileParsingError(f"Failed to read PDF: {str(e)}")


def extract_text_from_docx(file_path: str) -> str:
    try:
        doc = Document(file_path)
        text = "\n".join(paragraph.text for paragraph in doc.paragraphs)

        if not text.strip():
            raise FileParsingError("The DOCX file appears to be empty.")
        return text.strip()

    except Exception as e:
        if isinstance(e, FileParsingError):
            raise
        raise FileParsingError(f"Failed to read DOCX: {str(e)}")


def extract_text(file_path: str) -> str:
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)
    elif extension == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise FileParsingError(f"Unsupported file type: {extension}")
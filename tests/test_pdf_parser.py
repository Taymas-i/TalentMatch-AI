import pytest
from app.services.pdf_parser import extract_text
from app.core.exceptions import FileParsingError


def test_extract_text_from_real_pdf():
    """Happy path: a real, valid PDF should return non-empty text."""
    result = extract_text("test_files/CV.pdf")
    assert isinstance(result, str)
    assert len(result.strip()) > 0


def test_unsupported_file_extension_raises_error():
    """Files with unsupported extensions should raise FileParsingError."""
    with pytest.raises(FileParsingError):
        extract_text("test_files/some_file.txt")


def test_nonexistent_file_raises_error():
    """A missing file path should raise FileParsingError, not crash silently."""
    with pytest.raises(FileParsingError):
        extract_text("test_files/does_not_exist.pdf")
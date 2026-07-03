
from app.services.pdf_parser import extract_text

result = extract_text("test_files/CV.pdf")
print(result)
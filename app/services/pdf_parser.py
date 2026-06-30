"""
[ADIM 5.1]

Yüklenen PDF/DOCX'i düz metne çevirir (pdfplumber / python-docx).

Edge case'leri unutma: şifreli PDF, taranmış (OCR gerektiren) PDF,
boş dosya - bunları exceptions.py'deki InvalidPDFError ile yönet.
"""

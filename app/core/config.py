"""
[ADIM 2.1]

BaseSettings (pydantic-settings) ile .env dosyasını oku.

Örnek alanlar:
- GROQ_API_KEY: str
- DATABASE_URL: str
- DAILY_REQUEST_LIMIT: int = 10  (SaaS değil ama "concurrency-safe" gösterimi için tutuyoruz)

NOT: .env dosyasını ASLA git'e ekleme, .gitignore'a ekli olduğundan emin ol.
"""

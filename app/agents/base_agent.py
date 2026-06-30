"""
[ADIM 4.1 - EN KRİTİK TEMEL DOSYA]

Tüm ajanların miras alacağı temel sınıf.

İçereceği şeyler:
- Groq client bağlantısı (api key config'den okunur)
- retry mekanizması (örn. tenacity kütüphanesi ile, 3 deneme)
- timeout ayarı
- ortak bir `_call_llm(prompt, response_model)` metodu
  (Instructor kullanarak structured output alır)

ÖNCE BUNU SAĞLAM KUR: Extractor/Analyzer/Tailor bunun üzerine oturacak.
İlk olarak izole bir scriptte (bu dosyanın dışında) Groq + Instructor'ı
deneyip nasıl çalıştığını gör, sonra buraya class olarak taşı.
"""

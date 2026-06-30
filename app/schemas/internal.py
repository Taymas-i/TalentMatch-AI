"""
[ADIM 1.1 - İLK YAZILACAK DOSYA]

Bu dosya, üç ajanın (Extractor, Analyzer, Tailor) birbirine ne ileteceğini
tanımlar. Projeye buradan başla çünkü her şey buna bağımlı.

İçereceği örnek sınıflar:
- ExtractedCV(BaseModel): isim, deneyimler (liste), skiller (liste), egitim
- MatchAnalysis(BaseModel): skor (0-100), eslesen_skiller, eksik_skiller, gerekce (CoT çıktısı)
- TailoredExperience(BaseModel): orijinal_metin, yeniden_yazilmis_metin (STAR formatında)

Neden önemli: Instructor/Pydantic ile LLM'den bu şemalara UYUMLU JSON
zorunlu kılacaksın. Önce şemayı tasarlamak, "LLM'den ne istediğini"
netleştirmeni sağlar.
"""

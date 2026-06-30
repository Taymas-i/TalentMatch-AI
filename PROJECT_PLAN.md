# TalentMatch AI V2 — 3 Haftalık Uygulama Planı

Kural: Her yeni kütüphane/kavram için önce izole, küçük bir denemeyle
(tek dosya, projeye bağlamadan) mantığını anla. Sonra projeye entegre et.
AI'dan kod ÜRETTİRME — açıklat, sen yaz, takıldığında review iste.

Her klasörü doldurduğunda küçük bir commit at.

---

## 1. Hafta — Temel + Veri Katmanı

- [ ] Gün 1: Docker Compose ile PostgreSQL'i ayağa kaldır (`docker-compose up -d db`)
- [ ] Gün 1: `requirements.txt` kur, conda env'e (`ai_project`) yükle
- [ ] Gün 2: `schemas/internal.py` — ExtractedCV, MatchAnalysis, TailoredExperience
- [ ] Gün 2: `schemas/requests.py`, `schemas/responses.py`
- [ ] Gün 3: İzole bir scriptte Groq + Instructor dene (structured output POC)
- [ ] Gün 3: `core/config.py` — BaseSettings, .env okuma
- [ ] Gün 4: `models/user.py`, `user_limit.py`, `user_history.py`
- [ ] Gün 4: Alembic init et, ilk migration'ı oluştur ve çalıştır
- [ ] Gün 5: Şemada küçük bir değişiklik yap, ikinci migration'ı dene (migration döngüsünü öğren)
- [ ] Gün 5: `core/exceptions.py` — özel hata sınıfları
- [ ] Hafta sonu hedefi: DB ayakta, tablolar var, migration'lar çalışıyor, schemas net.

## 2. Hafta — Ajanlar

- [ ] Gün 1-2: `agents/base_agent.py` — LLM bağlantısı, retry (tenacity), timeout
- [ ] Gün 2-3: `agents/extractor.py` + `prompt_templates/extractor_prompts.py`
      → önce Groq playground'da prompt'u manuel dene
- [ ] Gün 3-4: `agents/analyzer.py` + `prompt_templates/analyzer_prompts.py`
      → CoT skorlama, aynı çifti 3-5 kez çalıştırıp tutarlılığı gözlemle
- [ ] Gün 4-5: `agents/tailor.py` + `prompt_templates/tailor_prompts.py`
      → Few-shot örnekler, "uydurma yapmama" guardrail'i özellikle test et
- [ ] Hafta sonu hedefi: Üç ajan izole (orchestrator olmadan) tek tek çalışıyor.

## 3. Hafta — Servisler, Orkestrasyon, API, Test, Docker

- [ ] Gün 1: `services/pdf_parser.py` — edge case'ler (şifreli, taranmış, boş PDF)
- [ ] Gün 1: `services/rate_limit.py` — SELECT FOR UPDATE, önce concurrency'i izole script ile simüle et
- [ ] Gün 2: `core/orchestrator.py` — üç ajanı bağla, SSE event'leri yield et
- [ ] Gün 2-3: `api/dependencies.py`, `api/endpoints/analysis.py` — SSE endpoint
      → önce basit bir "saniye sayan" SSE örneğiyle mekanizmayı anla
- [ ] Gün 3: `app/main.py` — her şeyi birbirine bağla
- [ ] Gün 4: `tests/` — mock LLM ile agent testleri, concurrency testi, PDF testleri
- [ ] Gün 4-5: Dockerfile (multi-stage build), docker-compose.yml tamamla
- [ ] Gün 5: `ui/app.py` — Streamlit, uçtan uca demo akışı
- [ ] Hafta sonu hedefi: CV yükle → ilan yapıştır → stream halinde skor + tailored CV gör.

---

## Notlar / Hatırlatmalar

- SaaS kredi/freemium mantığını tamamen çıkarmak istersen `user_limit.py`'yi
  basitleştir ama `rate_limit.py`'deki concurrency-safe mantığı bir
  teknik gösterim olarak sakla.
- README'ye "neden scraping'den vazgeçtim, manuel input'a geçtim" kısa bir
  not eklemek mühendislik karar verme sürecini gösterir, bunu sil-me.
- Tailor agent'ın guardrail testi portföyde özellikle bahsedilmeye değer.

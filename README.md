# TalentMatch AI (V2)

> Yüzlerce başvuru, sıfır dönüş devri bitti. Her ilana özel, otonom
> optimize edilmiş CV analiz ve yeniden yazım sistemi.

## Mimari

3 ajanlı (Extractor → Analyzer → Tailor) bir pipeline, FastAPI + SSE
streaming üzerinden çalışır. Detaylar için PROJECT_PLAN.md dosyasına bakın.

## Kurulum

```bash
cp .env.example .env  # GROQ_API_KEY'i doldur
docker-compose up -d db
pip install -r requirements.txt --break-system-packages
alembic upgrade head
uvicorn app.main:app --reload
```

## Geliştirme Sırası

Bkz. PROJECT_PLAN.md - her dosyanın içinde [ADIM X] notuyla yazılış sırası belirtildi.

# TalentMatch AI V2

Multi-agent AI system that analyzes a candidate's CV against a job description,
scores the match, and rewrites relevant experience using the STAR method —
tailored to the target role.

Built as a portfolio project to demonstrate production-oriented AI engineering
practices: structured LLM outputs, anti-hallucination guardrails, concurrency-safe
backend design, and full test coverage.

## Architecture

Three-agent pipeline orchestrated behind a FastAPI SSE endpoint:

- **Extractor** parses raw CV text into structured data (Pydantic + Instructor),
  distinguishing formal work experience from personal/academic projects.
- **Analyzer** compares the CV against the job description using chain-of-thought
  prompting, producing a 0–100 match score with matched/missing skills and reasoning.
- **Tailor** rewrites each experience and project description to align with the
  job description — with explicit guardrails against introducing skills or
  metrics not present in the original text.

Results stream to the client in real time via Server-Sent Events.

## Tech Stack

- **Backend:** FastAPI, Python
- **AI/LLM:** Groq API (`openai/gpt-oss-120b`), Instructor for structured outputs
- **Database:** PostgreSQL, SQLAlchemy, Alembic migrations
- **Frontend:** Streamlit
- **Infra:** Docker, Docker Compose (multi-stage build)
- **Testing:** pytest

## Engineering Highlights

- **Concurrency-safe rate limiting** — daily request limits enforced with
  `SELECT FOR UPDATE` and a unique constraint, verified with a threading-based
  test simulating 15 simultaneous requests.
- **Anti-hallucination guardrails** — the Tailor agent is tested to confirm it
  never introduces technologies or metrics absent from the original CV.
- **Score consistency validation** — the Analyzer is tested across repeated runs
  to confirm scoring stability.
- **Project-aware CV parsing** — handles candidates with academic/personal
  projects instead of formal work history (common for students and career
  changers), treating well-described projects as valid evidence of skill.

## Running Locally

```bash
cp .env.example .env  # fill in GROQ_API_KEY and DB credentials

# Start the database
docker-compose up -d db

# Run migrations
alembic upgrade head

# Start the API
uvicorn app.main:app --reload

# In a separate terminal, start the UI
streamlit run ui/streamlit_app.py
```

### Fully containerized

```bash
docker-compose up -d --build
```

Runs both the PostgreSQL database and the FastAPI backend in containers.

## Running Tests

```bash
pytest -v
```

## Project Structure

\`\`\`
app/
├── agents/            # Extractor, Analyzer, Tailor agents
├── api/               # FastAPI routes and dependencies
├── core/              # Config, orchestrator, prompt templates, exceptions
├── models/            # SQLAlchemy database models
├── schemas/            # Pydantic data contracts
└── services/           # PDF/DOCX parsing, rate limiting
tests/                   # pytest suite
ui/                      # Streamlit frontend
alembic/                 # Database migrations
\`\`\`

## Notes

This project evolved from an earlier version (V1) that relied on SBERT cosine
similarity for CV-job matching. V2 replaces that approach with an LLM-based
multi-agent pipeline for more explainable, context-aware scoring.

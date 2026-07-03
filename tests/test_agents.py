import pytest
from app.agents.tailor import TailorAgent
from app.agents.extractor import ExtractorAgent
from app.agents.analyzer import AnalyzerAgent
from app.schemas.internal import Experience


def test_tailor_does_not_hallucinate_technologies():
    """
    Critical guardrail test: the Tailor agent must never introduce
    technologies or skills that are not present in the original text,
    even when the job description mentions them.
    """
    tailor = TailorAgent()

    experience = Experience(
        company="ABC Company",
        role="Backend Developer",
        description="Developed microservice architecture using Python and FastAPI.",
    )

    job_description = (
        "We need a Senior Backend Engineer with Kubernetes, AWS, and "
        "GraphQL experience."
    )

    result = tailor.tailor(experience, job_description)

    forbidden_terms = ["kubernetes", "aws", "graphql"]
    tailored_lower = result.tailored_text.lower()

    for term in forbidden_terms:
        assert term not in tailored_lower, (
            f"Guardrail violation: '{term}' appeared in tailored text "
            f"but was not in the original experience."
        )


def test_analyzer_score_consistency():
    """
    The Analyzer agent should produce reasonably consistent scores
    across repeated runs for the same CV-job pair, even though LLM
    outputs are not perfectly deterministic.
    """
    extractor = ExtractorAgent()
    analyzer = AnalyzerAgent()

    cv_text = """
    Ahmet Yılmaz
    Yazılım Mühendisi

    Deneyim:
    - ABC Şirketi, Backend Developer, 2022-2024
      Python ve FastAPI ile mikroservis mimarisi geliştirdi.

    Yetenekler: Python, FastAPI, Docker, PostgreSQL
    """

    job_description = (
        "We are looking for a Backend Engineer with experience in "
        "Python and FastAPI."
    )

    extracted_cv = extractor.extract(cv_text)

    scores = []
    for _ in range(3):
        result = analyzer.analyze(extracted_cv, job_description)
        scores.append(result.score)

    print(f"\nScores across 3 runs: {scores}")

    max_variance = max(scores) - min(scores)
    assert max_variance <= 20, (
        f"Score variance too high: {scores} (variance: {max_variance}). "
        f"The analyzer may be inconsistent."
    )
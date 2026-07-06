from app.agents.extractor import ExtractorAgent
from app.agents.analyzer import AnalyzerAgent
from app.agents.tailor import TailorAgent
from app.schemas.responses import StreamEvent, FinalResult

extractor = ExtractorAgent()
analyzer = AnalyzerAgent()
tailor = TailorAgent()


def run_pipeline(cv_text: str, job_description: str):
    yield StreamEvent(event_type="extracting", data={"status": "Reading CV..."})
    extracted_cv = extractor.extract(cv_text)

    yield StreamEvent(event_type="analyzing", data={"status": "Comparing with job description..."})
    match_analysis = analyzer.analyze(extracted_cv, job_description)

    yield StreamEvent(event_type="tailoring", data={"status": "Rewriting experiences and projects..."})

    tailored_experiences = [
        tailor.tailor(exp.description, job_description) for exp in extracted_cv.experiences
    ]
    tailored_projects = [
        tailor.tailor(proj.description, job_description) for proj in extracted_cv.projects
    ]

    final_result = FinalResult(
        extracted_cv=extracted_cv,
        match_analysis=match_analysis,
        tailored_experiences=tailored_experiences + tailored_projects,
    )

    yield StreamEvent(event_type="done", data=final_result.model_dump())
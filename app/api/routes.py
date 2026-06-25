from fastapi import APIRouter
from app.schemas.report import AnalyzeResponse, AnalyzeRequest
from app.core.orchestrator import Orchestrator
from app.utils.log import log_request


router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Basic health check endpoint to verify the API is running
    Returns status and the engine type
    """
    return {"status": "ok", "engine": "mock"}


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_idea(request: AnalyzeRequest):
    orchestrator = Orchestrator()

    report, durations_ms = orchestrator.analyze(request.idea)

    log_request(request.idea, durations_ms, report.engine)

    return AnalyzeResponse(
        report=report, meta={"durations_ms": durations_ms, "engine": report.engine}
    )

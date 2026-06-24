from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Basic health check endpoint to verify the API is running
    Returns status and the engine type
    """
    return {
        "status": "ok",
        "engine": "mock"
    }

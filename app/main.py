from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.routes import router as api_router

load_dotenv()


def create_app() -> FastAPI:
    """
    Application factory function.
    Creates and configures the FastAPi application instance.
    """
    app = FastAPI(
        title="Ai product research & Feasibility Analyzer",
        description="Multi-agent feasibility analyzer for product ideas",
        version="0.1.0",
    )

    app.include_router(api_router)

    return app


app = create_app()

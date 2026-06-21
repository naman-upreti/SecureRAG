from fastapi import APIRouter

from app.core.config import settings
from app.core.logging import logger
from app.schemas.health import HealthResponse 
router = APIRouter()


@router.get("/health", response_model = HealthResponse)
def health():
    logger.info("Health endpoint accessed.")

    return {
        "status": "healthy",
        "debug": settings.DEBUG,
    }
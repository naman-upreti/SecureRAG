from fastapi import APIRouter

from app.core.config import settings
from app.core.logging import logger

router = APIRouter()


@router.get("/health")
def health():
    logger.info("Health endpoint accessed.")

    return {
        "status": "healthy",
        "debug": settings.DEBUG,
    }
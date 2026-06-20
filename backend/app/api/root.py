from fastapi import APIRouter

from app.core.config import settings
from app.core.logging import logger

router = APIRouter()


@router.get("/")
def root():
    logger.info("Root endpoint accessed.")

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }
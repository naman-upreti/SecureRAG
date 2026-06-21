from fastapi import APIRouter
from fastapi import Depends 
from app.api.dependencies import get_settings
from app.core.logging import logger
from app.schemas.root import RootResponse 
router = APIRouter()


@router.get("/", response_model = RootResponse)
def root(
    settings = Depends(get_settings)
):
    logger.info("Root endpoint accessed.")

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }
    
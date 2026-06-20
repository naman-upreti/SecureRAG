from fastapi import FastAPI

from app.api.root import router as root_router
from app.api.health import router as health_router

from app.core.config import settings
from app.core.lifespan import lifespan

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

app.include_router(root_router)
app.include_router(health_router)
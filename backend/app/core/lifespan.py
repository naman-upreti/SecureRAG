from contextlib import asynccontextmanager
from pathlib import Path 

from fastapi import FastAPI

from app.core.logging import logger
from app.core.config import settings

@asynccontextmanager
async def lifespan(app:FastAPI):
    """
    Handles application startup and shutdown event
    """

    logger.info("=== Starting SecureRAG ===")

    # create required directories 
    Path("uploads").mkdir(exist_ok=True)
    Path("logs").mkdir(exist_ok=True)

    logger.success("Required directories are ready ")
    
    # Everything before yield runs once at startup.
    yield
    #Everything after yield runs once during shutdown.
    logger.info("=== SecureRAG Shutdown complete ===")



    


from fastapi import FastAPI
### we have imported FastAPI class###we have initialised the FastAPI instance
from app.core.config import settings
#import setting from core config 
from app.core.logging import logger
# import logger from core logging 
from app.core.lifespan import lifespan
#import lifespan from core lifespan

logger.info("Initializing SecureRAG API...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)
# Create the FastAPI application instance.
# This is the main object that manages routes, middleware,
# startup events, and application configuration.

logger.success("SecureRAG API initialized successfully.")


@app.get("/")## this is decorator 
def root():
    logger.info("Root endpoint accessed.")
    return {
        "application":settings.APP_NAME,
        "version":settings.APP_VERSION,
        "status":"running",

    }
### the above is the root router which will return the message 
###FastAPI automatically converts Python dictionaries into JSON.


@app.get("/health")
def health():
    logger.info("Health endpoint accessed.")
    return{
        "status":"healthy",
        "debug":settings.DEBUG
    }
# Health endpoint used by monitoring systems (e.g., Docker, Kubernetes)
# to verify that the API is running correctly.
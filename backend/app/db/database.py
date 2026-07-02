from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

from app.core.config import settings
# Engine manages connections between the application and the database.
# It does not execute queries directly; sessions use the engine to communicate with the database.

engine = create_engine(
    settings.DATABASE_URL,
    echo = settings.DEBUG 
)

# session factory 
SessionLocal  = sessionmaker(
    bind = engine,
    autoflush= False,
    autocommit= False 
)
# SessionLocal creates a new database session for each request.
# Each session is isolated, preventing users from interfering with each other's transactions.

def get_db():
    """
    Creates a database session.

    Ensures the session is closed after the request.
    """
    db = SessionLocal()# session factory that createsone session 
    try:
        yield db
    finally:
        db.close()


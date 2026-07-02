from app.db.database import engine
from app.db.base import Base 

from app.models.document import Document
from app.models.user import User

def init_db():
    Base.metadata.create_all(bind=engine)  # Creates all tables defined in models


if __name__ == "__main__":
    init_db()

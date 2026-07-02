from sqlalchemy.orm import Session
from app.models.document import Document

class DocumentRepository:
    # constructor for the class 
    def __init__(self, db:Session):# whenever someone creates a repository they must provide a database session 
        self.db = db 

    def create_document(
        self, 
        document:Document,
        )-> Document:
        """
        Add a document to the Database
        """
        try:
            self.db.add(document)

            self.db.commit()
            self.db.refresh(document)
            return document
        except Exception:
            self.db.rollback()
            raise 
        
            

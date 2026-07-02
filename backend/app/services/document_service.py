from app.models.document import Document
from app.repositories.document_repository import DocumentRepository


class DocumentService:
    """
    Handles business logic related to documents.
    """
    def __init__(
        self,
        repository: DocumentRepository,
    ):
        self.repository = repository

    def create_document(
        self,
        filename: str,
        file_path: str,
    ) -> Document:

        document = Document(
            filename=filename,
            file_path=file_path,
        )

        return self.repository.create_document(
            document
        )
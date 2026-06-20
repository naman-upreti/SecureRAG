"""This is called

Single Responsibility Principle (SRP)

Every file should have one reason to change.

File	Responsibility
main.py	Create and configure the FastAPI application
config.py	Application configuration
logging.py	Logging configuration
lifespan.py	Startup and shutdown lifecycle
database.py	Database connection and session management
document_service.py (later)	Business logic for documents
documents.py (later)	API endpoints for documents"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    # -----------------------------
    # Application
    # -----------------------------
    APP_NAME: str = "SecureRAG API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    # -----------------------------
    # API
    # -----------------------------
    API_PREFIX: str = "/api/v1"

    # -----------------------------
    # Database
    # -----------------------------
    DATABASE_URL: str = "sqlite:///./secure_rag.db"

    # -----------------------------
    # AI
    # -----------------------------
    GEMINI_API_KEY: str = ""

    # -----------------------------
    # Logging
    # -----------------------------
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


    #JWT
    SECRET_KEY: str = "change_this_to_a_long_random_secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
from loguru import logger
import sys

# Remove Loguru's default logger to avoid duplicate log messages.
logger.remove()

# Configure console logging for development.
logger.add(
    sys.stdout,
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {message}",
    colorize=True,
)

__all__ = ["logger"]
import logging

from app.core.config import LOG_LEVEL

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)
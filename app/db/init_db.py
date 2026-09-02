from app.core.logging import get_logger
from app.db.base import Base
from app.core.database import engine

logger = get_logger(__name__)


def init_db() -> None:
    logger.info("Creating database tables")
    Base.metadata.create_all(bind=engine)

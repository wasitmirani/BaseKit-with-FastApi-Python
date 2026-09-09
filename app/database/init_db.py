from app.core.logging import get_logger
from app.db.base import Base
from app.core.database import engine

# Import models so SQLAlchemy registers them with Base.metadata
from app.modules.users.model import User  # noqa: F401
from app.modules.products.model import Product  # noqa: F401
from app.modules.orders.model import Order, OrderItem  # noqa: F401

logger = get_logger(__name__)


def init_db() -> None:
    logger.info("Creating database tables")
    Base.metadata.create_all(bind=engine)

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(UUID, primary_key=True, default=uuid.uuid4(), unique=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)
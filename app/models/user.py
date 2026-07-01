from sqlalchemy import Column, Integer, DateTime
from datetime import datetime, timezone
from app.models.base import Base

class user(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
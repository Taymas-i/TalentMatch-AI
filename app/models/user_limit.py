from sqlalchemy import Column, Integer, Date, ForeignKey
from datetime import date
from app.models.base import Base

class UserLimit(Base):
    __tablename__ = "user_limits"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    request_count = Column(Integer, default=0)
    last_reset_date = Column(Date, default=date.today)

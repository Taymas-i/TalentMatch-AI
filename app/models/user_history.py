from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone
from app.models.base import Base

class UserHistory(Base):
    __tablename__ = "user_history"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_title = Column(String, nullable= True)
    match_score = Column(Integer, nullable= False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    


from config.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key = True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    title = Column(String)
    descripton = Column(String)
    category = Column(String)
    poster = Column(String)
    likes = Column(Integer)
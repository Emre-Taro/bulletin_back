from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from database import Base

class Post(Base):
    __tablename__ = "posts"
    
    postId = Column(Integer, primary_key=True, index=True)
    postTitle = Column(String)
    message = Column(String)
    created_at = Column(String) 
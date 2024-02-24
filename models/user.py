#!/usr/bin/python3
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    __tablename__ = 'users'
    # Assuming other user attributes are defined here.
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    # Relationship with reviews
    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")


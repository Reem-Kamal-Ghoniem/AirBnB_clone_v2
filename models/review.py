#!/usr/bin/python3
"""Review module for the HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, String


class Review(BaseModel, Base):
    """Review classto store review information"""
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"))
    user_id = Column(String(60), ForeignKey("users.id"))
    """
    place = relationship("Place", back_populates="reviews")
    """

#!/usr/bin/python3
"""This module defines a class Amenity"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This class defines an Amenity by various attributes"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    
    # Define the many-to-many relationship with Place
    place_amenities = relationship(
        'Place',
        secondary='place_amenity',
        back_populates='amenities'
    )

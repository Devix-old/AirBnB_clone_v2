#!/usr/bin/python3
'''the Amenity module'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    '''the Amenities class.'''
    __tablename__ = 'amenities'
    if storage_type == 'db':
        from models.place import place_amenity
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""

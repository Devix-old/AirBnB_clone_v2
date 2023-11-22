#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    # For FileStorage
    @property
    def cities(self):
        """ Getter attribute for cities in FileStorage """
        from models import storage
        city_list = []
        for city_id, city in storage.all('City').items():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

#!/usr/bin/python3
"""This module defines the DBStorage engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
class DBStorage:
    """This class manages the database storage for hbnb"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage engine"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', default='localhost')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+pymysql://{}:{}@{}:3306/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        classes = [User, State, City, Amenity, Place, Review]

        if cls is None:
            objs = {}
            for class_name in classes:
                query = self.__session.query(class_name)
                for obj in query.all():
                    key = "{}.{}".format(class_name, obj.id)
                    objs[key] = obj
            return objs

        if cls not in classes:
            return {}

        objs = {}
        query = self.__session.query(cls)
        for obj in query.all():
            key = "{}.{}".format(cls, obj.id)
            objs[key] = obj

        return objs

    def new(self, obj):
        """Add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

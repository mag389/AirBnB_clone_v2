#!/usr/bin/python3
""" SQL storage engine, vroom """

import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ CLass handling rds storage stuff """
    __engine = None
    __session = None

    def __init__(self):
        """ init. """

        """ This probably isnt what they meant but it makes it easier. """
        mysql_user = os.environ.get('HBNB_MYSQL_USER')
        mysql_pass = os.environ.get('HBNB_MYSQL_PWD')
        mysql_host = os.environ.get('HBNB_MYSQL_HOST')
        mysql_db = os.environ.get('HBNB_MYSQL_DB')

        """ ik this is ugly but pep8 has forced my hand. 80 char limit. :( """
        login = "{}:{}".format(mysql_user, mysql_pass)
        server = "{}/{}".format(mysql_host, mysql_db)
        eng_str = "mysql+mysqldb://{}@{}".format(login, server)

        self.__engine = create_engine("{}".format(eng_str), pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') is 'test':
            """ drop tables HAVE NOT BEEN ABLE TO TEST YET!!!"""
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Query the current DB session for all objects (of cls) """

        fin_dict = {}
        query_objs = []
        """ If class has a value, search for only that class """
        if cls is not None:
            query_objs = self.__session.query(cls).all()
        else:
            query_objs += (self.__session.query(User).all())
            query_objs += (self.__session.query(City).all())
            query_objs += (self.__session.query(State).all())
            query_objs += (self.__session.query(Amenity).all())
            query_objs += (self.__session.query(Place).all())
            query_objs += (self.__session.query(Review).all())
        for obj in query_objs:
                key = obj.to_dict()['__class__'] + "." + obj.to_dict()['id']
                fin_dict[key] = obj
        return fin_dict

    def new(self, obj):
        """ Adds this object instance to the DB """
        self.__session.add(obj)

    def save(self):
        """ Commits to the database session self.__session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete an obj from the current session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reloads the db and assigns the session """
        Base.metadata.create_all(self.__engine)
        """ Just assigns the session to the class variable """
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        scope = scoped_session(Session)
        self.__session = scope()

    def close(self):
        """ close the session """
        self.__session.close()

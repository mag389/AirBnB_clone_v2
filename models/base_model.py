#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            stringy = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k == '__class__':
                    setattr(self, k, type(self))
                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(v, stringy))
                else:
                    setattr(self, k, v)
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs.keys():
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs.keys():
                self.updated_at = datetime.now()
            """
            if "updated_at" in kwargs.keys():
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         stringy)
            if "created_at" in kwargs.keys():
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                         stringy)
            if "__class__" in kwargs.keys():
                del kwargs['__class__']
            """

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictionary = self.to_dict()
        dictionary.pop('__class__')
        return '[{}] ({}) {}'.format(cls, self.id, dictionary)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        """ Holby wants that key removed if it exists (idk why) """
        if '_sa_instance_state' in dictionary:
            dictionary.pop('_sa_instance_state')

        return dictionary

    def delete(self):
        """ Makes this instance commit toaster bath """
        from models import storage
        storage.delete(self)
        """ del self """

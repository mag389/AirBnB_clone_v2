#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """return list of cities with this state id """
        from models.city import City
        from models.__init__ import storage
        from models.engine.file_storage import FileStorage
        cits = FileStorage.all(City)
        cits_b = []
        for city in cits:
            if city.state_id == self.id:
                cits_b.append(city)
        return cits_b

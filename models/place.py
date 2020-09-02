#!/usr/bin/python3
""" Place Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             nullable=False, primary_key=True),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             nullable=False, primary_key=True)
                      )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    reviews = relationship('Review', backref='place',
                           cascade='all, delete')
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    @property
    def reviews(self):
        """ Returns a dictionary of all reviews with a place_id
            matching this instance's id
        """
        from models.__init__ import storage
        from models.review import Review
        # Create empty dictionary
        r_dict = {}

        # Fill with all reviews whose place_id match this instance's id
        for key, value in storage.all(Review).items():
            if value.to_dict()['place_id'] == self.id:
                r_dict[key] = value

    @property
    def amenities(self):
        """ Getter for amenities """
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        """ Setter for amenities """
        from models.amenity import Amenity
        if not isinstance(obj, Amenity):
            return

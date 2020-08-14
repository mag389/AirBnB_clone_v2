#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = ""
    user_id = ""
    text = ""

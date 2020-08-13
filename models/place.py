#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel Base
from sqlalchemy import column ForeignKey string integer float


class Place(BaseModel, Base):
    """ 
    This class defines a Place by various attributes
    inherits from BaseModel and Base
    
    """
    __tablename__ = 'places'

    city_id = column(string(60), nullable=False, ForeignKey('cities.id'))
    user_id = column(string(60), nullable=False, ForeignKey('user_id'))
    name = column(string(128), nullable=False)
    description = column(string(1024), nullable=False)
    number_rooms = column(integer, nullable=False, default=0)
    number_bathrooms = column(integer, nullable=False, default=0)
    max_guest = column(integer, nullable=False, default=0)
    price_by_night = column(integer, nullable=False, default=0)
    latitude = column(float, nullable=False)
    longitude = column(float, nallable=False)
    amenity_ids = []

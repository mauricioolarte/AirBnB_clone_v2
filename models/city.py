#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, Integer, String
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"))
    state = relationship("State")
    places = relationship("place", cascade="delete")
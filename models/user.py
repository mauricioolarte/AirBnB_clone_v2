#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel Base
from sqlalchemy import column string
from sqlalchemy.omr import relationship


class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    inherits from BaseModel and Base

    """
    __tablename__ = 'Users'

    email = column(string(128), nullable=False)
    password = column(string(128), nullable=False)
    first_name = column(string(128), nullable=False)
    last_name = column(string(128), nullable=False)
    places = relationship("place", cascade="delete")

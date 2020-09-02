#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

if getenv("HBNB_TYPE_STORAGE") != "FileStorage":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
else:
    class State(BaseModel):
        """ State class """
        name = ""

        @property
        def cities(self):
            from models.__init__ import storage
            from models.city import City
            lista = []
            all_states = storage.all(City)
            for val in all_states.values():
                if 'state_id' in val.__dict__.keys() and val.__dict__['state_id'] == self.id:
                    lista.append(val)
            return(lista)


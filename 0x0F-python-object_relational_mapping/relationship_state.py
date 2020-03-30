#!/usr/bin/python3
""" Declarative Base class """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship
from relationship_city import City, Base

Base = declarative_base()


class State(Base):
    """ Hybrid attributes """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    city = relationship("City", back_populates="states")

City.states = relationship("State", back_populates="city")
Base.metadata.create_all(engine)

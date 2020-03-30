#!/usr/bin/python3
""" """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
Base = declarative_base()

class City(Base):
    """ Hybrid attributes for city_class """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

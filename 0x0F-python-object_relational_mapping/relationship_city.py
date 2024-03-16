#!/usr/bin/python3
""" Module for writing python file that containes the class
Define City class and delecrative instance """


from relationship_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City represents a table in MySQL database"""

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

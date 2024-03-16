#!/usr/bin/python3
""" Module for writing python file that containes the class
Define state class and delecrative instance """


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State represents a table in MySQL database"""

    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

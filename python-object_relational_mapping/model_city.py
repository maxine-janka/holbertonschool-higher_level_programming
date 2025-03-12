#!/usr/bin/python3
"""Defines a Class called City and links to the MYSQL table cities"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for all classes that will represent db tables
Base = declarative_base()


class City(Base):
    """A City class that links to the 'cities' table in the MySQL database"""
    __tablename__ = 'cities'

    # Define the columns to map the states class to in the states table
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_key=True)

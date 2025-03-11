#!/usr/bin/python3
"""Defines a Class called State and links to the MYSQL table states"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for all classes that will represent db tables
Base = declarative_base()


class State(Base):
    """A State class that links to the 'states' table in the MySQL database"""
    __tablename__ = 'states'

    # Define the columns to map the states class to in the states table
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

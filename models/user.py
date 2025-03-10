#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    if getenv("HBNB_TYPE_STORAGE", "fs") != "db":
        email = ''
        password = ''
        first_name = ''
        last_name = ''
    else:
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")

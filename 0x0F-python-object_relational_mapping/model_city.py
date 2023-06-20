#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""model_city.py
A script to define the model for a City to be represented in our db
"""
import sys
from sqlalchemy import (
    Column,
    Integer,
    String,
    MetaData,
    Sequence,
    create_engine,
    ForeignKey,
)

from model_state import Base


class City(Base):
    """City
    Model for a table cities with the following attributes:
    -class attribute id that represents a column of an auto-generated,
     unique integer, can’t be null and is a primary key
    -class attribute name that represents a column of a string of
    128 characters and can’t be null
    -class attribute state_id that represents a column of an integer,
    can’t be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        Sequence('cities_id_seq'),
        primary_key=True,
        unique=True,
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False,
    )

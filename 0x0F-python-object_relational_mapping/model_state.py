#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
a python file that contains the class definition of a State and
an instance Base = declarative_base():

State class:
inherits from Base Tips
links to the MySQL table states

class attribute id that represents a column of an auto-generated,
unique integer, can’t be null and is a primary key

class attribute name that represents a column of a string with maximum 128
characters and can’t be null

You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost at port 3306

WARNING:
all classes who inherit from Base must be imported before
calling Base.metadata.create_all(engine)
"""
import sys
from sqlalchemy import (
    Column,
    Integer,
    String,
    MetaData,
    Sequence,
    create_engine,
)
from sqlalchemy.orm import (
    declarative_base,
    relationship,
)


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """State:
    A class to model how instances of records in states table
    will be represented
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        Sequence('state_id_seq'),
        primary_key=True,
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
    cities = relationship('City', backref='state')


if __name__ == "__main__":
    """
    A check to ensure we can avoid circular imports
    """
    from model_city import City
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db}"
    )

    Base.metadata.create_all(engine)

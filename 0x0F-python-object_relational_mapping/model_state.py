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
    sessionmaker,
)

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
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


uname = sys.argv[1]
pwd = sys.argv[2]
db = sys.argv[3]
engine = create_engine(
    f"mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db}"
)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

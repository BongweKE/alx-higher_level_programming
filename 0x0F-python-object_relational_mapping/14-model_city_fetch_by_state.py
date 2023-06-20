#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""14-model_city_fetch_by_state.py
A script that prints all City instances from the input database

Your script should take 3 arguments: mysql username, mysql password
and database name
You must import State and Base from model_state
- from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
Results must be display as they are in the example below
(<state name>: (<city id>) <city name>)
Your code should not be executed when imported
"""
import sys
from sqlalchemy import (
    Column,
    Integer,
    String,
    MetaData,
    Sequence,
    create_engine,
    select,
)

from model_state import (
    State,
)

from model_city import (
    City,
)

from sqlalchemy.orm import (
    sessionmaker,
)


def main():
    """main
    A function to separate the code to run when the file is called
    by the interpreter
    """
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db}"
    )
    Session = sessionmaker(bind=engine)

    with Session() as session:
        stmt = select(
            State.name, City.id, City.name
        ).join(
            City
        ).order_by(
            City.id
        )
        res = session.execute(stmt).all()

        for row in res:
            print(f"{row[0]}: ({row[1]}) {row[2]}")


if __name__ == "__main__":
    """A method to prevent unwanted execution of main"""
    main()

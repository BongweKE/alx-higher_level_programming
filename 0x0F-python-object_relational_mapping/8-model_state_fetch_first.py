#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""8-model_state_fetch_first.py

 a script that prints the first State object from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password
and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
 from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
The state you display must be the first in states.id
You are not allowed to fetch all states from the database before displaying
the result
The results must be displayed as they are in the example below
If the table states is empty, print Nothing followed by a new line
Your code should not be executed when imported
"""
import sys
from model_state import (
    Base,
    State,
)
from sqlalchemy import (
    engine,
    create_engine,
    select
)
from sqlalchemy.orm import (
    sessionmaker,
)
from sqlalchemy.exc import (
    NoResultFound
)

def main():
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db}"
    )

    Session = sessionmaker(bind=engine)
    with Session() as session:
        stmt = select(State).order_by(State.id.asc())
        res = session.execute(stmt).scalars().first()

        if res is not None:
            print(f"{res.id}: {res.name}")
        else:
            print("Nothing\n")
if __name__ == "__main__":
    main()

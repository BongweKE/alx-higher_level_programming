#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""10-model_state_my_get.py
a script that prints the State object with the name passed as argument from
the database hbtn_0e_6_usa

Your script should take 4 arguments: mysql username, mysql password,
database name and state name to search (SQL injection free)

You must use the module SQLAlchemy
You must import State and Base from model_state
- from model_state import Base, State

Your script should connect to a MySQL server running on localhost at port 3306
You can assume you have one record with the state name to search
(Name is unique)
Results must display the states.id
If no state has the name you searched for, display Not found
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


def main():
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    s_name = sys.argv[4]
    engine = create_engine(
        f"mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db}"
    )

    Session = sessionmaker(bind=engine)
    with Session() as session:
        stmt = select(State).where(State.name==s_name).order_by(State.id.asc())
        res = session.execute(stmt).scalars().first()

        if res is not None:
            print(res.id)
        else:
            print("Not found")


if __name__ == "__main__":
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""11-model_state_insert.py
a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and
database name

You must use the module SQLAlchemy
You must import State and Base from model_state
- from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Print the new states.id after creation
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

    engine = create_engine(
        f"mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db}"
    )

    Session = sessionmaker(bind=engine)
    with Session() as session:
        Lou = State(name="Louisiana")
        session.add(Lou)
        session.commit()
        print(Lou.id)


if __name__ == "__main__":
    main()

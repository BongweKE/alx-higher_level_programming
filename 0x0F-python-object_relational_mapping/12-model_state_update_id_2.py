#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""12-model_state_update_id_2.py

a script that changes the name of a State object from the database
hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password
and database name
You must use the module SQLAlchemy
You must import State and Base from model_state
- from model_state import Base, State

Your script should connect to a MySQL server running on localhost at port 3306

Change the name of the State where id = 2 to New Mexico
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
    """main:
    Hide away code that should't be executed when the module is imported
    """
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db}"
    )

    Session = sessionmaker(bind=engine)
    with Session() as session:
        stmt = select(State).where(State.id == 2)
        res = session.execute(stmt).scalar_one()
        if res is not None:
            res.name = "New Mexico"
            session.commit()


if __name__ == "__main__":
    """run main code"""
    main()

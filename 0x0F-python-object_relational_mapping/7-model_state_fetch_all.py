#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""7-model_state_fetch_all.py
a script that lists all State objects from the database hbtn_0e_6_usa/

Your script should take 3 arguments: mysql username, mysql password
and database name/
You must use the module SQLAlchemy/
You must import State and Base from model_state/
-from model_state import Base, State/
Your script should connect to a MySQL server running on localhost at port 3306/
Results must be sorted in ascending order by states.id/
The results must be displayed as they are in the example below/
Your code should not be executed when imported/
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
    stmt = select(State).order_by(State.id.asc())
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(f"{row[0]}: {row[1]}")


if __name__ == "__main__":
    """run main code"""
    main()

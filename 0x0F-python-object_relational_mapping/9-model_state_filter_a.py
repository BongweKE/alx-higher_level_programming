#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""9-model_state_filter_a.py

a script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and
database name
You must use the module SQLAlchemy
You must import State and Base from model_state
- from model_state import Base, State

Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
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
        search = "%a%"
        stmt = select(
            State
        ).order_by(
            State.id.asc()
        ).filter(
            State.name.like(search)
        )
        res = session.execute(stmt).scalars().all()

        for row in res:
            print(f"{row.id}: {row.name}")


if __name__ == "__main__":
    """run main code"""
    main()

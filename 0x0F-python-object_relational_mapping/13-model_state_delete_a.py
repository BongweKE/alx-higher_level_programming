#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""13-model_state_delete_a.py
A script to delete a given state using commandline args
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
            session.delete(row)
        session.commit()


if __name__ == "__main__":
    """run main code"""
    main()

#!/usr/bin/python3
"""Script that will lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()
    states_delete = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )

    if states_delete:
        for state in states_delete:
            session.delete(state)
        session.commit()
    session.close()
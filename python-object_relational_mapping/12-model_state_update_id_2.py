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
    state_update = session.query(State).filter(State.id == 2).first()

    if state_update:
        state_update.name = "New Mexico"
        session.commit()

    session.close()
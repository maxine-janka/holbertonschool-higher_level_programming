#!/usr/bin/python3
"""Lists all objects that belong to the State class from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Don't execute when imported
if __name__ == "__main__":

    # Create engine with credentials from command line to connect to DB
    engine = create_engine(
        'mysql+mysql://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
    )
    #Creates a table from State class that inherits from Base
    Base.metadata.create_all(engine)

    # Create interactive session with DB to make queries
    create_session_obj = sessionmaker(engine)
    session = create_session_obj() #instantiate a session

    # Query, print and close
    for state in session.query(State).order_by(State.id.asc()).all():
        print("{}: {}".format(state.id, state.name))
    session.close()

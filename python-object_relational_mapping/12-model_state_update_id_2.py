#!/usr/bin/python3
"""Changes the name of the state where the state.id = 2
   to 'New Mexico' the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

# Don't execute when imported
if __name__ == "__main__":

    # Create engine with credentials from command line to connect to DB
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    # Creates a table from State class that inherits from Base
    # Dont need this line, it will create a table if its not there
    # Base.metadata.create_all(bind=engine)

    # Create interactive session with DB to make queries
    create_session_obj = sessionmaker(bind=engine)
    session = create_session_obj()  # Instantiate a session

    update_state = session.query(State).get(2)
    update_state.name = "New Mexico"

    session.commit()

    session.close()

#!/usr/bin/python3

"""
Create a script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get the arguments from the command line
    mysql_username, mysql_password, \
        database_name, state_name = sys.argv[1:5]
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name))
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query the database
    state = session.query(State).filter(
        State.name == state_name).first()
    # Print the result
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    # Close the session
    session.close()

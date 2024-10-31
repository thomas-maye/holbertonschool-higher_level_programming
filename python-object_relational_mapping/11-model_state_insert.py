#!/usr/bin/python3

"""
Create a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

Usage:
    Should take 3 arguments: mysql username, mysql password and database name
    Ex: ./11-model_state_insert.py root root hbtn_0e_6_usa

Arguments:
    mysql username: username to connect the mySQL
    mysql password: password to connect the mySQL
    database name: name of the database

Result:
    Print the new state id
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get the arguments from the command line
    mysql_username, mysql_password, database_name = sys.argv[1:4]
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name))
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Create a new state
    new_state = State(name='Louisiana')
    # Add the new state to the session
    session.add(new_state)
    # Commit the transaction
    session.commit()
    # Query the database
    state = session.query(State).filter(
        State.name == 'Louisiana').first()
    # Print the result
    print("{}".format(state.id))
    # Close the session
    session.close()

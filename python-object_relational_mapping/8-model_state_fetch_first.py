#!/usr/bin/python3

"""
Create a script that prints the first State object from the database hbtn_0e_6_usa

Usage: ./8-model_state_fetch_first.py
    <mysql username>
    <mysql password>
    <database name>

Arguments:
    mysql_username (str): MySQL username
    mysql_password (str): MySQL password
    database_name (str): MySQL database name

Returns:
    The first state in the database hbtn_0e_6_usa
"""

import sys
import sqlalchemy as db
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
    # Query the database
    state = session.query(State).order_by(State.id).first()
    # Print the results
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()

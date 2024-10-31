#!/usr/bin/python3

"""
Create a session for database access using SQLAlchemy
"""

import sys

from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Fetch all states from the database

    Usage: ./7-model_state_fetch_all.py
    <mysql username>
    <mysql password>
    <database name>

    Arguments:
        mysql_username (str): MySQL username
        mysql_password (str): MySQL password
        database_name (str): MySQL database name

    Returns:
        The states in the database
    """

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
    states = session.query(State).order_by(State.id).all()
    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()

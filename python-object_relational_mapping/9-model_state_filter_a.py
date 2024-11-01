#!/usr/bin/python3

"""
Create a script that lists all State objects that contain the letter a
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Create a script that lists all State objects that contain the letter a
    from the database hbtn_0e_6_usa

    Usage: ./9-model_state_filter_a.py
        <mysql username>
        <mysql password>
        <database name>

    Arguments:
        mysql_username (str): MySQL username
        mysql_password (str): MySQL password
        database_name (str): MySQL database name

    Returns:
        The states in the database hbtn_0e_6_usa that contain the letter a
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
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()

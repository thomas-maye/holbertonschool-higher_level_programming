#!/usr/bin/python3

"""
Delete all State objects with a name containing the letter a from the database
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Delete all State objects with a name containing the letter
    a from the database from the database hbtn_0e_6_usa

    Usage:
        ./13-model_state_delete_a.py
        <mysql username>
        <mysql password>
        <database name>

    Arguments:
        mysql username: username for MySQL server
        mysql password: password for MySQL server
        database name: name of the database to access

    Returns:
        The list of cities with their state names in
        the database hbtn_0e_14_usa
    """

    # Connect to the database
    mysql_username, mysql_password, database_name = sys.argv[1:4]
    # Create a connection to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name))
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query the database
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()
    # Close the session
    session.close()

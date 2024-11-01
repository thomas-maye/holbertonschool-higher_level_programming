#!/usr/bin/python3

"""
Create a script that lists all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_city import Base, City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Create a script that lists all City objects from the
    database hbtn_0e_14_usa

    Usage:
        ./14-model_city_fetch_by_state.py
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
    cities = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    # Close the session
    session.close()

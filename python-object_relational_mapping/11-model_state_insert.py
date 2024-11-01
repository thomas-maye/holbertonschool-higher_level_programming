#!/usr/bin/python3

"""
Create a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Create a script that adds the State object “Louisiana
    to the database hbtn_0e_6_usa

    Usage : ./11-model_state_insert.py
        <mysql username>
        <mysql password>
        <database name>

    Arguments:
        username: the username
        password: the password
        database: the name of the database to connect

    Returns:
        The id of the new state added
    """
    # Get the arguments from the command line
    mysql_username, mysql_password, \
        database_name = sys.argv[1:4]
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password, database_name))
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Add a new state
    new_state = State(name='Louisiana')
    # Add the new state to the session
    session.add(new_state)
    # Commit the transaction
    session.commit()
    print(new_state.id)
    # Close the session
    session.close()

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
    ”"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()

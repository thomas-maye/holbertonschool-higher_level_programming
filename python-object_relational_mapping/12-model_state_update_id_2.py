#!/usr/bin/python3

"""
Create a scritp that changes the name of a State object from the database
hbtn_0e_6_usa for exemple change the name of the state where id=2 to New Mexico
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Create a scritp that changes the name of a State object from the database
    hbtn_0e_6_usa for ex change the name of the state where id=2 to New Mexico

    Usage: ./12-model_state_update_id_2.py
        <mysql username>
        <mysql password>
        <database name>

    Arguments:
        mysql_username (str): MySQL username
        mysql_password (str): MySQL password
        database_name (str): MySQL database name

    Returns:
        The name of the state with the id 2 changed to New Mexico
    """
    # Get the arguments from the command line
    mysql_username, mysql_password, database_name = sys.argv[1:4]
    state_id = 2
    new_state_name = "New Mexico"
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name))
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query the database
    state = session.query(State).filter(State.id == state_id).first()
    if state:
        state.name = new_state_name
        session.commit()
    else:
        print("Not found")
    # Close the session
    session.close()

#!/usr/bin/python3

"""
Create a script that lists all cities from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """ List all states in the states table of hbtn_0e_0_usa where the name
    matches the argument.

    Usage:
        ./3-my_safe_filter_states.py
        <mysql username>
        <mysql password>
        <database name>
        <state name to search for>

    Arguments:
        sys.argv[1]: The MySQL username
        sys.argv[2]: The MySQL password
        sys.argv[3]: The MySQL database name
        sys.argv[4]: The state name to search for

    Returns:
        The states in the database with a name that matches the argument.
    """

    # Get the arguments from the command line
    mysql_username, \
        mysql_password, database_name, state_name = sys.argv[1:5]
    # Connect to the database
    db = MySQLdb.connect(
        # My host, usually localhost
        host="localhost",
        # The port number to connect to MySQL
        port=3306,
        # The user name specified in the command line
        user=mysql_username,
        # The password specified in the command line
        passwd=mysql_password,
        # The database name specified in the command line
        db=database_name
        )
    # Create a cursor object
    cursor = db.cursor()
    # Create a query string
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    # Execute the query
    cursor.execute(query, (state_name,))
    # Fetch all the rows in a list of lists
    states = cursor.fetchall()
    for state in states:
        print(state)
    # Close the cursor and database
    cursor.close()
    db.close()

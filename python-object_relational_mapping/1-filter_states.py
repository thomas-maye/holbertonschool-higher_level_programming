#!/usr/bin/python3

"""
Create a script that lists states with a name starting with N
from the database specified in the command line.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """
    List states with a name starting with N from the database
    specified in the command line.

    Usage:
        ./1-filter_states.py
        <mysql username>
        <mysql password>
        <database name>

    Arguments:
        sys.argv[1]: The MySQL username
        sys.argv[2]: The MySQL password
        sys.argv[3]: The MySQL database name

    Returns:
        The states in the database with a name starting with N
    """
    # Get the arguments from the command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
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
    # Execute the query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    # Fetch all the rows in a list of lists
    states = cursor.fetchall()
    # Iterate over the rows to print the states
    for state in states:
        # Print the state
        if state[1][0] == 'N':
            print(state)
    # Close the cursor and database
    cursor.close()
    db.close()

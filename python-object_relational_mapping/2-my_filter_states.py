#!/usr/bin/python3

"""
Create a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    List all states in the states table of hbtn_0e_0_usa where the name
    matches the argument.

    Usage:
        ./2-my_filter_states.py
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
        The states in the database with a name that matches the argument
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
    cursor.execute("SELECT * FROM states WHERE name = %s \
        ORDER BY id ASC", (sys.argv[4],))
    # Fetch all the rows in a list of lists
    states = cursor.fetchall()
    # Iterate over the rows to print the states
    for state in states:
        if state[1] == sys.argv[4]:
            # Print the state
            print(state)
    # Close the cursor and database
    cursor.close()
    db.close()

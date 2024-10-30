#!/usr/bin/python3

"""
Create a connection to the database and retrieve all 
states sorted by id from the database specified in the 
command line.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Retrieve all states sorted by id from the database 
    specified in the command line.

    Usage:
        ./0-select_states.py 
        <mysql username> 
        <mysql password> 
        <database name>

    Arguments:
        sys.argv[1]: The MySQL username
        sys.argv[2]: The MySQL password
        sys.argv[3]: The MySQL database name

    Returns:
        The states in the database sorted by id
    """
    # Connect to the database
    db = MySQLdb.connect(
        # My host, usually localhost
        host="localhost",
        # The user name specified in the command line
        user=sys.argv[1],
        # The password specified in the command line
        passwd=sys.argv[2],
        # The database name specified in the command line
        db=sys.argv[3],
        # The port number to connect to MySQL
        port=3306)

# Create a cursor object
cursor = db.cursor()
# Execute the query
cursor.execute("SELECT * FROM states ORDER BY id ASC")
# Fetch all the rows in a list of lists
states = cursor.fetchall()
# Iterate over the rows to print the states
for state in states:
    # Print the state
    print(state)
# Close the cursor and database
cursor.close()
db.close()

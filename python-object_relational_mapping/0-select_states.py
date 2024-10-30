#!/usr/bin/python3

"""
Create a connection to the database and retrieve all states sorted by id
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """The code is not executed when the file is importe

    Arguments:
        sys.argv[1]: The MySQL username
        sys.argv[2]: The MySQL password
        sys.argv[3]: The MySQL database name

    Returns:
        The states in the database sorted by id
    """
    db = MySQLdb.connect(  # Connect to the database
        host="localhost",  # My host, usually localhost
        user=sys.argv[1],  # The user name specified in the command line
        passwd=sys.argv[2],  # The password specified in the command line
        db=sys.argv[3],  # The database name specified in the command line
        port=3306)  # The port number to connect to MySQL
cursor = db.cursor()  # Create a cursor object
cursor.execute("SELECT * FROM states ORDER BY id ASC")  # Execute the query
states = cursor.fetchall()  # Fetch all the rows in a list of lists
for state in states:  # Print the states in the list of lists states
    print(state)  # Print the state
cursor.close()  # Close the cursor
db.close()  # Close the database

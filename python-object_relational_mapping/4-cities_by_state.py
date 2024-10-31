#!/usr/bin/python3

"""
Create a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    List all cities in the cities table of hbtn_0e_4_usa where the state name
    matches the argument.

    Usage:
        ./4-cities_by_state.py
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
        The cities in the database with a state name that matches the argument.
    """

    # Get the arguments from the command line
    mysql_username, \
        mysql_password, database_name = sys.argv[1:4]
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
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    # Execute the query
    cursor.execute(query)
    # Fetch all the rows in a list of lists
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    # Close the cursor and database
    cursor.close()
    db.close()

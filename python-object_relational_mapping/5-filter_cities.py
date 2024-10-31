#!/usr/bin/python3

"""
Create a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    """The script should take 4 arguments: mysql username, mysql password,
    database name and state name (SQL injection free!)

    Usage:
        ./5-filter_cities.py
        <mysql username>
        <mysql password>
        <database name>
        <state name>

    Arguments:
        mysql_username (str): MySQL username
        mysql_password (str): MySQL password
        database_name (str): MySQL database name
        state_name (str): State name

    Returns:
        The cities in the database with a state name that matches the argument.
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
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    # Execute the query
    cursor.execute(query, (state_name,))
    # Fetch all the rows in a list of lists
    cities = cursor.fetchall()
    # Print the results
    print(", ".join([city[0] for city in cities]))
    # Close all cursors and databases
    cursor.close()
    db.close()

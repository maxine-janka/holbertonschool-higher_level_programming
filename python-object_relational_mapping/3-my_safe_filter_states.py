#!/usr/bin/python3
"""Displays all values iin the 'states' table from the database
   hbtn_0e_0_usa, where the 'name; matches the state name passed
   in as a argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":

    # connect to a mysql database with args provided when running the script
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    # Get state name from the command line
    state_name = sys.argv[4]

    # Like a pointer that sends commands to the db to retrieve the results
    cursor = db.cursor()

    # Cursor sends query
    # User parametized query to prevent SQL injection
    cursor.execute("SELECT id, name FROM states \
                   WHERE name = %s \
                   ORDER BY id ASC", (state_name,))

    # fetch all rows from states table & store in 'states' as a list of tuples
    states = cursor.fetchall()

    # Iterate rows and print
    for state in states:
        print(state)

    # Close the cursor and free up resources, close db connection
    cursor.close()
    db.close()

#!/usr/bin/python3
"""Lists all 'cities' from the database hbtn_0e_4_usa."""

import sys
import MySQLdb

# Don't execute when imported
if __name__ == "__main__":

    # connect to a mysql database with args provided when running the script
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    # Like a pointer that sends commands to the db to retrieve the results
    cursor = db.cursor()

    # Cursor sends query
    # Link cities to states where state_id = state_id
    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities\
                   JOIN states ON cities.state_id = states.id\
                   ORDER BY cities.id ASC")

    # Grab all rows returned by above query
    cities = cursor.fetchall()

    # Iterate rows and print
    for city in cities:
        print(city)

    # Close the cursor and free up resources, close db connection
    cursor.close()
    db.close()

#!/usr/bin/python3
"""Lists all 'cities' from the database hbtn_0e_4_usa that belong
    to that 'state' and given as a argument"""

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

    # Get state name from the command line
    state_name = sys.argv[4]

    # Cursor sends query
    cursor.execute("SELECT cities.name\
                   FROM cities\
                   JOIN states ON cities.state_id = states.id\
                   WHERE states.name = %s\
                   ORDER BY cities.id ASC", (state_name,))

    # Grab all rows returned by above query
    cities = cursor.fetchall()

    string_of_cities = ", ".join(city[0] for city in cities)
    print(string_of_cities)

    # Close the cursor and free up resources, close db connection
    cursor.close()
    db.close()

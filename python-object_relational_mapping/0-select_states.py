#!/usr/bin/python3
"""Lists all 'states' from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

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

# Cursor sends query to db
cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

# fetch all rows from states table and store in 'states' as a list of tuples
states = cursor.fetchall()

# Iterate rows and print
for state in states:
    print(state)

# Close the cursor and free up resources, close db connection
cursor.close()
db.close()

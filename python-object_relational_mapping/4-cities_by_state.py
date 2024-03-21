#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys

if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = database.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities JOIN states
                   ON cities.state_id = states.id
                   ORDER BY cities.id""")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()

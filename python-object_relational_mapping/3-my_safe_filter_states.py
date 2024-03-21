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
    cursor.execute("""
                   SELECT * FROM states
                   WHERE name LIKE BINARY %s
                   ORDER BY states.id
                   """, (sys.argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()

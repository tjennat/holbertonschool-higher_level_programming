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
    cursor.execute("""SELECT cities.name
                  FROM cities
                  JOIN states
                  ON cities.state_id = states.id
                  WHERE states.name = %s
                  ORDER BY cities.id""", (sys.argv[4],))

    results = cursor.fetchall()

    city_names = [row[0] for row in results]
    print(", ".join(city_names))

    cursor.close()
    database.close()

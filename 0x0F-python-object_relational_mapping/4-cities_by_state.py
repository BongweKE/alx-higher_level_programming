#!/usr/bin/python3
"""4-cities_by_stare.py
a script that lists all cities from the database hbtn_0e_4_usa

Your script should take 3 arguments: mysql username, mysql password
and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
import MySQLdb
import sys

def main():
    """main
    Section to isolate the executable part of the script
    """
    args = sys.argv
    user = args[1]
    password = args[2]
    db = args[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db,
        charset="utf8"
    )

    cur = conn.cursor()
    # select the citirs by states
    cur.execute(
        """
        SELECT cities.id, cities.name, states.name
          FROM cities INNER JOIN states
        ON
          cities.state_id = states.id
        ORDER BY
          cities.id ASC
        """
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()

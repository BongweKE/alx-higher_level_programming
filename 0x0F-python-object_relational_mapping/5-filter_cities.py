#!/usr/bin/python3
"""5-filter_cities.py
a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password,
database name and state name (SQL injection free!)

You must use the module MySQLdb (import MySQLdb)/
Your script should connect to a MySQL server running on localhost at port 3306/
Results must be sorted in ascending order by cities.id/
You can use only execute() once/
Your code should not be executed when imported/
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
    searched_state = args[4]

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
        SELECT cities.name
          FROM cities INNER JOIN states
            ON cities.state_id = states.id
        WHERE states.name=%(s_state)s
         ORDER BY cities.state_id
           ASC;
        """,
        {'s_state': searched_state}
    )
    query_rows = cur.fetchall()
    print(', '.join([row[0] for row in query_rows]))

    cur.close()
    conn.close()


if __name__ == "__main__":
    """run main code"""
    main()

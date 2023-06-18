#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""0-select_states.py
a script that lists all states from the database hbtn_0e_0_usa:/

should take 3 arguments: mysql username, mysql password and
    database name (no argument validation needed) /
You must use the module MySQLdb (import MySQLdb)/
Your script should connect to a MySQL server running on localhost at port 3306/
Results must be sorted in ascending order by states.id/
Results must be displayed as they are in the example below/
Your code should not be executed when imported/
"""
import MySQLdb
import sys


def main():
    """main
    Section of the script to execute the main code
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
    # Get the required info from the db using the cursor
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    # Ensure that code only runs when this module is called from cmd
    main()

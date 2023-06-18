#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""2-my_filter_states.py
a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.

Your script should take 4 arguments:
    mysql username, mysql password, database name and state name searched
    (no argument validation needed)/
You must use the module MySQLdb (import MySQLdb)/
Your script should connect to a MySQL server running on localhost at port 3306/
You must use format to create the SQL query with the user input/
Results must be sorted in ascending order by states.id/
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
    searched_name = args[4]

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
    cur.execute(
        "SELECT * FROM states WHERE name='{s_name}' ORDER BY id ASC".format(
            s_name=searched_name
        )
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    # Ensure that code only runs when this module is called from cmd
    main()

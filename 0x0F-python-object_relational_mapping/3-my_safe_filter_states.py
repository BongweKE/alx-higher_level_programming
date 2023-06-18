#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""3-my_safe_filter_states.py
a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments:
mysql username, mysql password, database name and state name searched
(safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
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
        """
        SELECT *
        FROM states
        WHERE name=%(s_name)s
        ORDER BY id
        ASC
        """,
        {'s_name': searched_name}
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    # Ensure that code only runs when this module is called from cmd
    main()

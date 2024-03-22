#!/usr/bin/python3
"""
Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where name matches
the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ connect to database
    if len(sys.argv) != 5:
        sys.exit(1)"""

    u = sys.argv[1]  # user
    p = sys.argv[2]  # password
    db = sys.argv[3]
    state_name = sys.argv[4]

    con = MySQLdb.connect(host="localhost", user=u, passwd=p, db=db, port=3306)

    cur = con.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}'".format(state_name)
    cur.execute(query)
    results = cur.fetchall()

    if results:
        for i in results:
            print(i)
    else:
        print("No matching results found")

    # close database connections
    cur.close()
    con.close()

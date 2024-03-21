#!/usr/bin/python3
""" Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ connect to database """
    if len(sys.argv) != 5:
        sys.exit(1)

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    con = MySQLdb.connect(host="localhost", user=user, passwd=passwd, db=db, port=3306)

    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
    rows = cur.fetchall()

    for i in rows:
        print(i)

    # close database connections
    cur.close()
    con.close()

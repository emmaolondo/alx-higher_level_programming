#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa:
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ connect to database """
    if len(sys.argv) != 4:
        sys.exit(1)

    u = sys.argv[1]  # user
    p = sys.argv[2]  # password
    db = sys.argv[3]

    con = MySQLdb.connect(host="localhost", user=u, passwd=p, db=db, port=3306)

    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    rows = cur.fetchall()

    for i in rows:
        print(i)

    # close database connections
    cur.close()
    con.close()

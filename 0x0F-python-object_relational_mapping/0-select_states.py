#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    """ Connect to database """
    if len(sys.argv) != 4:
        sys.exit(1)

    u = sys.argv[1]  # user
    p = sys.argv[2]  # password
    db = sys.argv[3]
    port = 3306

    # connect to database
    con = MySQLdb.connect(host="localhost", user=u, passwd=p, db=db, port=port)

    cur = con.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    # read each row and print
    for i in rows:
        print(i)

    # close the database connection
    cur.close()
    con.close()

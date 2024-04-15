#!/usr/bin/python3
""" connecting with mysql """
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    db = sys.argv[3]  # database
    u = sys.argv[1]  # username
    p = sys.argv[2]  # password

    con = MySQLdb.connect(host="localhost", port=3306, user=u, passwd=p, db=db)
    cur = con.cursor()
    cur.execute("SELECT * FROM state ORDER BY id ASC")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    con.close()

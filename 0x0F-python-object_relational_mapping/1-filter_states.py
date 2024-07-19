#!/usr/bin/python3
""" connecting with mysql """
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    u = sys.argv[1]  # username
    p = sys.argv[2]  # password
    db = sys.argv[3]  # database

    # connect to mysqldb
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=u,
            passwd=p,
            db=db,
            charset="utf8")
    cur = conn.cursor()
    # execute command
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' COLLATE utf8_bin \
            ORDER BY id")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    conn.close()

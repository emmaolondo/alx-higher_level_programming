#!/usr/bin/python3
""" connecting with mysql """
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    u = sys.argv[1]  # username
    p = sys.argv[2]  # password
    db = sys.argv[3]  # database
    arg = sys.argv[4]

    con = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=u,
            passwd=p,
            db=db,
            charset="utf8"
            )
    cur = con.cursor()
    query = "SELECT cities.name FROM cities "\
    "JOIN states ON states.id = cities.state_id " \
    "WHERE states.name LIKE %s ORDER BY cities.id "
    cur.execute(query, (arg + "%",))
    rows = cur.fetchall()
    for i in rows:
        print(i)
#     print()
    cur.close()
    con.close()

#!/usr/bin/python3

import MySQLdb
import sys


def run():
    """Fetching from database"""
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=u, passwd=p, db=d, port=3306)
    cur = db.cursor()
    sql = """
    SELECT states.id AS id,
    states.name AS name
    FROM states WHERE name LIKE 'N%'
    """
    cur.execute(sql)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    run()

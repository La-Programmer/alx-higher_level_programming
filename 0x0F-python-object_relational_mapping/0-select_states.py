#!/usr/bin/python3

import sys
import MySQLdb


def run():
    """Fetching from database"""
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=u, passwd=p, db=d, port=3306)
    cur = db.cursor()
    sq = """
    SELECT states.id AS id,
    states.name AS name
    FROM states ORDER BY id ASC"""
    cur.execute(sq)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    run()

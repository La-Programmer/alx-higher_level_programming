#!/usr/bin/python3
"""MODULE 4 FETCHING CITIES WITH RESPECT TO STATES"""
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
    SELECT cities.id,
    cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id=states.id
    ORDER BY cities.id ASC"""
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    run()

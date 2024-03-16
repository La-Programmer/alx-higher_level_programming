#!/usr/bin/python3
"""MODULE 5 FETCHING CITIES WITH RESPECT TO A STATE INPUTTED BY THE USER"""
import MySQLdb
import sys


def run():
    """Fetching from database"""
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    search_val = sys.argv[4]

    db = MySQLdb.connect(host='localhost', user=u, passwd=p, db=d, port=3306)
    cur = db.cursor()
    sql = """
    SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states
    ON cities.state_id=states.id
    WHERE states.name=%s
    ORDER BY cities.id ASC;"""
    params = (search_val,)
    cur.execute(sql, params)
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[1])
    print(*cities, sep=", ")

    cur.close()
    db.close()


if __name__ == "__main__":
    run()

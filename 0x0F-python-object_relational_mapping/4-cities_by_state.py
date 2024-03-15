#!/usr/bin/python3

import MySQLdb
import sys


def run():
	"""Fetching from database"""
	username = sys.argv[1]
	password = sys.argv[2]
	database = sys.argv[3]

	db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database, port=3306)
	cur = db.cursor()
	sql = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC"
	cur.execute(sql)
	rows = cur.fetchall()
	for row in rows:
		print(row)

if __name__ == "__main__":
	run()

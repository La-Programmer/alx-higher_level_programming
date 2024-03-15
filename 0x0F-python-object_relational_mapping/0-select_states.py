#!/usr/bin/python3

import sys
import MySQLdb


def run():
	"""Fetching from database"""
	username = sys.argv[1]
	password = sys.argv[2]
	database = sys.argv[3]

	db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database, port=3306)
	cur = db.cursor()

	cur.execute("SELECT states.id AS id, states.name AS name FROM states ORDER BY id ASC")

	rows = cur.fetchall()
	for row in rows:
		print(row)

	cur.close()
	db.close()


if __name__ == "__main__":
	run()

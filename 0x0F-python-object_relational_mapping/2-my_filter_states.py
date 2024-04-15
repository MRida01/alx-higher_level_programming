#!/usr/bin/python3
"""
Script to display all values in the states table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()

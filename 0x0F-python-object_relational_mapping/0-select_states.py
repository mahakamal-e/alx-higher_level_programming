#!/usr/bin/python3
""" Module for writing script lists all states """


import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states")
    result = cursor.fetchall()
    for state in result:
        print(state)

    cursor.close()
    conn.close()

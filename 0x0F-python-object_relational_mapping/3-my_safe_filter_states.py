#!/usr/bin/python3
"""
Module for writing a Script that takes in an argument
and displays all values
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost",
                                    port=3306,
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   [sys.argv[4]])
    result = cursor.fetchall()

    for state in result:
        print(state)

    cursor.close()
    db_connection.close()

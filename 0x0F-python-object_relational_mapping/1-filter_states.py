#!/usr/bin/python3
""" lists all states with a name starting with N """


import MySQLdb
import sys

if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost",
                                    port=3306,
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' "
                   "ORDER BY states.id ASC")
    result = cursor.fetchall()

    for state in result:
        print(state)

    cursor.close()
    db_connection.close()

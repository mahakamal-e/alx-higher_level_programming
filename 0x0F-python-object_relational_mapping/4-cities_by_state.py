#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa """


import sys
import MySQLdb

if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost",
                                    port=3306,
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")

    result = cursor.fetchall()

    for city in result:
        print(city)

    cursor.close()
    db_connection.close()

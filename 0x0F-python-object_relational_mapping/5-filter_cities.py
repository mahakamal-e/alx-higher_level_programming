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
    cursor.execute("SELECT cities.name FROM cities "
                   "INNER JOIN states ON states.id=cities.state_id "
                   "WHERE states.name = %s ORDER BY states.id ASC",
                   [sys.argv[4]])

    result = cursor.fetchall()

    city_names = ", ".join(city[0] for city in result)
    print(city_names)

    cursor.close()
    db_connection.close()

#!/usr/bin/python3
""" Method """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    query = MySQLdb.connect(host='localhost',
                            user=argv[1],
                            passwd=argv[2],
                            db=argv[3],
                            port=3306)
    cur = query.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY\
    states.id ASC")
    cur2 = cur.fetchall()
    for result in cur2:
        print(result)
    query.close()
    cur.close()

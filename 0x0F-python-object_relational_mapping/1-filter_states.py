#!/usr/bin/python3
""" Method """
import MySQLdb
from sys import argv


def main():
    """ fenction to query in MySql server db witn name start N"""
    query = MySQLdb.connect(host='localhost',
                            user=argv[1],
                            passwd=argv[2],
                            database=argv[3],
                            port=3306,
                            charset='utf8')
    cur = query.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' OR name LIKE \
    'n%' ORDER BY id ASC;")
    cur2 = cur.fetchall()
    for result in cur2:
        print(result)
    query.close()
    cur.close()

if __name__ == "__main__":
    main()

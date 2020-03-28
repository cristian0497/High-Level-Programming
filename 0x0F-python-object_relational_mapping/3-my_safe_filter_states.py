#!/usr/bin/python3
""" Method """
import MySQLdb
from sys import argv


def main():
    """ function to query in MySql server db witn name start N"""
    try:
        query = MySQLdb.connect(host='localhost',
                                user=argv[1],
                                passwd=argv[2],
                                database=argv[3],
                                port=3306,
                                charset='utf8')
        cur = query.cursor()
        cur.execute('''SELECT * FROM states WHERE name = %s ORDER BY \
        states.id ASC''',(argv[4],))
        for result in cur.fetchall():
            print(result)
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()

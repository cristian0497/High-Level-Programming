#!/usr/bin/python3
""" Method """
import MySQLdb
from sys import argv


def main():
    """ function to query in MySql server db witn name start N"""
    query = MySQLdb.connect(host='localhost',
                            user=argv[1],
                            passwd=argv[2],
                            database=argv[3],
                            port=3306,
                            charset='utf8')
    cur = query.cursor()
    cur.execute("SELECT c.name FROM cities c JOIN states s\
    ON s.id = c.state_id \
    WHERE s.name=%s \
    ORDER BY c.id ASC", (argv[4], ))
    r = cur.fetchall()
    print(", ".join(city[0] for city in r))
if __name__ == "__main__":
    main()

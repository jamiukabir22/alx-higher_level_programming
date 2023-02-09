#!/usr/bin/python3
""" Script that lists all states from a database hbtn_0e_0_usa"""

if __name__ == '__main__:
    import MySQLdb
    import sys

    db_connection = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwrd=sys.argv[2], db=sys.argv[3]
    cur = db_connection.cursor()
    cur.execute("""SELECT * FROM states
    WHERE name LIKE BINARY 'N%'
    ORDER BY id ASC"""
    rows = cur.fecthall()
    for row in rows:
    print(row)

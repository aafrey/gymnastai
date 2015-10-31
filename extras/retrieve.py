__author__ = 'austin'
import MySQLdb as mdb

con = mdb.connect('localhost', 'austin', 'chicken4wing', 'prdb')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Anthropometry")

    rows = cur.fetchall()

    for row in rows:
        print row


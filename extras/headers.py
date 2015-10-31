__author__ = 'austin'
import MySQLdb as mdb

con = mdb.connect('localhost', 'austin', 'chicken4wing', 'prdb')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Anthropometry LIMIT 5")

    rows = cur.fetchall()

    desc = cur.description

    print "%s %3s %4s" % (desc[0][0], desc[1][0], desc[2][0])



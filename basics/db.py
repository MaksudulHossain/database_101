import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("My commands")
res = cur.execute("My commands")
res.fetchall()

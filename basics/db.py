import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")
# res = cur.execute("SELECT * FROM movie")
# res.fetchall()

# make a table
# cur.execute("CREATE TABLE students(id, name, cgpa)")
res = cur.execute("SELECT * FROM students")
print(res.fetchall())

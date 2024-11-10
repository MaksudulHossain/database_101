# database_101
Learning database

## How to create a table in Python
```
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")
res = cur.execute("SELECT * FROM movie")
res.fetchall()
```

## How to create a table in SQL
```
CREATE TABLE movie(title, year, score)
SELECT * FROM movie
```



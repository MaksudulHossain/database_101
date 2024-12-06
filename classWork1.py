import sqlite3 
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

# cur.execute("CREATE TABLE Employees(EmployeeID INTEGER, Name TEXT, Position TEXT, Salary REAL)")

many_employees = [(1,'Alice','Manager',80000),
                  (2,'Bob','Developer',60000), 
                  (3,'Charlie','Tester',40000), 
                  (4,'Diana','Developer',60000),  
                  ]

cur.executemany("INSERT INTO Employees VALUES (?,?,?,?)", many_employees)


# cur.execute("ALTER TABLE employee1 RENAME TO employee1_old")

# cur.execute("""
# CREATE TABLE employee1 (
#     name TEXT,
#     age INTEGER,
#     salary REAL,
#     department TEXT,
#     ID INTEGER,
#     PRIMARY KEY (ID)
# )
# """
# )

# cur.execute("""
# INSERT INTO employee1 (name, age, salary, department, ID)
# SELECT name, age, salary, department, ID FROM employee1_old
# """        
# )

# cur.execute("""
# INSERT INTO employee1
# SELECT * FROM employee1_old
# """        
# )


# cur.execute("INSERT INTO employee1 VALUES ('Abul Kalam', 25, 5000, 'Fabrication', 5)")
# cur.execute("DROP TABLE employee1_old")

res = cur.execute("SELECT * FROM Employees")

con.commit()

print(res.fetchall())
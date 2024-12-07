import sqlite3

con = sqlite3.connect("Employees.db")

cur = con.cursor()

# Create the Employees table
cur.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY,
    Name TEXT,
    Position TEXT,
    Salary DECIMAL
)
''')

sample_data = [
    (1, 'Alice', 'Manager', 80000),
    (2, 'Bob', 'Developer', 60000),
    (3, 'Charlie', 'Tester', 40000),
    (4, 'Diana', 'Developer', 60000)
]

# cur.executemany("INSERT INTO Employees (EmployeeID, Name, Position, Salary) VALUES (?, ?, ?, ?)", sample_data)


# 1. Write an SQL query to find the average salary of employees in the `Developer` position. 
average_salary = cur.execute("SELECT AVG(Salary) FROM Employees WHERE position='Developer'")
print(average_salary.fetchall())

# 2. Write an SQL query to add a new employee with the following details: `EmployeeID = 5`, `Name = "Eve"`, `Position = "HR"`, `Salary = 50000`. 

# cur.execute("INSERT INTO Employees VALUES (5,'Eve', 'HR', 50000)")

# 3. Write an SQL query to update the salary of all employees in the `Tester` position to 45000.
cur.execute("""UPDATE Employees SET salary=45000
				WHERE position='Tester'
""")


con.commit()

res = cur.execute("SELECT * FROM Employees")
print(res.fetchall())
con.close()

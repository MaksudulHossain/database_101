import sqlite3

con = sqlite3.connect("Employees.db")

cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY,
    Name TEXT,
    Course TEXT,
    Grade DECIMAL
)
''')

sample_data = [
    (1, 'John', 'Mathematics', 'B'),
    (2, 'Sarah', 'Physics', 'A'),
    (3, 'Michael', 'Chemistry', 'C'),
    (4, 'Anna', 'Chemistry', 'A')
]

# cur.executemany("INSERT INTO Students (StudentID, Name, Course, Grade) VALUES (?, ?, ?, ?)", sample_data)

# 1. Write an SQL query to find all students enrolled in `Mathematics` who have achieved an `A` grade. 
# res = cur.execute("""SELECT * FROM Students
# WHERE Course='Mathematics' AND Grade='A'
# """)

# 2. Write an SQL query to add a new student with the following details: `StudentID = 5`, `Name = "Emily"`, `Course = "Biology"`, `Grade = "B"`.  
# cur.execute("INSERT INTO Students VALUES (5,'Emily', 'Biology', 'B')")


# 3. Write an SQL query to update the grade of the student `Michael` in `Chemistry` to `B`.
cur.execute("""UPDATE Students SET Grade = 'B'
				WHERE Name='Michael' AND Course='Chemistry'
""")

res = cur.execute("SELECT * FROM Students")
print(res.fetchall())

con.commit()
con.close()
import sqlite3

con = sqlite3.connect("Employees.db")

cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY,
    ProductName TEXT,
    Category TEXT,
    Price DECIMAL,
    Stock INTEGER
)
''')

sample_data = [
    (1, 'Laptop', 'Electronics', 1000, 50),
    (2, 'Chair', 'Furniture', 150, 200),
    (3, 'Smartphone', 'Electronics', 800, 30),
    (4, 'Desk', 'Furniture', 300, 100)
]

# cur.executemany("INSERT INTO Products (ProductID, ProductName, Category, Price, Stock) VALUES (?, ?, ?, ?, ?)", sample_data)

# 1. Write an SQL query to retrieve all `Electronics` products whose price is greater than 500.  
# res = cur.execute("SELECT * FROM Products WHERE Category='Electronics' AND Price > 500")
# res = cur.execute("SELECT * FROM Products WHERE Category='Electronics' AND Price > 500")
# products = res.fetchall()

# for product in products:
	# print(product[1])
	
# 2. Write an SQL query to reduce the stock of the product `Laptop` by 10 units. 
# cur.execute("""UPDATE Products SET Stock = Stock-10
				# WHERE ProductName='Laptop'
# """)
# res = cur.execute("SELECT * FROM Products")
# print(res.fetchall())

# 3. Write an SQL query to delete all `Furniture` products with a stock less than 100. 
cur.execute("DELETE FROM Products WHERE Category='Furniture' AND Stock<100")

res = cur.execute("SELECT * FROM Products")
print(res.fetchall())



con.commit()
con.close()


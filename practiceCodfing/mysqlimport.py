import mysql.connector

# Establishing a connection to the MySQL database
cnx = mysql.connector.connect(user='root', password='vicky2003', host='localhost', database='org')

# Creating a cursor object to execute SQL queries
cursor = cnx.cursor()

# Executing an SQL query
query = "SELECT * FROM bonus"
cursor.execute(query)

# Fetching all rows from the result set
result = cursor.fetchall()

# Printing the result
for row in result:
    print(row)

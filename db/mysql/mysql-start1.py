import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythontest1",
  password="pythontest1",
  database="training"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))") 
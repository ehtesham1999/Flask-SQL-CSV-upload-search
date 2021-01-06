import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shirin98@",
  database="buyitdb"
)


mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

# List All Databases
for x in mycursor:
  print(x)



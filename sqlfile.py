import mysql.connector
from datetime import date
import datetime

db = mysql.connector.connect(
    host = "192.168.1.33",
    user = "ehtesham",
    passwd = "Shirin98@",
    database = "test"
)

mycursor = db.cursor()
# sqlquery = "insert into cars (location,price,brand) values(%s,%s,%s)"
#sqlquery1 = "select * from cars"
# recordTuple = ("chennai india", 12312, "asdasd")

# print(mycursor.execute("SHOW DATABASES"))
# print(mycursor.fetchall())
# print(mycursor.execute(sqlquery,recordTuple))
# db.commit()
#mycursor.execute("select * from cars")

# for x in mycursor:
#     print(x)

import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="1234"
)

c = mydb.cursor()
c.execute("CREATE DATABASE PetrolPump_Management")
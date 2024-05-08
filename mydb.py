import mysql.connector as mysql 

database= mysql.connect(
    host= "localhost",
    user= "root",
    password= "vicky2003"
)

# This is a function in the above code
# This function is used to create a database
# We should create a cursor object that will allow us to execute all the MySQL commands

cursor= database.cursor()

cursor.execute("CREATE DATABASE elderco")

print("All done! Database created")
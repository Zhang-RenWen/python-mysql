import mysql.connector 
import settings
import os

DB_HOST = os.getenv("db_host")
DB_USER = os.getenv("db_user")
DB_PASSWORD = os.getenv("db_password")
DB_DATABASE = os.getenv("db_database")

mysql_connection = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_DATABASE)
cursor = mysql_connection.cursor()

cursor.execute("CREATE TABLE Students (StudentID int PRIMARY KEY, Name VARCHAR(255), City VARCHAR(255))")
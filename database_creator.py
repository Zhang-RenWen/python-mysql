import mysql.connector 
import settings
import os

DB_HOST = os.getenv("db_host")
DB_USER = os.getenv("db_user")
DB_PASSWORD = os.getenv("db_password")


mysql_connection = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cursor = mysql_connection.cursor()

cursor.execute("CREATE DATABASE PythonTest")
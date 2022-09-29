import mysql.connector 
import settings
import os

DB_HOST = os.getenv("db_host")
DB_USER = os.getenv("db_user")
DB_PASSWORD = os.getenv("db_password")
DB_DATABASE = os.getenv("db_database")


class DBManager:
    def __init__(self, user, password, host, database):
        self.mysql_connection = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self.cursor = self.mysql_connection.cursor()
    def insert_values(self, info):
        sql = "INSERT INTO Students (StudentID, Name, City) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, info)
        self.mysql_connection.commit()
    def show_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        values = self.cursor.fetchall()
        for value in values:
            print(value)

db_manager = DBManager(DB_USER, DB_PASSWORD, DB_HOST, DB_DATABASE)
# Insert new students
values = [
    (8, 'Frank', 'Beijing'),
    (9, 'Alice', 'Tokyo'),
]
for value in values:
    db_manager.insert_values(value)
# Check students
db_manager.show_data("Students")
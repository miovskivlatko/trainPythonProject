import mysql.connector
from mysql.connector import Error


class DBConnection:
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print(f'Connected to MySQL database: {self.database}')
        except Error as e:
            print(f'Error while connecting to MySQL: {e}')
            raise

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print('MySQL connection closed')

    def execute_query(self, query: str):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f'Error executing query: {e}')
            raise
        finally:
            cursor.close()
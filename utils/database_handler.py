import sqlite3
from config import DATABASE_FILENAME 
from logging import Handler
from utils.exceptions import *


class DatabaseHandler:
    def __init__(self, database_filename):
        self.conn = sqlite3.connect(database_filename)
        self.cursor = self.conn.cursor()

    def emit(self):
        pass

    def register_user(self, data):
        # name, surname, birthday, gender, post
        columns_count = 5

        if len(data) < columns_count:
            raise InvalidDataStruct('Invalid columns count is {len(data)}')

        self.cursor.execute("INSERT INTO users (name, surname, birthday, gender, post) "
                            "VALUES (?, ?, ?, ?, ?)", data)

    def __del__(self):
        self.conn.close()


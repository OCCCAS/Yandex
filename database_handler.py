import sqlite3
from exceptions import *


class DatabaseHandler:
    def __init__(self, database_filename):
        self.conn = sqlite3.connect(database_filename, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def emit(self):
        pass

    def register_user(self, data):
        try:
            post_name = data[5]
            post_id = self.cursor.execute('SELECT id FROM posts WHERE name=?', (post_name,)).fetchone()[0]
            data[5] = post_id

            self.cursor.execute(
                "INSERT INTO users (name, surname, email, birthday, gender, post, password) VALUES (?, ?, ?, ?, ?, ?, ?)", data)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        except Exception as e:
            print(e)
            return False

    def login_user(self, data):
        try:
            res = self.cursor.execute('SELECT * FROM users WHERE email=? AND password=?', data).fetchall()
            return res
        except Exception as e:
            print(e)
            return False


    def __del__(self):
        self.conn.close()

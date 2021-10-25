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
                "INSERT INTO users (name, surname, email, birthday, gender, post, password, portfolio_count) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", data)
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

    def get_user_data(self, email, column):
        try:
            res = self.cursor.execute(f'SELECT {column} FROM users WHERE email=?', (email, )).fetchone()
            return res[0]
        except Exception as e:
            print(e)
            return False

    def execute(self, command, params, commit=False):
        try:
            data =  self.cursor.execute(command, params).fetchall()

            if commit:
                self.conn.commit()
            else:
                return data

        except Exception as e:
            print(e)
            return False



    def __del__(self):
        self.conn.close()

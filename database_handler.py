import sqlite3
from exceptions import *


class DatabaseHandler:
    def __init__(self, database_filename):
        self.conn = sqlite3.connect(database_filename, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def emit(self):
        pass

    def __get_columns_name(self) -> list:
        return list(map(lambda item: item[1], self.cursor.execute('PRAGMA table_info(users)').fetchall()))

    def create_account(self, data):
        try:
            columns_name = self.__get_columns_name()
            self.cursor.execute(
                f"INSERT INTO users ({', '.join(columns_name)}) "
                f"VALUES ({', '.join(['?' * len(columns_name)])})", data)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        except Exception as e:
            print(e)
            return False

    def check_login_exists(self, email, password):
        try:
            data = self.cursor.execute('SELECT * FROM users WHERE email=? AND password=?',
                                       (email, password)).fetchone()

            return True if data else False
        except Exception as e:
            print(e)
            return False

    def get_user_data_by_column(self, column, email):
        try:
            data = self.cursor.execute(f'SELECT {column} FROM users WHERE email=?', (email,)).fetchone()[0]
            return data
        except Exception as e:
            print(e)
            return False

    def get_user_data_by_columns(self, columns, email):
        data = []
        for column_name in columns:
            data.append(self.get_user_data_by_column(column_name, email))

        return data

    def edit_user_data_by_column(self, column, new_data, email):
        try:
            self.cursor.execute(f'UPDATE users SET {column}=? WHERE email=?', (new_data, email))
            self.conn.commit()
        except Exception as e:
            print(e)
            return False

    def edit_user_data_by_columns(self, columns, new_data, email):
        if len(columns) != len(new_data):
            return

        for column, data_item in zip(columns, new_data):
            self.edit_user_data_by_column(column, data_item, email)

    def increase_portfolio_photo_count(self, email):
        self.cursor.execute('UPDATE users SET portfolio_count=portfolio_count + 1 WHERE email=?',
                            (email,))
        self.conn.commit()

    def add_portfolio_to_portfolios(self, user_email, competitions_name, place, date, photo):
        self.cursor.execute(
            'INSERT INTO portfolio (email, competitions_name, place, date, photo) VALUES(?, ?, ?, ?, ?)',
            (user_email, competitions_name, place, date, photo))
        self.conn.commit()

    def get_portfolio(self, email):
        return self.cursor.execute('SELECT * FROM portfolio WHERE email=?', (email, )).fetchall()

    def get_full_user_data(self, email):
        return self.cursor.execute('SELECT * FROM users WHERE email=?', (email, )).fetchone()[0]

    def __del__(self):
        self.conn.close()

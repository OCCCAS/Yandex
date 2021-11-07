import sqlite3
from typing import Union, List, Tuple


class DatabaseHandler:
    def __init__(self, database_filename):
        self.conn = sqlite3.connect(database_filename, check_same_thread=False)
        self.cursor = self.conn.cursor()
    
    def __get_columns_name(self) -> list:
        return list(map(lambda item: item[1], self.cursor.execute('PRAGMA table_info(users)').fetchall()))

    def create_account(self, data: Union[list, tuple]) -> bool:
        try:
            columns_name = self.__get_columns_name()
            self.cursor.execute(
                f"INSERT or REPLACE INTO users ({', '.join(columns_name[1:])}) "
                f"VALUES ({', '.join(['?'] * len(columns_name[1:]))})", data)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def check_login_exists(self, email: str, password: str) -> bool:
        data = self.cursor.execute('SELECT * FROM users WHERE email=? AND password=?',
                                   (email, password)).fetchone()
        return True if data else False

    def get_user_data_by_column(self, column: str, email: str) -> Union[list, tuple]:
        data = self.cursor.execute(f'SELECT {column} FROM users WHERE email=?', (email,)).fetchone()
        return data[0] if data else tuple()

    def get_user_data_by_columns(self, columns: Union[list, tuple], email: str) -> list:
        data = [self.get_user_data_by_column(column, email) for column in columns]
        return data

    def delete_profile(self, user_email: str) -> None:
        self.cursor.execute('DELETE FROM users WHERE email=?', (user_email, ))
        self.conn.commit()

    def edit_user_data_by_column(self, column: str, new_data: Union[str, int, float, bool], email: str) -> None:
        self.cursor.execute(f'UPDATE users SET {column}=? WHERE email=?', (new_data, email))
        self.conn.commit()

    def edit_user_data_by_columns(self, columns: Union[list, tuple], new_data: Union[list, tuple], email: str) -> None:
        if len(columns) != len(new_data):
            return

        for column, data_item in zip(columns, new_data):
            self.edit_user_data_by_column(column, data_item, email)

    def increase_portfolio_photo_count(self, email: str) -> None:
        self.cursor.execute('UPDATE users SET portfolio_count=portfolio_count + 1 WHERE email=?',
                            (email,))
        self.conn.commit()

    def add_portfolio_to_portfolios(self, user_email: str, competitions_name: str, place: str, date: int,
                                    photo: str) -> None:
        self.cursor.execute(
            'INSERT INTO portfolio (email, competitions_name, place, date, photo) VALUES(?, ?, ?, ?, ?)',
            (user_email, competitions_name, place, date, photo))
        self.conn.commit()

    def get_portfolio(self, email: str) -> list:
        return self.cursor.execute('SELECT * FROM portfolio WHERE email=?', (email,)).fetchall()

    def get_full_user_data(self, email: str) -> Union[list, tuple]:
        data = self.cursor.execute('SELECT * FROM users WHERE email=?', (email,)).fetchone()
        return data if data else tuple()

    def check_login_data_correctness(self, login_data: dict) -> bool:
        data = self.cursor.execute('SELECT password FROM users WHERE email=?', 
                (login_data.get('email'),)).fetchone()[0]
        return True if data and data == login_data.get('password') else False

    def create_task(self, title: str, text: str, date: int, photo: Union[str, None], class_: int) -> None:
        self.cursor.execute('INSERT INTO tasks (title, text, date, photo, class) VALUES(?, ?, ?, ?, ?)',
                            (title, text, date, photo, class_))
        self.conn.commit()

    def get_class_id_by_director_email(self, director_email):
        id_ = self.cursor.execute('SELECT id FROM classes WHERE director=(SELECT id FROM users WHERE email=?)',
                                  (director_email,)).fetchone()[0]
        return id_

    def get_tasks(self, user_email) -> List[Tuple]:
        return self.cursor.execute(
            """SELECT * FROM tasks WHERE class=(
                    SELECT class FROM users WHERE email=?
            )""", (user_email,)).fetchall()

    def get_post_id(self, post_name: str) -> int:
        data = self.cursor.execute('SELECT id FROM posts WHERE name=?', (post_name,)).fetchone()
        return data[0] if data else -1

    def get_children_list(self) -> list:
        # 2 - children post id
        return self.cursor.execute('SELECT * FROM users WHERE post=2').fetchall()

    def __is_class_created(self, director_email: str):
        data = self.cursor.execute(
                'SELECT * FROM classes WHERE director=(SELECT id FROM users WHERE email=?)', 
                (director_email, )).fetchone()
        return True if data else False

    def create_class(self, director_email: str, children_emails: List[str]) -> None:
        if not self.__is_class_created(director_email):
            self.cursor.execute("""INSERT or REPLACE INTO classes(director) 
                                VALUES((SELECT id FROM users WHERE email=?))""",
                                (director_email,))
            self.conn.commit()

        class_id = self.cursor.execute('SELECT id FROM classes WHERE '
                                       'director=(SELECT id FROM users WHERE email=?)',
                                       (director_email,)).fetchone()[0]
        for email in children_emails:
            self.cursor.execute('UPDATE users SET class=? WHERE email=?', (class_id, email))
        self.conn.commit()

    def get_class_by_director_email(self, director_email: str):
        return self.cursor.execute("""SELECT * FROM users WHERE class=(
            SELECT id FROM classes WHERE director=(
                SELECT id FROM users WHERE email=?
            )
        )""", (director_email,)).fetchall()

    def __del__(self):
        self.conn.close()

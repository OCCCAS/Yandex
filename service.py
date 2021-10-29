import shutil
import os
from database_handler import DatabaseHandler
import config
import json
from utils import *

database_handler_ = DatabaseHandler(config.DATABASE_PATH)


def is_user_created(email):
    data = database_handler_.execute('SELECT * FROM users WHERE email=?', (email,))
    return True if data else False


def create_local_avatar_file_name(email):
    return f'user.{email}.avatar.png'


def create_account(data):
    json_keys = ['name', 'surname', 'email', 'birthday', 'gender', 'password', 'portfolio_count', 'avatar_photo']
    json_ = {}

    if not is_user_created(data.get('email')):
        avatar_path = copy_avatar_photo(data.get('avatar_photo'), data.get('email'))
        data['avatar_photo'] = avatar_path

        for key in json_keys:
            json_[key] = data.get(key)

        database_handler_.execute(
            f'INSERT INTO users({", ".join(json_keys)}) '
            f'VALUES({", ".join(["?" for _ in range(len(json_keys))])})', list(json_.values()), commit=True)

        return True
    else:
        return False


def login(data):
    json_keys = ['email', 'password']
    json_ = {}

    for key in json_keys:
        json_[key] = data.get(key)

    res = database_handler_.login_user(list(json_.values()))

    if not res:
        return False

    return res[0]


def get_user_data(email, column_name):
    data = database_handler_.execute(f'SELECT {column_name} FROM users WHERE email=?', (email,))
    if data:
        return data[0][0]
    else:
        return ''


def get_current_user_email():
    with open('user.json', 'r') as json_:
        json_data = json.load(json_)
        json_.close()

    if 'user' in json_data:
        if 'email' in json_data['user']:
            return json_data['user']['email']

    return False


def copy_avatar_photo(file_name):
    user_email = hash_data(get_current_user_email())
    new_file_name = create_local_avatar_file_name(user_email)
    new_file_path = os.path.join(config.AVATARS_PATH, new_file_name)

    shutil.copyfile(file_name, new_file_path)

    return new_file_path


def save_current_user(data):
    data = {
        'user': {
            'email': data.get('email'),
        }
    }

    with open('user.json', 'w') as json_:
        json.dump(data, json_)
        json_.close()


def create_local_file_name():
    user_email = hash_data(get_current_user_email())
    photo_index = get_user_data(user_email, 'portfolio_count')
    return f'{user_email}_{photo_index}.png'


def copy_user_portfolio_photo(user_photo):
    new_file_name = create_local_file_name()
    new_file_path = os.path.join(config.PORTFOLIO_PATH, new_file_name)

    shutil.copyfile(user_photo, new_file_path)

    return new_file_path


def edit_profile(name, surname, gender, birthday, photo):
    user_email = get_current_user_email()
    photo = copy_avatar_photo(photo)
    database_handler_.execute('UPDATE users SET name=?, surname=?, gender=?, birthday=?, avatar_photo=? WHERE email=?',
                              (name, surname, gender, birthday, photo, user_email), commit=True)


def increase_photo_count():
    user_email = get_current_user_email()
    database_handler_.execute('UPDATE users SET portfolio_count=portfolio_count + 1 WHERE email=?',
                              (user_email,), commit=True)


def add_to_portfolio(competitions_name, place, date, photo):
    user_email = get_current_user_email()
    photo = copy_user_portfolio_photo(photo)
    increase_photo_count()

    try:
        database_handler_.execute(
            'INSERT INTO portfolio (email, competitions_name, place, date, photo) VALUES(?, ?, ?, ?, ?)',
            (user_email, competitions_name, place, date, photo), commit=True)

        return True
    except Exception as e:
        print(e)
        return False


def get_user_portfolio():
    user_email = get_current_user_email()
    data = database_handler_.execute('SELECT * FROM portfolio WHERE email=?', (user_email,))

    return data


def get_user_avatar_photo():
    user_email = get_current_user_email()
    return get_user_data(user_email, 'avatar_photo')


def get_all_user_data():
    user_email = get_current_user_email()
    data = database_handler_.execute('SELECT * FROM users WHERE email=?', (user_email,))[0]
    return data


def is_user_loggined():
    with open('user.json', 'r') as file:
        data = json.load(file)
        file.close()

    if 'user' in data:
        if 'email' in data['user']:
            return True

    return False

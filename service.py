from database_handler import DatabaseHandler
import config
import datetime
import json

database_handler_ = DatabaseHandler(config.DATABASE_PATH)


def create_account(data):
    json_keys = ['name', 'surname', 'email', 'birthday', 'gender', 'post', 'password', 'portfolio_count']
    json_ = {}

    for key in json_keys:
        json_[key] = data.get(key)

    res = database_handler_.register_user(list(json_.values()))

    return res


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
    data = database_handler_.get_user_data(email, column_name)

    if not data:
        return False

    return data


def get_current_user_email():
    with open('user.json', 'r') as json_:
        json_data = json.load(json_)
        json_.close()

    return json_data['user']['email']


def save_current_user(data):
    data = {
        'user': {
            'email': data.get('email')
        }
    }

    with open('user.json', 'w') as json_:
        json.dump(data, json_)
        json_.close()

from utils.database_handler import *
from config import DATABASE_FILENAME
from utils.database_handler import DatabaseHandler

from exceptions import InvalidDataStruct
from flask import jsonify

database_handler = DatabaseHandler(DATABASE_FILENAME)


class WebStatusCode:
    def __init__(self, json_: dict, status_code: int):
        self.__json = json_
        self.__status_code = status_code

    def get_formatted(self) -> tuple:
        return jsonify(self.__json), self.__status_code


def check_register_json(json):
    fields = {
        'name': str,
        'surname': str,
        'email': str,
        'birthday': int,
        'gender': str,
        'post': int,
        'password': str,
    }

    # Check data types and data fields
    for field_name, field_type in fields.items():
        # If field in json
        if field_name in json:
            # If field type is not good
            if not isinstance(json[field_name], field_type):
                return False
        else:
            return False

    return True


def web_error(message):
    return {'error': message}


def register(data):
    try:
        # If data fields count not valid 
        state = database_handler.register_user(data)

        if not state:
            raise UserWasRegistered('User was created')

        # If registration is seccsesfully
        name, surname = list(data)[:2]
        return WebStatusCode({
            'user': {
                'name': name,
                'surname': surname
            }
        }, 200)
    except InvalidDataStruct:
        # Returning 400 error code
        return WebStatusCode(web_error('Invalid data lenght'), 400)
    except UserWasRegistered:
        # Returning 400 error code
        return WebStatusCode(web_error('User was registered'), 400)



def login(username: str, password: str):
    try:
        pass
    except Exception:
        pass


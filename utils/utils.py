from utils.database_handler import *
from config import DATABASE_FILENAME
from utils.database_handler import DatabaseHandler

from utils.exceptions import InvalidDataStruct
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
        'birthday': int,
        'gender': str,
        'password': str,
    }

    # Check data types and data fields
    for field_name, field_type in fields.items():
        # If field in json
        if field_name in json:
            # If field type is good
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
        database_handler.register_user(data)

        # If good return 200 status code and user data
        return WebStatusCode({
            'user': {
                'name': data.get('name'),
                'surname': data.get('surname')
            }
        }, 200)
    except InvalidDataStruct:
        # Returning 400 error code
        return WebStatusCode(web_error('Invalid data lenght'), 400)

import shutil
import os
from typing import Union

from database_handler import DatabaseHandler
import config
import json
from utils import *

database_handler_ = DatabaseHandler(config.DATABASE_PATH)


# Check is user created account
def check_login_exists(data: dict) -> bool:
    data = database_handler_.check_login_exists(data.get('email'), data.get('password'))
    return True if data else False


# Creating file name for user avatar
def create_local_avatar_file_name(email: str) -> str:
    return f'user.{email}.avatar.png'


# Creating file name for user portfolio photo
def create_local_portfolio_file_name() -> str:
    user_email = hash_data(get_local_user_email())
    photo_index = get_user_data_by_column('portfolio_count', user_email)

    return f'{user_email}_{photo_index}.png'


# Creating account
def create_account(data: dict) -> bool:
    if not check_login_exists(data.get('email')):
        data['avatar_photo'] = copy_avatar_photo_to_local(data.get('avatar_photo'))

        database_handler_.create_account(list(data.values()))
        return True
    else:
        return False


# Get user info from column
def get_user_data_by_column(column: str, email: str) -> Union[int, float, str, bool]:
    data = database_handler_.get_user_data_by_column(column, email)
    return data if data else False


# Get user info from columns
def get_user_data_by_columns(columns: Union[list, tuple], email: str) -> Union[int, float, str, bool]:
    data = database_handler_.get_user_data_by_columns(columns, email)
    return data if data else False


# Check is user logged in in his computer
def is_user_logged_in_local() -> bool:
    with open('user.json', 'r') as file:
        data = json.load(file)
        file.close()

    if 'user' in data:
        if 'email' in data['user']:
            return True

    return False


# Get user email which logged in in this computer (local)
def get_local_user_email() -> Union[str, bool]:
    with open('user.json', 'r') as json_:
        json_data = json.load(json_)
        json_.close()

    if is_user_logged_in_local():
        return json_data['user']['email']

    return False


# Copy user avatar photo to application local path
def copy_avatar_photo_to_local(file_name: str) -> str:
    user_email = hash_data(get_local_user_email())
    new_file_name = create_local_avatar_file_name(user_email)
    new_file_path = os.path.join(config.AVATARS_PATH, new_file_name)

    shutil.copyfile(file_name, new_file_path)

    return new_file_path


# Copy user portfolio photo to application local path
def copy_portfolio_photo_to_local(file_name: str) -> str:
    new_file_name = create_local_portfolio_file_name()
    new_file_path = os.path.join(config.PORTFOLIO_PATH, new_file_name)

    shutil.copyfile(file_name, new_file_path)

    return new_file_path


# Save in local, that user is logged in
def save_current_user(data: dict) -> None:
    with open('user.json', 'w') as json_file:
        json.dump(
            {
                'user': {
                    'email': data.get('email'),
                }
            }, json_file)
        json_file.close()


# Edit profile
def edit_profile(name: str, surname: str, gender: str, birthday: int, photo: str) -> None:
    user_email = get_local_user_email()
    photo = copy_avatar_photo_to_local(photo)

    database_handler_.edit_user_data_by_columns(['name', 'surname', 'birthday', 'gender', 'photo'],
                                                [name, surname, birthday, gender, photo],
                                                user_email)


# Increase portfolio photo count (in database)
def increase_photo_count() -> None:
    user_email = get_local_user_email()
    database_handler_.increase_portfolio_photo_count(user_email)


# Add portfolio
def add_to_portfolio(competitions_name: str, place: str, date: int, photo: str) -> bool:
    user_email = get_local_user_email()
    photo = copy_portfolio_photo_to_local(photo)
    increase_photo_count()

    try:
        database_handler_.add_portfolio_to_portfolios(user_email, competitions_name, place, date, photo)
        return True
    except Exception as e:
        print(e)
        return False


# Get user portfolio
def get_user_portfolio() -> Union[list, tuple]:
    user_email = get_local_user_email()
    return database_handler_.get_portfolio(user_email)


# Get path to user avatar
def get_user_avatar_photo() -> str:
    user_email = get_local_user_email()
    return get_user_data_by_column('avatar_photo', user_email)


# Get full user data
def get_all_user_data() -> Union[list, tuple]:
    user_email = get_local_user_email()
    return database_handler_.get_full_user_data(user_email)


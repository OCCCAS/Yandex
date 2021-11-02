from typing import Union, List, Tuple

from database_handler import DatabaseHandler
from utils import *

import config
import json
import shutil
import os

database_handler_ = DatabaseHandler(config.DATABASE_PATH)


# Check is user created account
def check_login_exists(data: dict) -> bool:
    return database_handler_.check_login_exists(data.get('email'), data.get('password'))


# Creating file name for user avatar
def create_local_avatar_file_name() -> str:
    user_email = hash_data(get_local_user_email())
    return f'user.{user_email}.avatar.png'


# Creating file name for user portfolio photo
def create_local_portfolio_file_name() -> str:
    user_email = hash_data(get_local_user_email())
    photo_index = get_user_data_by_column('portfolio_count', user_email)
    photo_index = 0 if not photo_index else photo_index

    return f'{user_email}_{photo_index}.png'


# Create own user path
def create_user_path() -> None:
    user_email = hash_data(get_local_user_email())
    user_path = os.path.join(config.USERS_PATH, user_email)
    user_portfolio_path = os.path.join(user_path, 'portfolio')

    if not os.path.exists(user_path):
        os.mkdir(user_path)
        os.mkdir(user_portfolio_path)


# Creating account
def create_account(data: dict) -> bool:
    if not check_login_exists(data):
        save_current_user_to_local(data)
        create_user_path()
        data['avatar_photo'] = copy_avatar_photo_to_local(data.get('avatar_photo'))
        data['post'] = get_post_id(data['post'])

        created = database_handler_.create_account(list(data.values()))
        return created
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
    with open('user.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        file.close()

    if 'user' in data:
        if 'email' in data['user']:
            return True

    return False


# Get user email which logged in in this computer (local)
def get_local_user_email() -> Union[str, bool]:
    with open('user.json', 'r', encoding='utf-8') as json_:
        json_data = json.load(json_)
        json_.close()

    if is_user_logged_in_local():
        return json_data['user']['email']

    return False


# Copy user avatar photo to application local path
def copy_avatar_photo_to_local(file_name: str) -> str:
    user_email = hash_data(get_local_user_email())
    new_file_name = create_local_avatar_file_name()
    new_file_path = os.path.join(os.path.join(config.USERS_PATH, user_email), new_file_name)

    shutil.copyfile(file_name, new_file_path)

    return new_file_path


# Copy user portfolio photo to application local path
def copy_portfolio_photo_to_local(file_name: str) -> str:
    user_email = hash_data(get_local_user_email())
    user_portfolio_path = os.path.join(os.path.join(config.USERS_PATH, user_email), 'portfolio')

    new_file_name = create_local_portfolio_file_name()
    new_file_path = os.path.join(user_portfolio_path, new_file_name)

    shutil.copyfile(file_name, new_file_path)

    return new_file_path


# Save in local, that user is logged in
def save_current_user_to_local(data: dict) -> None:
    with open('user.json', 'w', encoding='utf-8') as json_file:
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

    database_handler_.edit_user_data_by_columns(['name', 'surname', 'birthday', 'gender', 'avatar_photo'],
                                                [name, surname, birthday, gender, photo],
                                                user_email)


# Increase portfolio photo count (in database)
def increase_photos_count() -> None:
    user_email = get_local_user_email()
    database_handler_.increase_portfolio_photo_count(user_email)


# Add portfolio
def add_to_portfolio(competitions_name: str, place: str, date: int, photo: str) -> bool:
    user_email = get_local_user_email()
    photo = copy_portfolio_photo_to_local(photo)
    increase_photos_count()

    database_handler_.add_portfolio_to_portfolios(user_email, competitions_name, place, date, photo)
    return True


# Get user portfolio
def get_user_portfolio() -> Union[list, tuple]:
    user_email = get_local_user_email()
    return database_handler_.get_portfolio(user_email)


# Get path to user avatar
def get_user_avatar_photo() -> str:
    user_email = get_local_user_email()
    return get_user_data_by_column('avatar_photo', user_email)


# Get full user data
def get_full_user_data() -> Union[list, tuple]:
    user_email = get_local_user_email()
    return database_handler_.get_full_user_data(user_email)


# Check login data correctness
def check_login_data_correctness(login_data: dict) -> bool:
    return database_handler_.check_login_data_correctness(login_data)


# Read program messages file, and return message
def get_filing_error_text(error_name: str) -> str:
    with open('program_messages.json', 'r', encoding='utf-8') as json_file:
        errors_message = json.load(json_file)
        json_file.close()

    if error_name in errors_message['errors_text']:
        return errors_message['errors_text'].get(error_name)
    else:
        return ''


# Load task to database
def create_task(title: str, text: str, date: int, photo: Union[str, None]) -> bool:
    database_handler_.create_task(title, text, date, photo)
    return True


# Get tasks
def get_tasks() -> List[Tuple]:
    return database_handler_.get_tasks()


# Get user post
def get_user_post_id():
    user_email = get_local_user_email()
    return get_user_data_by_column('post', user_email)


# Get post id from table, because post column is foreign key (table: posts)
def get_post_id(post_name):
    return database_handler_.get_post_id(post_name)

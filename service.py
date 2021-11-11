from typing import Union, List, Tuple

from database_handler import DatabaseHandler
from utils import *

import config
import json
import shutil
import os

database_handler_ = DatabaseHandler(config.DATABASE_PATH)


def check_login_exists(data: dict) -> bool:
    """Check is user created account"""
    return database_handler_.check_login_exists(data.get('email'), data.get('password'))


def create_local_avatar_file_name() -> str:
    """Creating file name for user avatar"""
    user_email = hash_data(get_local_user_email())
    return f'user.{user_email}.avatar.png'


def create_local_portfolio_file_name() -> str:
    """Creating file name for user portfolio photo"""
    user_email = hash_data(get_local_user_email())
    photo_index = get_user_data_by_column('portfolio_count', user_email)
    photo_index = 0 if not photo_index else photo_index

    return f'{user_email}_{photo_index}.png'


def create_user_path() -> None:
    """Create own user path"""
    user_email = hash_data(get_local_user_email())
    user_path = os.path.join(config.USERS_PATH, user_email)
    user_portfolio_path = os.path.join(user_path, 'portfolio')

    if not os.path.exists(user_path):
        os.mkdir(user_path)
        os.mkdir(user_portfolio_path)


def create_account(data: dict) -> bool:
    """Creating account"""
    if not check_login_exists(data):
        save_current_user_to_local(data)
        create_user_path()
        data['avatar_photo'] = copy_avatar_photo_to_local(data.get('avatar_photo'))
        data['post'] = get_post_id(data['post'])

        created = database_handler_.create_account(list(data.values()))
        return created
    else:
        return False


def get_user_data_by_column(column: str, email: str) -> Union[int, float, str, bool]:
    """Get user info from column"""
    data = database_handler_.get_user_data_by_column(column, email)
    return data if data else False


def get_user_data_by_columns(columns: Union[list, tuple], email: str) -> Union[int, float, str, bool]:
    """Get user info from columns"""
    data = database_handler_.get_user_data_by_columns(columns, email)
    return data if data else False


def is_user_logged_in_local() -> bool:
    """Check is user logged in in his computer"""
    with open('user.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        file.close()

    if 'user' in data:
        if 'email' in data['user']:
            return True

    return False


def get_local_user_email() -> Union[str, bool]:
    """Get user email which logged in in this computer (local)"""
    with open('user.json', 'r', encoding='utf-8') as json_:
        json_data = json.load(json_)
        json_.close()

    if is_user_logged_in_local():
        return json_data['user']['email']

    return False


def copy_avatar_photo_to_local(file_name: str) -> str:
    """Copy user avatar photo to application local path"""
    user_email = hash_data(get_local_user_email())
    new_file_name = create_local_avatar_file_name()
    new_file_path = os.path.join(os.path.join(config.USERS_PATH, user_email), new_file_name)

    shutil.copyfile(file_name, new_file_path)

    return new_file_path


def copy_portfolio_photo_to_local(file_name: str) -> str:
    """Copy user portfolio photo to application local path"""
    user_email = hash_data(get_local_user_email())
    user_portfolio_path = os.path.join(os.path.join(config.USERS_PATH, user_email), 'portfolio')

    new_file_name = create_local_portfolio_file_name()
    new_file_path = os.path.join(user_portfolio_path, new_file_name)

    shutil.copyfile(file_name, new_file_path)

    return new_file_path


def save_current_user_to_local(data: dict) -> None:
    """Save in local, that user is logged in"""
    with open('user.json', 'w', encoding='utf-8') as json_file:
        json.dump(
            {
                'user': {
                    'email': data.get('email'),
                }
            }, json_file)
        json_file.close()

    create_user_path()


def edit_profile(name: str, surname: str, gender: str, birthday: int, photo: str) -> None:
    """Edit profile"""
    user_email = get_local_user_email()
    if photo:
        photo = copy_avatar_photo_to_local(photo)
    else:
        photo = get_user_avatar_photo()

    database_handler_.edit_user_data_by_columns(['name', 'surname', 'birthday', 'gender', 'avatar_photo'],
                                                [name, surname, birthday, gender, photo],
                                                user_email)


def delete_profile():
    """Delete user"""
    user_email = get_local_user_email()
    database_handler_.delete_profile(user_email)


def increase_photos_count() -> None:
    """Increase portfolio photo count (in database)"""
    user_email = get_local_user_email()
    database_handler_.increase_portfolio_photo_count(user_email)


def add_to_portfolio(competitions_name: str, place: str, date: int, photo: str) -> bool:
    """Add portfolio"""
    user_email = get_local_user_email()
    photo = copy_portfolio_photo_to_local(photo)
    increase_photos_count()
    database_handler_.add_portfolio_to_portfolios(user_email, competitions_name, place, date, photo)
    return True


def get_user_portfolio() -> Union[list, tuple]:
    """Get user portfolio"""
    user_email = get_local_user_email()
    return database_handler_.get_portfolio(user_email)


def get_user_avatar_photo() -> str:
    """Get path to user avatar"""
    user_email = get_local_user_email()
    file_name = get_user_data_by_column('avatar_photo', user_email)
        
    if not os.path.exists(file_name):
        file_name = config.DEFAULT_AVATAR_PATH

    return file_name

def get_full_user_data() -> Union[list, tuple]:
    """Get full user data"""
    user_email = get_local_user_email()
    return database_handler_.get_full_user_data(user_email)


def check_login_data_correctness(login_data: dict) -> bool:
    """Check login data correctness"""
    return database_handler_.check_login_data_correctness(login_data)


def get_static_interface_texts(name: str) -> str:
    """Read program messages file, and return messages"""
    with open('program_messages.json', 'r', encoding='utf-8') as json_file:
        errors_message = json.load(json_file)
        json_file.close()

    if name in errors_message['texts']:
        return errors_message['texts'].get(name)
    else:
        return ''


def create_task(title: str, text: str, date: int, photo: Union[str, None]) -> bool:
    """Load task to database"""
    user_email = get_local_user_email()
    class_ = database_handler_.get_class_id_by_director_email(user_email)
    database_handler_.create_task(title, text, date, photo, class_)
    return True


def get_tasks() -> List[Tuple]:
    """Get tasks"""
    user_email = get_local_user_email()
    return database_handler_.get_tasks(user_email)


def get_user_post_id() -> str:
    """Get user post"""
    user_email = get_local_user_email()
    return get_user_data_by_column('post', user_email)


def get_post_id(post_name: str) -> int:
    """Get post id from table, because post column is foreign key (table: posts)"""
    return database_handler_.get_post_id(post_name)


def get_children_list() -> list:
    """Get list of children (if post = 2)"""
    return database_handler_.get_children_list()


def create_class(children_email: List[str]) -> bool:
    """Create children class -> (insert or replace classes database and
    set class columns at children)"""
    user_email = get_local_user_email()
    database_handler_.create_class(user_email, children_email)
    return True


def get_class() -> list:
    """This method user for get children list from class by director email"""
    user_email = get_local_user_email()
    return database_handler_.get_class_by_director_email(user_email)


def exit_from_local():
    with open('user.json', 'w') as json_file:
        json.dump({}, json_file)
        json_file.close()

def delete_portfolio_item(data):
    user_email = get_local_user_email()
    competitions_name = data.get('competitions_name')
    place = data.get('place')
    datetime_ = data.get('datetime')
    database_handler_.delete_portfolio_item(user_email, competitions_name, place, datetime_)


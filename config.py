import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'database.db')
DEFAULT_AVATAR_PHOTO = 'default.user.png'
DEFAULT_AVATAR_PATH = os.path.join(os.path.join(BASE_DIR, 'images'), DEFAULT_AVATAR_PHOTO) 
USERS_PATH = os.path.join(BASE_DIR, 'users')


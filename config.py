import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'database.db')
PORTFOLIO_PATH = os.path.join(BASE_DIR, os.path.join('images', 'portfolio'))
AVATARS_PATH = os.path.join(BASE_DIR, os.path.join('images', 'avatars'))
DEFAULT_AVATAR_PHOTO = 'default.user.png'
DEFAULT_AVATAR_PATH = os.path.join(AVATARS_PATH, DEFAULT_AVATAR_PHOTO) 


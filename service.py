from database_handler import DatabaseHandler
import config


database_handler_ = DatabaseHandler(config.DATABASE_PATH)

def create_session():
    pass


def create_account(data):
    json_keys = ['name', 'surname', 'email', 'birthday', 'gender', 'post', 'password']
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


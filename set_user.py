import json


email_children = 'pavlov.timur556@yandex.ru'
email_teacher = 'email@email.ru'

choose = input('(t or c): ')

if choose in ['t', 'c']:
    data = {
        'user': {
        }
    }
    if choose == 't':
        email = email_teacher
    elif choose == 'c':
        email = email_children

    data['user']['email'] = email
    with open('user.json', 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()

    print('Done! User was swiched')


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
        print('Done! User was swiched')
        json_file.close()
else:
    print('Use:\n'
          '\t(t or c): t\n'
          '\tOR\n'
          '\t(t or c): c')


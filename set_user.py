#!/usr/bin/env python

import json
import sqlite3



conn = sqlite3.connect('database.db')
cur = conn.cursor()

choose = input('(t(teacher) or c(children)): ')

if choose in ['t', 'c']:
    data = {
        'user': {
        }
    }

    if choose == 't':
        res = cur.execute('SELECT email FROM users WHERE post=1').fetchall()
    elif choose == 'c':
        res = cur.execute('SELECT email FROM users WHERE post=2').fetchall()
        
    for i in range(len(res)):
        print(f'{i + 1}. {res[i][0]}')

    choose = int(input(f'num from range(1, {len(res)}): '))

    data['user']['email'] = res[choose - 1][0]
    with open('user.json', 'w') as json_file:
        json.dump(data, json_file)

        print('Done! User was swiched')

        json_file.close()
else:
    print('Use:\n'
          '\t(t or c): t\n'
          '\tOR\n'
          '\t(t or c): c')


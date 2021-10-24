import requests as r
import datetime


uri = 'http://127.0.0.1:5000/api/create_account'
session = r.Session()
# session.auth = ('Timur', '123')

data = {
    'nick': 'OCCCAS',
    'name': 'Timur',
    'surname': 'Pavlov',
    'birthday': int(datetime.datetime(2006, 3, 23, 0, 0, 0).timestamp()),
    'post': 1,
    'gender': 'M',
    'password': '123'
}
auth = session.post(uri, json=data)

if auth.status_code == 200:
    print(auth.json())
elif auth.status_code == 400:
    print(auth.json())


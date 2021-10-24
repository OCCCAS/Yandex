# API functions
- [Create account](#create_account)
- [Login](#login)

## <a name='create_account'></a> Create account
```python
import requests
import datetime

session = requests.Session()

data = {
    'name': 'Name',
    'surname': 'Surname',
    'birthday': int(datetime.datetime(2000, 1, 1, 0, 0, 0).timestamp()),
    'post': 1,
    'gender': 'M',
    'password': 'Hashed password'
}

response = session.post('http://127.0.0.1:5000/api/create_account', json=data)

if response.status_code == 200:
    print(response.json())
elif response.status_code == 400:
    print('Invalid data struct')
```

## <a name='login'></a> Login
```python
# Some code
```

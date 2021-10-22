#!venv/bin/python3
from flask import Flask, jsonify, make_response, request, abort
from flask_httpauth import HTTPBasicAuth
from utils.utils import *


app = Flask(__name__)
auth = HTTPBasicAuth()


# @auth.verify_password
# def verify_password(username, password):
#     if username in users:
#         if users[username] == password:
#             return username


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/api/create_account', methods=['POST'])
def create_account():
    # If json is empty
    if not request.json:
        return make_response(jsonify({'error': 'Json is empty'}), 400)
    # Checking fields for emptiness 
    elif not check_register_json(request.json):
        return make_response(jsonify({'error': 'Some fields is empty'}), 400)
    
    web_status_code: WebStatusCode = register(request.json.values()).get_formatted()
    return make_response(*web_status_code)



if __name__ == '__main__':
    app.run(debug=True)


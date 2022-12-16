from flask import request

def add_question():
    # validation du token
    token = request.headers.get('Authorization')
    payload = request.get_json()
    
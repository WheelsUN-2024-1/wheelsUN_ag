import requests
import json
import strawberry
import os
from src.utils.response_transformer import jsonToLogin, jsonToRegister, jsonToLogout

""" # Check if running in a Docker container
def is_running_in_docker():
    return os.path.exists('/.dockerenv')

# Set base URL based on environment
if is_running_in_docker():
    BASE_URL = 'http://wheelsunauth:8080'
else:
    BASE_URL = 'http://127.0.0.1:8080' """

BASE_URL = 'http://wheelsunauth:8080'
#REGISTER

def register(register):
    register_dict = strawberry.asdict(register)
    response = requests.post(f'{BASE_URL}/register', json=register_dict)
    register =jsonToRegister(response.content)
    return register
#LOGIN

def login(login):
    login_dict = strawberry.asdict(login)
    response = requests.post(f'{BASE_URL}/login', json=login_dict)
    login = jsonToLogin(response.content)
    return login

#LOGOUT
def logoutConn(token):
    response = requests.post(f'{BASE_URL}/logout', headers={'Authorization': f'Bearer {token}'})
    logout = jsonToLogout(response.content)
    return logout

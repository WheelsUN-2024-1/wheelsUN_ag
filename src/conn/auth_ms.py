import requests
import json
import strawberry
from src.utils.response_transformer import jsonToCreditCard, jsonToTransaction

BASE_URL = 'http://127.0.0.1:8080'


#REGISTER

def register(register):
    register_dict = strawberry.asdict(register)
    response = requests.post(f'{BASE_URL}/register', json=register_dict)
    register ="a" #jsonToRegister(response.content)
    return register
#LOGIN

def login(login):
    login_dict = strawberry.asdict(login)
    response = requests.post(f'{BASE_URL}/login', json=login_dict)
    login = "a" #jsonToLogin(response.content)
    return login


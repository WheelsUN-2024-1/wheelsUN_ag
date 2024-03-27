import requests
import json
import strawberry
from src.utils.response_transformer import jsonToCreditCard, jsonToTransaction

BASE_URL = 'http://127.0.0.1:3000'

#CREDITCARD
def get_creditcard_by_id(id):
    response = requests.get(f'{BASE_URL}/creditcard/get/{id}')
    creditcard = jsonToCreditCard(response.content)
    return creditcard

def create_creditcard(creditcard):
    creditcard_dict = strawberry.asdict(creditcard)
    response = requests.post(f'{BASE_URL}/creditcard/create', json=creditcard_dict)
    creditcard = jsonToCreditCard(response.content)
    return creditcard

def update_creditcard(id, creditcard):
    creditcard_dict = strawberry.asdict(creditcard)
    filtered_dict = {key: value for key, value in creditcard_dict.items() if value is not None}
    response = requests.put(f'{BASE_URL}/creditcard/put/{id}', json=filtered_dict)
    creditcard = jsonToCreditCard(response.content)
    return creditcard

#TRANSACTION

def get_transaction_by_id(id):
    response = requests.get(f'{BASE_URL}/transaction/get/{id}')
    transaction = jsonToTransaction(response.content)
    return transaction

def create_transaction(transaction):
    transaction_dict = strawberry.asdict(transaction)
    response = requests.post(f'{BASE_URL}/transaction/create', json=transaction_dict)
    transaction = jsonToTransaction(response.content)
    return transaction
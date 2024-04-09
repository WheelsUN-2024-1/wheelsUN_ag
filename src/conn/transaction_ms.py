import requests
import json
import strawberry
from src.utils.response_transformer import jsonToCreditCard, jsonToTransaction
from src.models.transactions import Transaction_model

BASE_URL = 'https://127.0.0.1:3000'

#CREDITCARD
def get_creditcard_by_id(id):
    response = requests.get(f'{BASE_URL}/creditcard/get/{id}', verify=False)
    creditcard = jsonToCreditCard(response.content)
    return creditcard

def create_creditcard(creditcard):
    creditcard_dict = strawberry.asdict(creditcard)
    response = requests.post(f'{BASE_URL}/creditcard/create', json=creditcard_dict, verify=False)
    creditcard = jsonToCreditCard(response.content)
    return creditcard

def update_creditcard(id, creditcard):
    creditcard_dict = strawberry.asdict(creditcard)
    filtered_dict = {key: value for key, value in creditcard_dict.items() if value is not None}
    response = requests.put(f'{BASE_URL}/creditcard/put/{id}', json=filtered_dict, verify=False)
    creditcard = jsonToCreditCard(response.content)
    return creditcard

def delete_creditcard(id):
    response = requests.delete(f'{BASE_URL}/creditcard/delete/{id}', verify=False)
    creditcard = jsonToCreditCard(response.content)
    return creditcard

#TRANSACTION

def get_transaction_by_id(id):
    response = requests.get(f'{BASE_URL}/transaction/get/{id}', verify=False)
    transaction = jsonToTransaction(response.content)
    return transaction

def create_transaction(transaction):
    if type(transaction) == Transaction_model:
        transaction_dict = strawberry.asdict(transaction)
    else:
        transaction_dict = transaction
    response = requests.post(f'{BASE_URL}/transaction/create', json=transaction_dict, verify=False)
    print(response.content)
    transaction = jsonToTransaction(response.content)
    return transaction

def create_transaction_database(transaction):
    transaction_dict = strawberry.asdict(transaction)
    response = requests.post(f'{BASE_URL}/transaction/createdata', json= transaction_dict, verify=False)
    transaction = jsonToTransaction(response.content)
    return transaction
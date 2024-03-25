import requests
import strawberry
from src.utils.response_transformer import jsonToDrivers, jsonToDriver, jsonToPassengers, jsonToPassenger, jsonToString

BASE_URL = 'http://127.0.0.1:8000'

##DRIVER
def get_driver():
    response = requests.get(f'{BASE_URL}/driver')
    drivers = jsonToDrivers(response.content)
    return drivers

def get_driver_by_id(id):
    response = requests.get(f'{BASE_URL}/driver/{id}')
    driver = jsonToDriver(response.content)
    return driver

def create_driver(driver):
    driver_dict = strawberry.asdict(driver)
    response = requests.post(f'{BASE_URL}/driver', json=driver_dict)
    driver = jsonToDriver(response.content)
    return driver

def update_driver(id, driver):
    driver_dict = strawberry.asdict(driver)
    filtered_dict = {key: value for key, value in driver_dict.items() if value is not None}
    response = requests.patch(f'{BASE_URL}/driver/{id}', json=filtered_dict)
    #print(response.content)
    driver = jsonToDriver(response.content)
    return driver

def delete_driver(id):
    response = requests.delete(f'{BASE_URL}/driver/{id}')
    message = jsonToString(response.content)
    return message

##PASSENGER
def get_passenger():
    response = requests.get(f'{BASE_URL}/passenger')
    passengers = jsonToPassengers(response.content)
    return passengers

def get_passenger_by_id(id):
    response = requests.get(f'{BASE_URL}/passenger/{id}')
    passenger = jsonToPassenger(response.content)
    return passenger

def create_passenger(passenger):
    passenger_dict = strawberry.asdict(passenger)
    response = requests.post(f'{BASE_URL}/passenger', json=passenger_dict)
    passenger = jsonToPassenger(response.content)
    return passenger

def update_passenger(id, passenger):
    passenger_dict = strawberry.asdict(passenger)
    filtered_dict = {key: value for key, value in passenger_dict.items() if value is not None}
    response = requests.patch(f'{BASE_URL}/passenger/{id}', json=filtered_dict)
    #print(response.content)
    passenger = jsonToPassenger(response.content)
    return passenger

def delete_passenger(id):
    response = requests.delete(f'{BASE_URL}/passenger/{id}')
    message = jsonToString(response.content)
    return message

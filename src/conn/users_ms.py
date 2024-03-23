import requests
import json
import strawberry
from src.models.users import Driver_model
from src.utils.response_transformer import jsonToDrivers, jsonToDriver

BASE_URL = 'http://127.0.0.1:8000'

# Example GET request
def get_driver():
    response = requests.get(f'{BASE_URL}/driver')
    drivers = jsonToDrivers(response.content)
    return drivers

def get_driver_by_id(id):
    response = requests.get(f'{BASE_URL}/driver/{id}')
    driver = jsonToDriver(response.content)
    return driver

# Example POST request
def create_driver(driver):
    driver_dict = strawberry.asdict(driver)
    response = requests.post(f'{BASE_URL}/driver', json=driver_dict)
    driver = jsonToDriver(response.content)
    return driver

# Example PUT request
def update_driver(id, driver):
    driver_dict = strawberry.asdict(driver)
    filtered_dict = {key: value for key, value in driver_dict.items() if value is not None}
    response = requests.patch(f'{BASE_URL}/driver/{id}', json=filtered_dict)
    #print(response.content)
    driver = jsonToDriver(response.content)
    return driver

# Example DELETE request
def delete_driver(id):
    response = requests.delete(f'{BASE_URL}/driver/{id}')
    return response.status_code  # Returns HTTP status code


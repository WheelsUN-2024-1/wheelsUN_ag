import requests
import json
import strawberry
from src.models.users import Driver_model
from src.utils.response_transformer import jsonToDrivers, jsonToDriver, jsonToString

BASE_URL = 'http://127.0.0.1:8001'

# Example GET request
def get_trips():
    response = requests.get(f'{BASE_URL}/trip')
    drivers = jsonToDrivers(response.content)
    return drivers

def get_trip_by_id(id):
    response = requests.get(f'{BASE_URL}/trip/{id}')
    driver = jsonToDriver(response.content)
    return driver

# Example POST request
def create_trip(trip):
    driver_dict = strawberry.asdict(trip)
    response = requests.post(f'{BASE_URL}/trip', json=driver_dict)
    driver = jsonToDriver(response.content)
    return driver

# Example PUT request
def update_trip(id, trip):
    driver_dict = strawberry.asdict(driver)
    filtered_dict = {key: value for key, value in driver_dict.items() if value is not None}
    response = requests.put(f'{BASE_URL}/trip/{id}', json=filtered_dict)
    #print(response.content)
    driver = jsonToDriver(response.content)
    return driver

# Example PUT request
def add_passg_trip(id, trip):
    trip_dict = strawberry.asdict(trip)
    filtered_dict = {key: value for key, value in trip_dict.items() if value is not None}
    response = requests.put(f'{BASE_URL}/trip/add/{id}', json=filtered_dict)
    #print(response.content)
    driver = jsonToDriver(response.content)
    return driver

# Example PUT request
def remove_passg_trip(id, trip):
    trip_dict = strawberry.asdict(trip)
    filtered_dict = {key: value for key, value in trip_dict.items() if value is not None}
    response = requests.put(f'{BASE_URL}/trip/remove/{id}', json=filtered_dict)
    #print(response.content)
    driver = jsonToDriver(response.content)
    return driver


# Example DELETE request
def delete_trip(id):
    response = requests.delete(f'{BASE_URL}/trip/{id}')
    message = jsonToString(response.content)
    return message


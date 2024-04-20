import requests
import json
import strawberry
from src.utils.response_transformer import jsonToTrips, jsonToTrip, jsonToPredictions,jsonToCoordinates
from src.models.trip import TripPassenger
import os

# Check if running in a Docker container
def is_running_in_docker():
    return os.path.exists('/.dockerenv')

# Set base URL based on environment
if is_running_in_docker():
    BASE_URL = 'http://wheelsun_trip_ms:3002'
else:
    BASE_URL = 'http://127.0.0.1:3002'

# Example GET request
def get_trips():
    response = requests.get(f'{BASE_URL}/trip')
    trips = jsonToTrips(response.content)
    return trips

def get_trip_by_id(id):
    response = requests.get(f'{BASE_URL}/trip/{id}')
    trip = jsonToTrip(response.content)
    return trip

# Example POST request
def create_trip(trip):
    trip_dict = strawberry.asdict(trip)
    response = requests.post(f'{BASE_URL}/trip', json=trip_dict)
    trip = jsonToTrip(response.content)
    return trip

# Example PUT request
def update_trip(id, trip):
    trip_dict = strawberry.asdict(trip)
    filtered_dict = {key: value for key, value in trip_dict.items() if value is not None}
    response = requests.patch(f'{BASE_URL}/trip/{id}', json=filtered_dict)
    #print(response.content)
    trip = jsonToTrip(response.content)
    return trip

# Example PUT request
def add_passg_trip(id, trip):
    if type(trip) == TripPassenger:
        trip_dict = strawberry.asdict(trip)
    else:
        trip_dict = trip
    filtered_dict = {key: value for key, value in trip_dict.items() if value is not None}
    response = requests.patch(f'{BASE_URL}/trip/add/{id}', json=filtered_dict)
    trip = jsonToTrip(response.content)
    return trip

# Example PUT request
def remove_passg_trip(id, trip):
    trip_dict = strawberry.asdict(trip)
    filtered_dict = {key: value for key, value in trip_dict.items() if value is not None}
    response = requests.patch(f'{BASE_URL}/trip/remove/{id}', json=filtered_dict)
    trip = jsonToTrip(response.content)
    return trip


# Example DELETE request
def delete_trip(id):
    response = requests.delete(f'{BASE_URL}/trip/{id}')
    trip = jsonToTrip(response.content)
    return trip

def auto_complete(query):
    response = requests.get(f'{BASE_URL}/trip/places/{query}')
    predictions = jsonToPredictions(response.content)
    return predictions


def coordinates(place_id):
    response = requests.get(f'{BASE_URL}/trip/coord/{place_id}')
    coordinates = jsonToCoordinates(response.content)
    return coordinates
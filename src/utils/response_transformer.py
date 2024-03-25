import json
from typing import List

from src.models.users import Driver_model, Passenger_model

def jsonToString(content)->str:
    return json.loads(content.decode('utf-8'))

def jsonToDriver(content)->Driver_model:
    i = json.loads(content.decode('utf-8'))
    driver =  Driver_model(
        userAddress=i["userAddress"],
        userAge=i["userAge"],
        userCity=i["userCity"],
        userCountry=i["userCountry"],
        userEmail=i["userEmail"],
        userIdNumber=i["userIdNumber"],
        userLicenseExpirationDate=i["userLicenseExpirationDate"],
        userName=i["userName"],
        userPhone=i["userPhone"],
        userPostalCode=i["userPostalCode"],
        )
    
    return driver

def jsonToDrivers(content)->List[Driver_model]:
    data = json.loads(content.decode('utf-8'))
    drivers = []
    for i in data:
        driver =  Driver_model(
            userAddress=i["userAddress"],
            userAge=i["userAge"],
            userCity=i["userCity"],
            userCountry=i["userCountry"],
            userEmail=i["userEmail"],
            userIdNumber=i["userIdNumber"],
            userLicenseExpirationDate=i["userLicenseExpirationDate"],
            userName=i["userName"],
            userPhone=i["userPhone"],
            userPostalCode=i["userPostalCode"],
            )
        drivers.append(driver)
    return drivers

def jsonToPassenger(content)->Passenger_model:
    i = json.loads(content.decode('utf-8'))
    passenger =  Passenger_model(
        userAddress=i["userAddress"],
        userAge=i["userAge"],
        userCity=i["userCity"],
        userCountry=i["userCountry"],
        userEmail=i["userEmail"],
        userIdNumber=i["userIdNumber"],
        userName=i["userName"],
        userPhone=i["userPhone"],
        userPostalCode=i["userPostalCode"],
        )
    
    return passenger

def jsonToPassengers(content)->List[Passenger_model]:
    data = json.loads(content.decode('utf-8'))
    passengers = []
    for i in data:
        passenger =  Passenger_model(
            userAddress=i["userAddress"],
            userAge=i["userAge"],
            userCity=i["userCity"],
            userCountry=i["userCountry"],
            userEmail=i["userEmail"],
            userIdNumber=i["userIdNumber"],
            userName=i["userName"],
            userPhone=i["userPhone"],
            userPostalCode=i["userPostalCode"],
            )
        passengers.append(passenger)
    return passengers
import json
from typing import List

from src.models.users import Driver_model, Passenger_model
from src.models.vehicle import Vehicle_model
from src.models.trip import Trip
from src.models.transactions import Transaction_Response
from src.models.transactions import CreditCard_Response

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

def jsonToVehicles(content)->List[Vehicle_model]:
    data = json.loads(content.decode('utf-8'))
    vehicles = []
    for i in data:
        passenger =  Vehicle_model(
            vehicleOwnerId=i["vehicleOwnerId"],
            vehiclePlate=i["vehiclePlate"],
            vehicleBrand=i["vehicleBrand"],
            vehicleModel=i["vehicleModel"],
            vehicleCylinder=i["vehicleCylinder"],
            vehicleYear=i["vehicleYear"],
            vehicleSeatingCapacity=i["vehicleSeatingCapacity"]
            )
        vehicles.append(passenger)
    return vehicles

def jsonToVehicle(content)->Vehicle_model:
    i = json.loads(content.decode('utf-8'))
    passenger =  Vehicle_model(
            vehicleOwnerId=i["vehicleOwnerId"],
            vehiclePlate=i["vehiclePlate"],
            vehicleBrand=i["vehicleBrand"],
            vehicleModel=i["vehicleModel"],
            vehicleCylinder=i["vehicleCylinder"],
            vehicleYear=i["vehicleYear"],
            vehicleSeatingCapacity=i["vehicleSeatingCapacity"]
            )
    
    return passenger

def jsonToTrips(content)->List[Trip]:
    data = json.loads(content.decode('utf-8'))
    trips = []
    for i in data:
        print(i)
        trip =  Trip(
            id=i["_id"],
            route=i["route"],
            price=i["price"],
            vehicleId=i["vehicleId"],
            transactionIds=i["transactionIds"],
            currentState=i["currentState"],
            )
        trips.append(trip)
    return trips


def jsonToTrip(content)->Trip:
    i = json.loads(content.decode('utf-8'))   
        
    trip =  Trip(
        id=i["_id"],
        route=i["route"],
        price=i["price"],
        vehicleId=i["vehicleId"],
        transactionIds=i["transactionIds"],
        currentState=i["currentState"],
        waypoints=i["waypoints"]
        )

    return trip

def jsonToTransaction(content)->Transaction_Response:
    i = json.loads(content.decode('utf-8'))   
        
    transaction =  Transaction_Response(
        ID=i["ID"],
        CreatedAt=i["CreatedAt"],
        UpdatedAt=i["UpdatedAt"],
        DeletedAt=i["DeletedAt"],
        referenceCode=i["referenceCode"],
        description=i["description"],
        value=i["value"],
        paymentMethods=i["paymentMethods"],
        state=i["state"],
        TransactionIdPay=i["transactionIdPay"],
        orderId=i["orderId"],
        tripId=i["tripId"],
        creditCardId=i["creditCardId"]

        )

    return transaction

def jsonToCreditCard(content)->CreditCard_Response:
    i = json.loads(content.decode('utf-8'))   
        
    creditcard =  CreditCard_Response(
        ID=i["ID"],
        CreatedAt=i["CreatedAt"],
        UpdatedAt=i["UpdatedAt"],
        DeletedAt=i["DeletedAt"],
        creditCardId=i["creditCardId"],
        userId=i["userId"],
        number=i["number"],
        name=i["name"],
        securityCode=i["securityCode"],
        expirationDate=i["expirationDate"],
        )

    return creditcard
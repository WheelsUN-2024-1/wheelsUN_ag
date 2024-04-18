import strawberry
from typing import Optional
@strawberry.type
class Passenger_model:
    id:str
    userIdNumber: int
    userName: str
    userAge: int
    userEmail: str
    userPhone: str
    userAddress: str
    userCity: str
    userCountry: str
    userPostalCode: str

@strawberry.type
class Driver_model(Passenger_model):
    userLicenseExpirationDate: str

@strawberry.input
class Passenger_input:
    userIdNumber: int
    userName: str
    userAge: int
    userEmail: str
    userPhone: str
    userAddress: str
    userCity: str
    userCountry: str
    userPostalCode: str

@strawberry.input
class Driver_input(Passenger_input):
    userLicenseExpirationDate: str

@strawberry.input
class Passenger_patch:
    userName: Optional[str] = None
    userAge: Optional[int] = None
    userEmail: Optional[str] = None
    userPhone: Optional[str] = None
    userAddress: Optional[str] = None
    userCity: Optional[str] = None
    userCountry: Optional[str] = None
    userPostalCode: Optional[str] = None

@strawberry.input
class Driver_patch(Passenger_patch):
    userLicenseExpirationDate: Optional[str] = None

import strawberry
from typing import Optional, Union
from src.models.users import Driver_model, Passenger_model
@strawberry.input
class RegisterModel:
   userId: str
   password: str

@strawberry.type
class RegisterResponse:
   token:str
   message: str


@strawberry.input
class LoginModel:
   userId: str
   password: str

@strawberry.type
class LoginResponse:
   token:str
   message: str

@strawberry.type
class LoginResponseWithDriver(LoginResponse):
   driver:Driver_model

@strawberry.type
class LoginResponseWithPassenger(LoginResponse):
   passenger: Passenger_model

@strawberry.type
class LogoutResponse:
   message: str
import strawberry
from typing import Optional

@strawberry.input
class RegisterModel:
   username: str
   password: str
   firstName: str
   lastName:str

@strawberry.type
class RegisterResponse:
   # completar
   response: str


@strawberry.input
class LoginModel:
   username: str
   password: str

@strawberry.type
class LoginResponse:
   # completar
   response: str
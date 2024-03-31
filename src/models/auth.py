import strawberry
from typing import Optional

@strawberry.input
class RegisterModel:
   firstName: str
   lastName:str
   username: str
   password: str
   role:str

@strawberry.type
class RegisterResponse:
   token:str
   message: str


@strawberry.input
class LoginModel:
   username: str
   password: str

@strawberry.type
class LoginResponse:
   token:str
   message: str
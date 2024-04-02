import strawberry
from typing import Optional

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
class LogoutResponse:
   message: str
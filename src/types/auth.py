import strawberry
import typing
from src.conn.auth_ms import register, login, logoutConn
from src.models.auth import LoginModel, LoginResponse, RegisterModel, RegisterResponse, LogoutResponse
from strawberry.types import Info

    
@strawberry.type
class Query:
    @strawberry.field
    def hello(self, info: Info) -> str:
        return "Hello, world!"

@strawberry.type
class AuthMutation :
    @strawberry.mutation
    def register(self, info: Info, registerM:RegisterModel)->RegisterResponse:        
        return register(registerM)
    
    @strawberry.mutation
    def login(self, info: Info, loginM:LoginModel)->LoginResponse:        
        return login(loginM)
    
    @strawberry.mutation
    def logout(self, info: Info, token:str)->LogoutResponse:        
        return logoutConn(token)
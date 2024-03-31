import strawberry
import typing
from src.conn.auth_ms import register, login
from src.models.auth import LoginModel, LoginResponse, RegisterModel, RegisterResponse
from strawberry.types import Info

    
@strawberry.type
class AuthMutation :
    @strawberry.mutation
    def register(self, info: Info, registerM:RegisterModel)->RegisterResponse:        
        return register(registerM)
    
    @strawberry.mutation
    def login(self, info: Info, loginM:LoginModel)->LoginResponse:        
        return login(loginM)
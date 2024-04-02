import strawberry
import typing
from src.conn.users_ms import create_driver, create_passenger, get_driver_by_email, get_passenger_by_email
from src.models.users import Driver_model, Driver_input, Passenger_model, Passenger_input
from src.models.auth import LoginModel, LoginResponse, RegisterModel, RegisterResponse
from src.conn.auth_ms import register, login
from strawberry.types import Info

@strawberry.type
class AuthenticationMutation:
    @strawberry.mutation
    def createNewDriver(self, info: Info, driver:Driver_input, password: str)->RegisterResponse: 
        driverResonse = create_driver(driver)
        registerM = RegisterModel(userId=driverResonse.id, password=password)
        return register(registerM)
    
    @strawberry.mutation
    def createNewPassenger(self, info: Info, passenger:Passenger_input, password: str)->RegisterResponse:
        passengerResponse = create_passenger(passenger)
        registerM = RegisterModel(userId=passengerResponse.id, password=password)
        return register(registerM)
    
    @strawberry.mutation
    def driverLogin(self, info, email:str, password:str)->LoginResponse:
        driver = get_driver_by_email(email)
        loginM = LoginModel(userId=driver.id, password= password)
        return login(loginM)
    
    @strawberry.mutation
    def passengerLogin(self, info, email:str, password:str)->LoginResponse:
        passenger = get_passenger_by_email(email)
        loginM = LoginModel(userId=passenger.id, password= password)
        return login(loginM)
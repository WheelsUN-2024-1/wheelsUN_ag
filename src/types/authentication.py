import strawberry
import typing
from src.conn.users_ms import create_driver, create_passenger, get_driver_by_email, get_passenger_by_email
from src.models.users import Driver_model, Driver_input, Passenger_model, Passenger_input
from src.models.auth import LoginModel, LoginResponse, RegisterModel, RegisterResponse, LoginResponseWithDriver, LoginResponseWithPassenger
from src.conn.auth_ms import register, login
from strawberry.types import Info
from src.conn.ldap_ms import registerInLdap, userInLdap

@strawberry.type
class AuthenticationMutation:
    @strawberry.mutation
    def createNewDriver(self, info: Info, driver:Driver_input, password: str)->RegisterResponse: 
        #if(registerInLdap(driver.userName, True, password)):
            driverResponse = create_driver(driver)
            registerM = RegisterModel(userId=driverResponse.id, password=password)
            return register(registerM)
        #return RegisterResponse(message= "failed to create", token='')
        #print("failed to create driver:" + str(driver.userIdNumber))
    
    @strawberry.mutation
    def createNewPassenger(self, info: Info, passenger:Passenger_input, password: str)->RegisterResponse:
        #if(registerInLdap(passenger.userName, False, password)):
            passengerResponse = create_passenger(passenger)
            registerM = RegisterModel(userId=passengerResponse.id, password=password)
            return register(registerM)
        #print("failed to create passenger:" + str(passenger.userIdNumber))
    
    @strawberry.mutation
    def driverLogin(self, info, email:str, password:str)->LoginResponseWithDriver:
        driver = get_driver_by_email(email)
        #if(userInLdap(driver.userName,password, True)):
        loginM = LoginModel(userId=driver.id, password= password)
        loginResponse = login(loginM)
        loginResponseUser = LoginResponseWithDriver(message=loginResponse.message, token= loginResponse.token, driver=driver)
        return loginResponseUser
        #print("failed to auth driver:" + str(driver.userIdNumber))

    @strawberry.mutation
    def passengerLogin(self, info, email:str, password:str)->LoginResponseWithPassenger:
        passenger = get_passenger_by_email(email)
        #if(userInLdap(passenger.userName,password, False)):
        loginM = LoginModel(userId=passenger.id, password= password)
        loginResponse = login(loginM)
        loginResponseUser = LoginResponseWithPassenger(message=loginResponse.message, token= loginResponse.token, passenger=passenger)
        return loginResponseUser
        #print("failed to auth passenger:" + str(passenger.userIdNumber))
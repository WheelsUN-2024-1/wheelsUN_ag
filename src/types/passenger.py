import strawberry
import typing
from src.conn.users_ms import get_passenger, get_passenger_by_id, create_passenger, update_passenger, delete_passenger
from src.models.users import Passenger_model, Passenger_input, Passenger_patch
from strawberry.types import Info

@strawberry.type
class PassengerQuery:
    @strawberry.field
    def allPassengers(self, info: Info)->typing.List[Passenger_model]:
        return get_passenger()
   
    @strawberry.field
    def passengerById(self, info: Info, id:int)->Passenger_model:
        return get_passenger_by_id(id)
    
@strawberry.type
class PassengerMutation:
    @strawberry.mutation
    def createPassenger(self, info: Info, passenger:Passenger_input)->Passenger_model:        
        return create_passenger(passenger)
    
    @strawberry.mutation
    def updatePassenger(self, info, id:int, passenger:Passenger_patch)->Passenger_model:
        return update_passenger(id, passenger)
    
    @strawberry.mutation
    def deletePassenger(self, info, id:int)->str:
        return delete_passenger(id)
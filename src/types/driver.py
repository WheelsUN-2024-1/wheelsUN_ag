import strawberry
import typing
from src.conn.users_ms import get_driver, get_driver_by_id, create_driver, update_driver, delete_driver
from src.models.users import Driver_model, Driver_input, Driver_patch
from strawberry.types import Info

@strawberry.type
class Query:
    #allDrivers: typing.List[Driver_model] = strawberry.field(resolver= get_data)
    @strawberry.field
    def allDrivers(self, info: Info)->typing.List[Driver_model]:
        return get_driver()
   
    @strawberry.field
    def driverById(self, info: Info, id:int)->Driver_model:
        return get_driver_by_id(id)
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    def createDriver(self, info: Info, driver:Driver_input)->Driver_model:        
        return create_driver(driver)
    
    @strawberry.mutation
    def updateDriver(self, info, id:int, driver:Driver_patch)->Driver_model:
        return update_driver(id, driver)
    """
    #TODO
    @strawberry.mutation
    def deleteDriver(self, info, driver:Driver)->str:
        #return delete_data(driver)
        return "deleteDriver succesful" """
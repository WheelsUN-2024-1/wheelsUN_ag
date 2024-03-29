import strawberry
import typing
from src.conn.users_ms import get_vehicles, get_vehicle_by_plate, get_vehicle_by_id, create_vehicle, update_vehicle, delete_vehicle
from src.models.vehicle import Vehicle_model, Vehicle_input, Vehicle_patch
from strawberry.types import Info

@strawberry.type
class VehicleQuery:
    @strawberry.field
    def allVehicles(self, info: Info)->typing.List[Vehicle_model]:
        return get_vehicles()
   
    @strawberry.field
    def vehicleById(self, info: Info, id:int)->typing.List[Vehicle_model]:
        return get_vehicle_by_id(id)
    
    @strawberry.field
    def vehicleByPlate(self, info: Info, plate:str)->Vehicle_model:
        return get_vehicle_by_plate(plate)
    
@strawberry.type
class VehicleMutation:
    @strawberry.mutation
    def createVehicle(self, info: Info, vehicle:Vehicle_input)->Vehicle_model:        
        return create_vehicle(vehicle)
    
    @strawberry.mutation
    def updateVehicle(self, info, plate:str, vehicle:Vehicle_patch)->Vehicle_model:
        return update_vehicle(plate, vehicle)
    
    @strawberry.mutation
    def deleteVehicle(self, info, plate:str)->str:
        return delete_vehicle(plate)
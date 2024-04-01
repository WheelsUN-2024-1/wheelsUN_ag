import strawberry
import typing 
from typing import Optional
from src.conn.trip_ms import get_trips, get_trip_by_id, create_trip, update_trip, add_passg_trip, remove_passg_trip, delete_trip
from src.conn.join_trip import join_trip
from src.models.trip import Trip, TripInput, TripPassenger, TransactionID, TripPatch
from strawberry.types import Info
from src.messaging.new_task import push_notification

@strawberry.type
class TripQuery:
    @strawberry.field
    def allTrips(self, info: Info)->typing.List[Trip]:
        return get_trips()
   
    @strawberry.field
    def tripById(self, info: Info, id:str)->Trip:
        return get_trip_by_id(id)


@strawberry.type
class TripMutation:
    @strawberry.mutation
    def createTrip(self, info: Info, trip: TripInput)->Trip:     
        dict = {"message": "El viaje ha sido creado", 
                "inicio": trip.startingPoint,
                "final": trip.endingPoint,
                "precio": trip.price}
        push_notification(dict)   
        return create_trip(trip)
    
    @strawberry.mutation
    def deleteTrip(self, info, id:str)->Trip:
        return delete_trip(id)
    
    @strawberry.mutation
    def updateTrip(self, info, id:str, trip: TripPatch)->Trip:
        return update_trip(id, trip)

    @strawberry.mutation
    def addPassenger(self, info, id:str, trip: TripPassenger)->Trip:
        return add_passg_trip(id, trip)
    
    @strawberry.mutation
    def removePassenger(self, info, id:str, tx_id: TransactionID)->Trip:
        return remove_passg_trip(id,tx_id)
    
    @strawberry.mutation
    def joinTrip(self, info, id:str)->Trip:
        return join_trip(id)
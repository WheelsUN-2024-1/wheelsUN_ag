
import requests
import json
import strawberry
from src.models.transactions import Transaction_database
from src.conn.trip_ms import get_trip_by_id, add_passg_trip
from src.conn.transaction_ms import get_creditcard_by_id, create_transaction, create_transaction_database
from src.conn.users_ms import get_passenger_by_email
from src.utils.referenceCodeGenerator import generateString
from src.wheelsUN_mq.new_task import push_notification

TRIP_URL = 'http://127.0.0.1:3002'
TX_URL = 'https://127.0.0.1:3000'


# Example GET request
def join_trip(tripId,passengerEmail, creditCardId, stopPoint):

    passengerInfo = get_passenger_by_email(passengerEmail)
    referenceCodeGenerated = generateString()
    # get credit card
    responseCreditCard = get_creditcard_by_id(creditCardId)

    # get trip
    responseTrip = get_trip_by_id(tripId)


    json_tx = {

   "language": "es",

   "command": "SUBMIT_TRANSACTION",

   "merchant": {

      "apiKey": "4Vj8eK4rloUd272L48hsrarnUA",

      "apiLogin": "pRRXKOl8ikMmt9u"

   },

   "transaction": {

      "order": {

         "accountId": "512321",

         "referenceCode": referenceCodeGenerated,

         "description": "Payment test description",

         "language": "es",

         "signature": "1d6c33aed575c4974ad5c0be7c6a1c87",

         "notifyUrl": "http://www.payu.com/notify",

         "additionalValues": {

            "TX_VALUE": {

               "value": responseTrip.price,

               "currency": "COP"

         },

            "TX_TAX": {

               "value": responseTrip.price*1,

               "currency": "COP"

         },

            "TX_TAX_RETURN_BASE": {

               "value": 54622,

               "currency": "COP"

         }

         },

         "buyer": {

            "merchantBuyerId": "1",

            "fullName": passengerInfo.userName,

            "emailAddress": passengerInfo.userEmail,

            "contactPhone": passengerInfo.userPhone,

            "dniNumber": str(passengerInfo.userIdNumber),

            "shippingAddress": {

               "street1": passengerInfo.userAddress,

               "street2": "5555487",

               "city": passengerInfo.userCity,

               "state": "Bogotá D.C.",

               "country": "CO",

               "postalCode": passengerInfo.userPostalCode,

               "phone": str(passengerInfo.userPhone)

            }

         },

         "shippingAddress": {

            "street1": passengerInfo.userAddress,

            "street2": "5555487",

            "city": passengerInfo.userCity,

            "state": "Bogotá D.C.",

            "country": "CO",

            "postalCode": passengerInfo.userPostalCode,

            "phone": str(passengerInfo.userPhone)

         }

      },

      "payer": {

         "merchantPayerId": "1",

         "fullName": "First name and second payer name",

         "emailAddress": "payer_test@test.com",

         "contactPhone": "7563126",

         "dniNumber": "5415668464654",
         "dniType":"CC",
         "birthdate":"2002-02-21",
         "billingAddress": {

            "street1": "Cr 23 No. 53-50",

            "street2": "125544",

            "city": "Bogotá",

            "state": "Bogotá D.C.",

            "country": "CO",

            "postalCode": "000000",

            "phone": "7563126"

         }

      },

      "creditCard": {

         "number": responseCreditCard.number,

         "securityCode": responseCreditCard.securityCode,

         "expirationDate": responseCreditCard.expirationDate,

         "name": "APPROVED"

      },

      "extraParameters": {

         "INSTALLMENTS_NUMBER": 1

      },

      "type": "AUTHORIZATION_AND_CAPTURE",

      "paymentMethod": "VISA",

      "paymentCountry": "CO",

      "deviceSessionId": "vghs6tvkcle931686k1900o6e1",

      "ipAddress": "127.0.0.1",

      "cookie": "pt1t38347bs6jc9ruv2ecpv7o2",

      "userAgent": "Mozilla/5.0 (Windows NT 5.1; rv:18.0) Gecko/20100101 Firefox/18.0",

      "threeDomainSecure": {

         "embedded": False,

         "eci": "01",

         "cavv": "AOvG5rV058/iAAWhssPUAAADFA==",

         "xid": "Nmp3VFdWMlEwZ05pWGN3SGo4TDA=",

         "directoryServerTransactionId": "00000-70000b-5cc9-0000-000000000cb"

      }

   },

   "test": True

}
    
    
         
    # create transaction
    responseTransaction = create_transaction(json_tx)
    dict = {"message": "La transaccion ha sido creada", 
                "referenceCode":referenceCodeGenerated,
                "price": responseTrip.price
                }
    push_notification(dict) 
   
    tx_id = referenceCodeGenerated

    transaction = Transaction_database(
         referenceCode=tx_id,
         description="Payment test description",
         value=responseTrip.price,
         paymentMethods=json_tx["transaction"]["paymentMethod"],
         state="APPROVED",
         tripId=tripId,
         creditCardId=creditCardId
    )
    
    transaction_database = create_transaction_database(transaction)

       # create trip
    json_trip = {
        "transactionId": tx_id,
        "waypoint": stopPoint
    }

    
    tripResponse = add_passg_trip(tripId, json_trip)

    return tripResponse

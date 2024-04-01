
import requests
import json
import strawberry
from src.conn.trip_ms import get_trip_by_id, add_passg_trip
from src.conn.transaction_ms import get_creditcard_by_id, create_transaction


TRIP_URL = 'http://127.0.0.1:3002'
TX_URL = 'http://127.0.0.1:3000'


# Example GET request
def join_trip(tripId):
    userId = 456
    vehicleId = 2
    creditCardId = 1

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

         "referenceCode": "pruebita",

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

            "fullName": "First name and second buyer name",

            "emailAddress": "buyer_test@test.com",

            "contactPhone": "7563126",

            "dniNumber": "123456789",

            "shippingAddress": {

               "street1": "Cr 23 No. 53-50",

               "street2": "5555487",

               "city": "Bogotá",

               "state": "Bogotá D.C.",

               "country": "CO",

               "postalCode": "000000",

               "phone": "7563126"

            }

         },

         "shippingAddress": {

            "street1": "Cr 23 No. 53-50",

            "street2": "5555487",

            "city": "Bogotá",

            "state": "Bogotá D.C.",

            "country": "CO",

            "postalCode": "0000000",

            "phone": "7563126"

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

    tx_id = responseTransaction.referenceCode

    # create trip

    json_trip = {
        "transactionId": tx_id,
        "waypoint": "Nuestro Bogotá"
    }

    
    tripResponse = add_passg_trip(tripId, json_trip)

    return tripResponse

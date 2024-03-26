import strawberry

@strawberry.type
class TX_TAX_model:
    value : int
    currency : str

@strawberry.type
class TX_VALUE_model:
    value : int
    currency : str

@strawberry.type
class TX_TAX_RETURN_BASE_model:
    value : int
    currency : str

@strawberry.type
class AdditionalValues_model:
    TX_VALUE: TX_VALUE_model           
    TX_TAX: TX_TAX_model        
    TX_TAX_RETURN_BASE: TX_TAX_RETURN_BASE_model

@strawberry.type
class Address_model:
    street1 : str
    street2 : str
    city  : str
    state : str
    country : str
    postalCode: str
    phone : str

@strawberry.type
class Buyer_model:
    merchantBuyerID : str
    fullName : str    
    emailAddress : str    
    dniNumber: str      
    shippingAddress : Address_model

@strawberry.type
class CreditCardPay_model:
    number: str             
    securityCode: str       
    expirationDate: str     
    name:str               
    processWithoutCvv2: bool 

@strawberry.type
class ExtraParameters_model:
    installmentsNumber : int

@strawberry.type
class Merchant_model:
    apiLogin : str
    apiKey : str

@strawberry.type
class Order_model:
    accountId : str
    referenceCode : str
    description : str
    language : str
    notifyUrl : str
    partnerId : str
    signature : str
    shippingAddress : Address_model
    buyer : Buyer_model
    additionalValues : AdditionalValues_model

@strawberry.type
class Payer_model:
    emailAddress : str 
    merchantPayerID : str
    fullName : str
    billingAddress : Address_model
    birthdate : str
    contactPhone : str
    dniNumber : str
    dniType : str      

@strawberry.type
class PaymentMethod_model:
    language : str
    command : str
    test : bool
    merchant : Merchant_model

@strawberry.type
class TransactionPay_model:
    order: Order_model
    creditCard: CreditCardPay_model
    payer: Payer_model
    type : str
    paymentMethod : str
    paymentCountry: str
    deviceSessionId: str
    ipAddress : str
    cookie : str
    userAgent : str
    extraParameters : ExtraParameters_model

@strawberry.type
class RequestPayment_model:
    language : str
    command : str
    test : bool
    merchant : Merchant_model
    transaction : TransactionPay_model

@strawberry.type
class ThreeDomainSecure_model:
    embedded : bool
    eci : int
    xid : str
    cavv : str
    directoryServerTransactionId : str
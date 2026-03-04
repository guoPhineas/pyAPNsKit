import time,uuid,jwt
from pyAPNsKit.types import PushType

class APNsHeader(dict):
    def __init__(self,teamID:str,topic:str,keyID:str,p8Key:str,pushType:PushType,apns_collapse_id:str=None,apns_priority:str='10',apns_id:str=None,apns_expiration:str=None):
        '''
        Structure of APNs request header.

        **Parameters:**

        * **teamID** - The issuer key, the value for which is the 10-character Team ID you use for developing your company’s apps. Obtain this value from your developer account.
        * **topic** - The topic for the notification. In general, the topic is your app’s bundle ID/app ID.
        * **keyID** - The 10-character Key ID you obtained from your developer account.
        * **p8Key** - Used for JWT signature.
        * **pushType** - The value of this header must accurately reflect the contents of your notification’s payload. If there’s a mismatch, or if the header is missing on required systems, APNs may return an error, delay the delivery of the notification, or drop it altogether.
        * **apns_collapse_id** - *(optional)* An identifier you use to merge multiple notifications into a single notification for the user.
        * **apns_priority** - *(optional)* The priority of the notification. If you omit this header, APNs sets the notification priority to 10.
        * **apns_id** - *(optional)* A canonical UUID that’s the unique ID for the notification. If an error occurs when sending the notification, APNs includes this value when reporting the error to your server.
        * **apns_expiration** - *(optional)* The date at which the notification is no longer valid. This value is a UNIX epoch expressed in seconds (UTC).

        For more information, please check out [User Notifications](https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns) in Apple Developer Documentation.

        
        '''
        self.iat=int(time.time())
        self.keyID=keyID
        self.teamID=teamID
        self.p8Key=p8Key
        super().__init__()
        
        jwtSignature=self.genJwtSignature()

        self['authorization']=f"bearer {jwtSignature}"
        self['apns-push-type']=pushType.value
        self['apns-topic']=topic
        if apns_expiration: self['apns-id']=apns_id
        if apns_expiration: self['apns-expiration']=apns_expiration
        if apns_priority: self['apns-priority']=apns_priority
        if apns_collapse_id: self['apns-collapse-id']=apns_collapse_id

    def withAPNsCollapse(self,id:str):
        temp=self.copy()
        temp['apns-collapse-id']=id
        return temp
    
    def genJwtSignature(self)->str:
        self.iat=int(time.time())
        header={
            "alg" : "ES256",
            "kid" : self.keyID
        }

        payload={
            "iss": self.teamID,
            "iat": self.iat
        }

        return jwt.encode(payload,self.p8Key,headers=header)

    
    def refrashToken(self):
        '''
        Refrash Token
        '''
        jwtSignature=self.genJwtSignature()
        self['authorization']=f"bearer {jwtSignature}"

    


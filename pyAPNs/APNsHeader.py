import time,uuid,jwt
from pyAPNs.types import PushType

class APNsHeader(dict):
    def __init__(self,teamID:str,topic:str,keyID:str,p8Key:str,pushType:PushType,apns_collapse_id:str=None,apns_priority:str='10',apns_id:str=None,apns_expiration:str=None):
        super().__init__()
        header={
            "alg" : "ES256",
            "kid" : keyID
        }

        payload={
            "iss": teamID,
            "iat": int(time.time())
        }
        jwtSignature=jwt.encode(payload,p8Key,headers=header)

        self['authorization']=f"bearer {jwtSignature}"
        self['apns-push-type']=pushType.value
        self['apns-topic']=topic
        if apns_expiration: self['apns-id']=apns_id
        if apns_expiration: self['apns-expiration']=apns_expiration
        if apns_priority: self['apns-priority']=apns_priority
        if apns_collapse_id: self['apns-collapse-id']=apns_collapse_id

    def withAPNsCollapse(self,id:str):
        self['apns-collapse-id']=id
        return self
    


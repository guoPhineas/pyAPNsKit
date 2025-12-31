import time,uuid,jwt
from pyAPNs.enums import PushType

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

        self.setdefault('authorization',f"bearer {jwtSignature}")
        self.setdefault('apns-push-type',pushType.value)
        self.setdefault('apns-topic',topic)
        self.setdefault('apns-id',apns_id if apns_id else str(uuid.uuid4()))
        if apns_expiration: self.setdefault('apns-expiration',apns_expiration)
        if apns_priority: self.setdefault('apns-priority',apns_priority)
        if apns_collapse_id: self.setdefault('apns-collapse-id',apns_collapse_id)

from pyAPNs import APNsHeader,APNsBody
import httpx
from pyAPNs.helper import *


class apns:
    def __init__(self,teamID,keyID,p8Key,):
        pass
    def sendToDevice(deviceID,headers:APNsHeader,json:APNsBody,isSandbox=False)->bool:
        pass
        


def sendAPNsByDeviceID(deviceID,headers:APNsHeader.APNsHeader,json:APNsBody.APNsBody,isSandbox=False)->bool:
    with httpx.Client(http2=True) as client:
        apnsApi=''
        if isSandbox:
            apnsApi=sandboxEnvironment
        else:
            apnsApi=productEnvironment

        apnsApi=f'{apnsApi}/3/device/{deviceID}'

        response=client.post(url=apnsApi,json=json,headers=headers)
        (status_code,reason,apnsID)=checkResponse(response)

        if status_code==200:
            print('Success: ',status_code,reason,apnsID)
            return True
        else:
            print('Error: ',status_code,reason,apnsID)
            return False
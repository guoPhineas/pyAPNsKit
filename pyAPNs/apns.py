from pyAPNs import APNsHeader,APNsBody
import httpx
from pyAPNs import helper


class apns:
    def __init__(self,teamID,keyID,p8Key,):
        pass
    def sendToDevice(deviceID,headers:APNsHeader,json:APNsBody,isSandbox=False)->bool:
        pass
        


def sendAPNsByDeviceID(deviceID:str,headers:APNsHeader.APNsHeader,json:APNsBody.APNsBody,isSandbox=False)->bool:
    
    apnsApi=''
    if isSandbox:
        apnsApi=helper.sandboxEnvironment
    else:
        apnsApi=helper.productEnvironment

    apnsApi=f'{apnsApi}/3/device/{deviceID}'

    return helper.APNSRequest(apnsApi,json,headers)


def sendAPNsByDeviceID(deviceIDs:list[str],headers:APNsHeader.APNsHeader,json:APNsBody.APNsBody,isSandbox=False):
    
    apnsApi=''
    if isSandbox:
        apnsApi=helper.sandboxEnvironment
    else:
        apnsApi=helper.productEnvironment

    apnsApi=f'{apnsApi}/3/device/{deviceID}'

    for deviceID in deviceIDs:
        if not helper.APNSRequest(apnsApi,json,headers):
            print("Failed to send: ",deviceID)
    
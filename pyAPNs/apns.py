from pyAPNs import APNsHeader,APNsBody
import httpx
from pyAPNs import helper


def sendAPNsByDeviceID(deviceID:str,headers:APNsHeader.APNsHeader,json:APNsBody.APNsBody,isSandbox=False)->bool:
    
    apnsApi=''
    if isSandbox:
        apnsApi=helper.sandboxEnvironment
    else:
        apnsApi=helper.productEnvironment

    apnsApi=f'{apnsApi}/3/device/{deviceID}'

    return helper.APNSRequest(apnsApi,json,headers)


def sendAPNsByDeviceIDs(deviceIDs:list[str],headers:APNsHeader.APNsHeader,json:APNsBody.APNsBody,isSandbox=False):
    
    apnsApi=''
    if isSandbox:
        apnsApi=helper.sandboxEnvironment
    else:
        apnsApi=helper.productEnvironment

    apnsApi=f'{apnsApi}/3/device/'

    for deviceID in deviceIDs:
        url=apnsApi+deviceID
        failture=[]
        if not helper.APNSRequest(url,json,headers):
            failture.append(deviceID)
        if len(failture) != 0:
            print()
            print("Finished. But some sending failed: ",failture)
        else:
            print("Finished.")
        return failture
        
    
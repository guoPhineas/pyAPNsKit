from pyAPNsKit import APNsHeader,APNsBody,APNsResponse
from pyAPNsKit import helper,types
import httpx
import asyncio


def pushByDeviceToken(deviceTokens:str,headers:APNsHeader.APNsHeader|dict,json:APNsBody.APNsBody|dict,isSandbox=False)->APNsResponse.APNsResponse:
    '''
    Send APNs request via DeviceToken and return `APNsResponse`

    **Parameters:**

    * **deviceTokens** - DeviceToken
    * **headers** - `APNsHeader` or a `dict`
    * **json** - `APNsBody` or a `dict`
    * **isSandbox** - *(optional)* Whether to use a sandbox environment. Default is `False`

    '''
    apnsApi=''
    if isSandbox:
        apnsApi=helper.sandboxEnvironment
    else:
        apnsApi=helper.productEnvironment

    url=f'{apnsApi}/3/device/{deviceTokens}'

    return APNsResponse.APNsResponse(helper.Http2OnceRequest(url,json,headers))


async def asyncPushByDeviceTokens(deviceTokens:list[str],headers:APNsHeader.APNsHeader|dict,json:APNsBody.APNsBody|dict,isSandbox=False)->list[APNsResponse.APNsResponse]:
    '''
    Send APNs requests via DeviceToken and return `list[APNSResponse]`.
    **This method is asynchronous. **

    **Parameters:**

    * **deviceTokens** - `list[DeviceToken]`
    * **headers** - `APNsHeader` or a `dict`
    * **json** - `APNsBody` or a `dict`
    * **isSandbox** - *(optional)* Whether to use a sandbox environment. Default is `False`
    '''

    apnsApi=''
    if isSandbox:
        apnsApi=helper.sandboxEnvironment
    else:
        apnsApi=helper.productEnvironment

    urls=[f'{apnsApi}/3/device/{deviceID}' for deviceID in deviceTokens]

    responses=await helper.Http2ManyRequest(urls,json,headers)
    
    responses=[APNsResponse.APNsResponse(response) for response in responses]

    return responses


class Client:
    def __init__(self,teamID:str,topic:str,keyID:str,p8Key:str,isSandbox=False):
        self.teamID=teamID
        self.topic=topic
        self.keyID=keyID
        self.p8Key=p8Key
        self.isSandbox=isSandbox

    def sendAlert(self,deviceID:str,title:str,subtitle:str,message:str,sound:str|bool=None,apns_collapse_id:str=None)->bool:
        aPNsBody=APNsBody.APNsBody()\
                    .withAlert(title,subtitle,message)
        if not sound==None:
            if type(sound)==bool and sound:
                aPNsBody.withSound()
            elif type(sound)==str:
                aPNsBody.withSound(sound)
            
        return pushByDeviceToken(deviceID,
                           APNsHeader.APNsHeader(self.teamID,
                                                 self.topic,
                                                 self.keyID,
                                                 self.p8Key,
                                                 types.PushType.alert,
                                                 apns_collapse_id
                                                ),
                            aPNsBody,
                            self.isSandbox
                ).isSuccess

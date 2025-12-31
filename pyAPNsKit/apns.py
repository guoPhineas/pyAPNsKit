from pyAPNsKit import APNsHeader,APNsBody
from pyAPNsKit import helper,types
import httpx


def sendAPNsByDeviceID(deviceID:str,headers:APNsHeader.APNsHeader,json:APNsBody.APNsBody,isSandbox=False)->bool:
    
    apnsApi=''
    if isSandbox:
        apnsApi=helper.sandboxEnvironment
    else:
        apnsApi=helper.productEnvironment

    url=f'{apnsApi}/3/device/{deviceID}'

    with helper.Client(http2=True) as client:
        response=client.post(url=url,json=json,headers=headers)
        (status_code,reason,apnsID)=helper.checkResponse(response)

        if status_code==200:
            print('Success: ',status_code,reason,apnsID)
            return True
        else:
            print('Error: ',status_code,reason,apnsID)
            return False



def sendAPNsByDeviceIDs(deviceIDs:list[str],headers:APNsHeader.APNsHeader,json:APNsBody.APNsBody,isSandbox=False)->list[str]:
    with httpx.Client(http2=True) as client:
        apnsApi=''
        if isSandbox:
            apnsApi=helper.sandboxEnvironment
        else:
            apnsApi=helper.productEnvironment

        apnsApi=f'{apnsApi}/3/device/'
        failture=[]

        for deviceID in deviceIDs:
            response=client.post(url=apnsApi+deviceID,json=json,headers=headers)
            (status_code,reason,apnsID)=helper.checkResponse(response)

            if status_code!=200:
                print('Error: ',status_code,reason,apnsID)
                failture.append(deviceID)

    if len(failture) != 0:
        print("Finished. But some sending failed: ",failture)
    else:
        print("Finished.")
    return failture        


class Server:
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
            
        return sendAPNsByDeviceID(deviceID,
                           APNsHeader.APNsHeader(self.teamID,
                                                 self.topic,
                                                 self.keyID,
                                                 self.p8Key,
                                                 types.PushType.alert,
                                                 apns_collapse_id
                                                ),
                            aPNsBody,
                            self.isSandbox
                )

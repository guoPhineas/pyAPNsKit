from httpx import Response,Client

sandboxEnvironment='https://api.sandbox.push.apple.com'
productEnvironment='https://api.push.apple.com'

def checkResponse(response:Response)->tuple[int,str,str]:
    match response.status_code:
        case 200:
            return (200,'Success.',response.headers.get('apns-id'))

        case _:
            return (response.status_code,response.json().get('reason'),response.headers.get('apns-id'))

        
def APNSRequest(url,body,headers):
    with Client(http2=True) as client:
        response=client.post(url=url,json=body,headers=headers)
        (status_code,reason,apnsID)=checkResponse(response)

        if status_code==200:
            print('Success: ',status_code,reason,apnsID)
            return True
        else:
            print('Error: ',status_code,reason,apnsID)
            return False
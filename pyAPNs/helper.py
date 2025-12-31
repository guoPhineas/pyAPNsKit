from httpx import Response,Client

sandboxEnvironment='https://api.sandbox.push.apple.com'
productEnvironment='https://api.push.apple.com'

def checkResponse(response:Response)->tuple[int,str,str]:
    match response.status_code:
        case 200:
            return (200,'Success.',response.headers.get('apns-id'))

        case 400:
            return (400,response.json().get('reason'),response.headers.get('apns-id'))

        case 403:
            return (403,response.json().get('reason'),response.headers.get('apns-id'))

        case 404:
            return (404,response.json().get('reason'),response.headers.get('apns-id'))

        case 405:
            return (405,response.json().get('reason'),response.headers.get('apns-id'))

        case 410:
            return (410,response.json().get('reason'),response.headers.get('apns-id'))

        case 413:
            return (413,response.json().get('reason'),response.headers.get('apns-id'))

        case 429:
            return (429,response.json().get('reason'),response.headers.get('apns-id'))

        case 500:
            return (500,response.json().get('reason'),response.headers.get('apns-id'))

        case 503:
            return (503,response.json().get('reason'),response.headers.get('apns-id'))

        case _:
            return (-1,'Unknown.','','')
        
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
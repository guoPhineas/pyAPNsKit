from httpx import Response

class APNsResponse:
    def __init__(self,response:Response):
        '''
        Response to APNs service requests

        **Parameters:**

        * **response** - Response to http2 request
        
        '''
        self.status_code=response.status_code
        self.reason=response.json().get('reason') if self.status_code != 200 else "Success"
        self.apns_id=response.headers.get('apns-id')
        self.rawResponse=response

        self.isSuccess=self.status_code==200


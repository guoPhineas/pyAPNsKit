from httpx import Response,Client,AsyncClient
from pyAPNsKit import APNsResponse
import asyncio

sandboxEnvironment='https://api.sandbox.push.apple.com'
productEnvironment='https://api.push.apple.com'


def Http2OnceRequest(url,body,headers)->Response:
    '''
    A http2 request

    **Parameters:**

    * **url** - The requested URL
    * **body** - Request body for http2
    * **headers** - Request headers for http2
    '''
    with Client(http2=True) as client:
        response=client.post(url=url,json=body,headers=headers)
        return response
    
        
async def Http2ManyRequest(urls:list[str],body,headers)->list[Response]:
    '''
    Multiple http2 requests, asynchronous and multiplexed connection pool

    **Parameters:**

    * **urls** - The requested URL list
    * **body** - Request body for http2
    * **headers** - Request headers for http2

    '''
    async with AsyncClient(http2=True) as client:
        tasks=[client.post(url=url,json=body,headers=headers) for url in urls]
        responses = await asyncio.gather(*tasks)
        return responses

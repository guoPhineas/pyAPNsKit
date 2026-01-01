# pyAPNsKit

[简体中文](./docs/cn_zh.md)

> Send requests to Apple Push Notification service (APNs) to push notifications to users via HTTP/2, token-based



```Shell
pip install pyAPNsKit
```



## Get Started

Quickly push information to devices

```Python
from pyAPNsKit import apns

p8key=""
with open('AuthKey_KeyID.p8','r') as p8file:
    p8key=p8file.read()
client=apns.Client("teamID","App_BundleID","KeyID",p8key)
isSuccess=client.sendAlert('deviceToken','title','subtitle','message',sound=True)
```

> [!NOTE]
>
> For parameters, their acquisition methods, and instructions, please refer to the [Apple Developer Document](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server)



## Customized

```Python
from pyAPNsKit import apns,APNsHeader,APNsBody,types

p8key=""
with open('AuthKey_KeyID.p8','r') as p8file:
    p8key=p8file.read()

apnsHeader=APNsHeader.APNsHeader("teamID","topic","KeyID",p8key,types.PushType.alert)
isSuccess=apns.pushByDeviceToken('deviceToken',
               apnsHeader
                .withAPNsCollapse('Collapse')
               ,
               APNsBody.APNsBody()
                .withAlert("title","sub","message")
                .withSound()
             # ,isSandbox=True
)
```


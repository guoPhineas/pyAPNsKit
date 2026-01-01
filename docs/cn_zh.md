# pyAPNsKit

> 基于Token验证，通过HTTP/2向Apple APNs发送请求以向用户推送信息



```Shell
pip install pyAPNsKit
```



## 快速开始

快速向设备推送信息

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
> 对于参数及其获取方法与说明，请见[Apple Developer Document](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server)



## 自定义推送

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


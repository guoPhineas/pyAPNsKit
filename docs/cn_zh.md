# pyAPNs

> 向Apple APNs服务发送请求以向用户推送信息



## 快速开始

快速向设备推送信息

```Python
from pyAPNs import apns

p8key=""
with open('AuthKey_KeyID.p8','r') as p8file:
    p8key=p8file.read()
server=apns.Server("teamID","App_BundleID","KeyID",p8key)
isSuccess=server.sendAlert('deviceID','title','subtitle','message',sound=True)
```

> [!NOTE]
>
> 对于参数及其获取方法与说明，请见[Apple Developer Document](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server)



## 自定义推送

```Python
from pyAPNs import apns,APNsHeader,APNsBody,types

p8key=""
with open('AuthKey_KeyID.p8','r') as p8file:
    p8key=p8file.read()

apnsHeader=APNsHeader.APNsHeader("teamID","topic","KeyID",p8key,types.PushType.alert)
isSuccess=apns.sendAPNsByDeviceID('deviceID',
               apnsHeader
                .withAPNsCollapse('Collapse')
               ,
               APNsBody.APNsBody()
                .withAlert("title","sub","message")
                .withSound()
             # ,isSandbox=True
)
```


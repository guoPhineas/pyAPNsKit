# pyAPNsKit

> 基于Token验证，通过HTTP/2向Apple APNs发送请求以向用户推送信息



```Shell
pip install pyAPNsKit
```



## 快速开始

快速批量推送通知到设备（异步，支持批量）

```Python
import asyncio
from pyAPNsKit import apns

p8key = ""
with open('AuthKey_KeyID.p8', 'r') as p8file:
    p8key = p8file.read()

client = apns.Client("teamID", "topic", "KeyID", p8key, isSandbox=False)

async def main():
    responses = await client.sendAlert(
        ["deviceToken1", "deviceToken2"],  # 支持批量
        "title",
        "subtitle",
        "message",
        sound=True,
        apns_collapse_id="Collapse"
    )
    for resp in responses:
        print(resp.isSuccess, resp.status_code, resp.reason, resp.apns_id)

asyncio.run(main())
```

> [!NOTE]
>
> 对于参数及其获取方法与说明，请见[Apple Developer Document](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server)



## 自定义推送

```Python
p8key=""
apnsHeader=APNsHeader.APNsHeader("teamID","topic","KeyID",p8key,types.PushType.alert)
import asyncio
from pyAPNsKit import apns, APNsHeader, APNsBody, types

p8key = ""
with open('AuthKey_KeyID.p8', 'r') as p8file:
    p8key = p8file.read()

header = APNsHeader.APNsHeader(
    teamID="teamID",
    topic="topic",
    keyID="KeyID",
    p8Key=p8key,
    pushType=types.PushType.alert,
    apns_collapse_id="Collapse"
)
body = APNsBody.APNsBody().withAlert(
    title="title",
    subtitle="sub",
    message="message"
).withSound().withBadge(1)

async def main():
    responses = await apns.asyncPushByDeviceTokens(
        ["deviceToken1", "deviceToken2"],
        header,
        body,
        isSandbox=False
    )
    for resp in responses:
        print(resp.isSuccess, resp.status_code, resp.reason, resp.apns_id)

asyncio.run(main())
```


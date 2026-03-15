# pyAPNsKit

[简体中文](./docs/cn_zh.md)

> Send requests to Apple Push Notification service (APNs) to push notifications to users via HTTP/2, token-based


```Shell
pip install pyAPNsKit
```


## Get Started

Quickly push notifications to devices (async, batch supported)

```Python
import asyncio
from pyAPNsKit import apns

p8key = ""
with open('AuthKey_KeyID.p8', 'r') as p8file:
    p8key = p8file.read()

client = apns.Client("teamID", "topic", "KeyID", p8key, isSandbox=False)

async def main():
    responses = await client.sendAlert(
        ["deviceToken1", "deviceToken2"],  # support batch
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
> For parameters, their acquisition methods, and instructions, please refer to the [Apple Developer Document](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server)



## Customized

```Python

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


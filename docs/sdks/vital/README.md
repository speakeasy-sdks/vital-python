# Vital SDK


## Overview

Vital API: API for at-home health Wearables and Lab test API for digital health companies.

### Available Operations

* [robots_robots_txt_get](#robots_robots_txt_get) - Robots

## robots_robots_txt_get

Robots

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.vital.robots_robots_txt_get()

if res.robots_robots_txt_get_200_text_plain_string is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.RobotsRobotsTxtGetResponse](../../models/operations/robotsrobotstxtgetresponse.md)**


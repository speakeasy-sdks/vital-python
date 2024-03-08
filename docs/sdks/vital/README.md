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

s = vital.Vital()


res = s.robots_robots_txt_get()

if res.res is not None:
    # handle response
    pass

```


### Response

**[operations.RobotsRobotsTxtGetResponse](../../models/operations/robotsrobotstxtgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

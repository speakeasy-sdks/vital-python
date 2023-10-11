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


res = s.vital.robots_robots_txt_get()

if res.robots_robots_txt_get_200_text_plain_string is not None:
    # handle response
```


### Response

**[operations.RobotsRobotsTxtGetResponse](../../models/operations/robotsrobotstxtgetresponse.md)**


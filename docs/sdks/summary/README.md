# Summary
(*summary*)

### Available Operations

* [get_meals](#get_meals) - Get Meals
* [get_user_activity](#get_user_activity) - Get User Activity
* [get_user_activity_raw](#get_user_activity_raw) - Get User Activity Raw
* [get_user_body](#get_user_body) - Get User Body
* [get_user_body_raw](#get_user_body_raw) - Get User Body Raw
* [get_user_devices_raw](#get_user_devices_raw) - Get User Devices Raw
* [get_user_profile](#get_user_profile) - Get User Profile
* [get_user_profile_raw](#get_user_profile_raw) - Get User Profile Raw
* [get_user_sleep](#get_user_sleep) - Get User Sleep
* [get_user_sleep_raw](#get_user_sleep_raw) - Get User Sleep Raw
* [get_user_sleep_stream](#get_user_sleep_stream) - Get User Sleep Stream
* [get_user_workouts](#get_user_workouts) - Get User Workouts
* [get_user_workouts_raw](#get_user_workouts_raw) - Get User Workouts Raw
* [post_user_activity](#post_user_activity) - Post User Activity
* [post_user_body](#post_user_body) - Post User Body
* [post_user_profile](#post_user_profile) - Post User Profile
* [post_user_sleep](#post_user_sleep) - Post User Sleep
* [post_user_workout](#post_user_workout) - Post User Workout

## get_meals

Get user's meals

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_meals(start_date='string', user_id='641fb67c-c4de-44d2-8b5e-3e073000b0a5', end_date='string', provider='string')

if res.client_facing_meal_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00 |
| `user_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `end_date`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59      |
| `provider`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Provider oura/strava etc                                                                                                   |


### Response

**[operations.GetMealsV2SummaryMealUserIDGetResponse](../../models/operations/getmealsv2summarymealuseridgetresponse.md)**


## get_user_activity

Get Daily Activity for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_activity(start_date='string', user_id='29994eda-1c81-42f3-a33b-dcb5592eeffb', end_date='string', provider='string')

if res.client_activity_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00 |
| `user_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `end_date`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59      |
| `provider`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Provider oura/strava etc                                                                                                   |


### Response

**[operations.GetUserActivityV2SummaryActivityUserIDGetResponse](../../models/operations/getuseractivityv2summaryactivityuseridgetresponse.md)**


## get_user_activity_raw

Get Daily Activity for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_activity_raw(start_date='string', user_id='c752487b-77c7-4c61-ad1e-e885ef0bdc3c', end_date='string', provider='string')

if res.raw_activity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00 |
| `user_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `end_date`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59      |
| `provider`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Provider oura/strava etc                                                                                                   |


### Response

**[operations.GetUserActivityRawV2SummaryActivityUserIDRawGetResponse](../../models/operations/getuseractivityrawv2summaryactivityuseridrawgetresponse.md)**


## get_user_body

Get Daily Body data for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_body(start_date='string', user_id='8170daa1-c702-4d4a-9653-9a8a9e6e4eae', end_date='string', provider='string')

if res.client_body_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00 |
| `user_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `end_date`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59      |
| `provider`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Provider oura/strava etc                                                                                                   |


### Response

**[operations.GetUserBodyV2SummaryBodyUserIDGetResponse](../../models/operations/getuserbodyv2summarybodyuseridgetresponse.md)**


## get_user_body_raw

Get Daily Body data for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_body_raw(start_date='string', user_id='318730e0-1d99-4c94-97d6-8e72c1985489', end_date='string', provider='string')

if res.raw_body is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00 |
| `user_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `end_date`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59      |
| `provider`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Provider oura/strava etc                                                                                                   |


### Response

**[operations.GetUserBodyRawV2SummaryBodyUserIDRawGetResponse](../../models/operations/getuserbodyrawv2summarybodyuseridrawgetresponse.md)**


## get_user_devices_raw

Get Devices for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_devices_raw(user_id='d3afcead-cf24-4987-97fa-74fe26009852', provider='string')

if res.raw_devices is not None:
    # handle response
    pass
```

### Parameters

| Parameter                | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `user_id`                | *str*                    | :heavy_check_mark:       | N/A                      |
| `provider`               | *Optional[str]*          | :heavy_minus_sign:       | Provider oura/strava etc |


### Response

**[operations.GetUserDevicesRawV2SummaryDevicesUserIDRawGetResponse](../../models/operations/getuserdevicesrawv2summarydevicesuseridrawgetresponse.md)**


## get_user_profile

Get Daily profile for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_profile(user_id='1e03319e-ca0e-4660-8784-a0581ebdd19f', provider='string')

if res.client_facing_profile is not None:
    # handle response
    pass
```

### Parameters

| Parameter                | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `user_id`                | *str*                    | :heavy_check_mark:       | N/A                      |
| `provider`               | *Optional[str]*          | :heavy_minus_sign:       | Provider oura/strava etc |


### Response

**[operations.GetUserProfileV2SummaryProfileUserIDGetResponse](../../models/operations/getuserprofilev2summaryprofileuseridgetresponse.md)**


## get_user_profile_raw

Get Daily profile for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_profile_raw(user_id='ae101aa4-8797-4dc6-bac7-aa9d64e72a37', provider='string')

if res.raw_profile is not None:
    # handle response
    pass
```

### Parameters

| Parameter                | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `user_id`                | *str*                    | :heavy_check_mark:       | N/A                      |
| `provider`               | *Optional[str]*          | :heavy_minus_sign:       | Provider oura/strava etc |


### Response

**[operations.GetUserProfileRawV2SummaryProfileUserIDRawGetResponse](../../models/operations/getuserprofilerawv2summaryprofileuseridrawgetresponse.md)**


## get_user_sleep

Get Daily sleep for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_sleep(start_date='string', user_id='6a2ea429-e1c8-48ab-a43b-c6a94c896bba', end_date='string', provider='string')

if res.client_sleep_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00 |
| `user_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `end_date`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59      |
| `provider`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Provider oura/strava etc                                                                                                   |


### Response

**[operations.GetUserSleepV2SummarySleepUserIDGetResponse](../../models/operations/getusersleepv2summarysleepuseridgetresponse.md)**


## get_user_sleep_raw

Get Daily sleep for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_sleep_raw(start_date='string', user_id='b2ba77ed-68ff-441f-bfc0-77eae7285ab9', end_date='string', provider='string')

if res.raw_sleep is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00 |
| `user_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `end_date`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59      |
| `provider`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Provider oura/strava etc                                                                                                   |


### Response

**[operations.GetUserSleepRawV2SummarySleepUserIDRawGetResponse](../../models/operations/getusersleeprawv2summarysleepuseridrawgetresponse.md)**


## get_user_sleep_stream

Get Daily sleep stream for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_sleep_stream(start_date='string', user_id='8905f1c3-5295-4037-bc4a-b0890f30d313', end_date='string', provider='string')

if res.client_sleep_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00 |
| `user_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `end_date`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59      |
| `provider`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Provider oura/strava etc                                                                                                   |


### Response

**[operations.GetUserSleepStreamV2SummarySleepUserIDStreamGetResponse](../../models/operations/getusersleepstreamv2summarysleepuseridstreamgetresponse.md)**


## get_user_workouts

Get Daily workout for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_workouts(start_date='string', user_id='bc0edaf0-6098-41f4-a6eb-525d09cc6d26', end_date='string', provider='string')

if res.client_workout_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00 |
| `user_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `end_date`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59      |
| `provider`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Provider oura/strava etc                                                                                                   |


### Response

**[operations.GetUserWorkoutsV2SummaryWorkoutsUserIDGetResponse](../../models/operations/getuserworkoutsv2summaryworkoutsuseridgetresponse.md)**


## get_user_workouts_raw

Get Daily workout for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.get_user_workouts_raw(start_date='string', user_id='4853d653-58ad-48c0-b4b1-c219bac589e4', end_date='string', provider='string')

if res.raw_workout is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00 |
| `user_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `end_date`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59      |
| `provider`                                                                                                                 | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Provider oura/strava etc                                                                                                   |


### Response

**[operations.GetUserWorkoutsRawV2SummaryWorkoutsUserIDRawGetResponse](../../models/operations/getuserworkoutsrawv2summaryworkoutsuseridrawgetresponse.md)**


## post_user_activity

Post User Activity

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.post_user_activity(user_id='0e4724f5-d113-41c1-bf58-cd7168d06d0c', x_vital_android_sdk_version='string', x_vital_ios_sdk_version='string')

if res.response_post_user_activity_v2_summary_activity_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `user_id`                     | *str*                         | :heavy_check_mark:            | N/A                           |
| `x_vital_android_sdk_version` | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |
| `x_vital_ios_sdk_version`     | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |


### Response

**[operations.PostUserActivityV2SummaryActivityUserIDPostResponse](../../models/operations/postuseractivityv2summaryactivityuseridpostresponse.md)**


## post_user_body

Post User Body

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.post_user_body(user_id='2aac64a8-1a4b-47b9-b083-c6d33a9beb02', x_vital_android_sdk_version='string', x_vital_ios_sdk_version='string')

if res.response_post_user_body_v2_summary_body_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `user_id`                     | *str*                         | :heavy_check_mark:            | N/A                           |
| `x_vital_android_sdk_version` | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |
| `x_vital_ios_sdk_version`     | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |


### Response

**[operations.PostUserBodyV2SummaryBodyUserIDPostResponse](../../models/operations/postuserbodyv2summarybodyuseridpostresponse.md)**


## post_user_profile

Post User Profile

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.post_user_profile(user_id='343ee935-de73-408c-a15e-4782d3b864c4', x_vital_android_sdk_version='string', x_vital_ios_sdk_version='string')

if res.response_post_user_profile_v2_summary_profile_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `user_id`                     | *str*                         | :heavy_check_mark:            | N/A                           |
| `x_vital_android_sdk_version` | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |
| `x_vital_ios_sdk_version`     | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |


### Response

**[operations.PostUserProfileV2SummaryProfileUserIDPostResponse](../../models/operations/postuserprofilev2summaryprofileuseridpostresponse.md)**


## post_user_sleep

Post User Sleep

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.post_user_sleep(user_id='4332e922-db99-44ec-bd9d-77a063c520e5', x_vital_android_sdk_version='string', x_vital_ios_sdk_version='string')

if res.response_post_user_sleep_v2_summary_sleep_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `user_id`                     | *str*                         | :heavy_check_mark:            | N/A                           |
| `x_vital_android_sdk_version` | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |
| `x_vital_ios_sdk_version`     | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |


### Response

**[operations.PostUserSleepV2SummarySleepUserIDPostResponse](../../models/operations/postusersleepv2summarysleepuseridpostresponse.md)**


## post_user_workout

Post User Workout

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.summary.post_user_workout(user_id='63a9d635-f084-45f5-a781-131420d3a83b', x_vital_android_sdk_version='string', x_vital_ios_sdk_version='string')

if res.response_post_user_workout_v2_summary_workouts_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `user_id`                     | *str*                         | :heavy_check_mark:            | N/A                           |
| `x_vital_android_sdk_version` | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |
| `x_vital_ios_sdk_version`     | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |


### Response

**[operations.PostUserWorkoutV2SummaryWorkoutsUserIDPostResponse](../../models/operations/postuserworkoutv2summaryworkoutsuseridpostresponse.md)**


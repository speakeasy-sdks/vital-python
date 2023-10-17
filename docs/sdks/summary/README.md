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
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_meals(start_date='Money', user_id='fb67cc4d-e4d2-44b5-a3e0-73000b0a593d', end_date='whenever', provider='black')

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
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |


### Response

**[operations.GetMealsV2SummaryMealUserIDGetResponse](../../models/operations/getmealsv2summarymealuseridgetresponse.md)**


## get_user_activity

Get Daily Activity for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_activity(start_date='salmon', user_id='994eda1c-812f-4363-bbdc-b5592eeffbfe', end_date='sonata', provider='Fantastic')

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
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |


### Response

**[operations.GetUserActivityV2SummaryActivityUserIDGetResponse](../../models/operations/getuseractivityv2summaryactivityuseridgetresponse.md)**


## get_user_activity_raw

Get Daily Activity for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_activity_raw(start_date='turquoise', user_id='52487b77-c7c6-41ed-9ee8-85ef0bdc3cda', end_date='blah', provider='enforcement')

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
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |


### Response

**[operations.GetUserActivityRawV2SummaryActivityUserIDRawGetResponse](../../models/operations/getuseractivityrawv2summaryactivityuseridrawgetresponse.md)**


## get_user_body

Get Daily Body data for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_body(start_date='hack', user_id='70daa1c7-02d4-4a96-939a-8a9e6e4eae9b', end_date='magnetic', provider='local')

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
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |


### Response

**[operations.GetUserBodyV2SummaryBodyUserIDGetResponse](../../models/operations/getuserbodyv2summarybodyuseridgetresponse.md)**


## get_user_body_raw

Get Daily Body data for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_body_raw(start_date='Computer', user_id='8730e01d-99c9-4457-968e-72c19854893e', end_date='Credit', provider='South')

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
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |


### Response

**[operations.GetUserBodyRawV2SummaryBodyUserIDRawGetResponse](../../models/operations/getuserbodyrawv2summarybodyuseridrawgetresponse.md)**


## get_user_devices_raw

Get Devices for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_devices_raw(user_id='d3afcead-cf24-4987-97fa-74fe26009852', provider='Kwacha')

if res.raw_devices is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `provider`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Provider oura/strava etc                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetUserDevicesRawV2SummaryDevicesUserIDRawGetResponse](../../models/operations/getuserdevicesrawv2summarydevicesuseridrawgetresponse.md)**


## get_user_profile

Get Daily profile for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_profile(user_id='1e03319e-ca0e-4660-8784-a0581ebdd19f', provider='Unbranded')

if res.client_facing_profile is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `provider`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Provider oura/strava etc                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetUserProfileV2SummaryProfileUserIDGetResponse](../../models/operations/getuserprofilev2summaryprofileuseridgetresponse.md)**


## get_user_profile_raw

Get Daily profile for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_profile_raw(user_id='ae101aa4-8797-4dc6-bac7-aa9d64e72a37', provider='Liberia')

if res.raw_profile is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `provider`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Provider oura/strava etc                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetUserProfileRawV2SummaryProfileUserIDRawGetResponse](../../models/operations/getuserprofilerawv2summaryprofileuseridrawgetresponse.md)**


## get_user_sleep

Get Daily sleep for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_sleep(start_date='Pakistan', user_id='ea429e1c-88ab-4243-bc6a-94c896bba7aa', end_date='Southeast', provider='wireless')

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
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |


### Response

**[operations.GetUserSleepV2SummarySleepUserIDGetResponse](../../models/operations/getusersleepv2summarysleepuseridgetresponse.md)**


## get_user_sleep_raw

Get Daily sleep for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_sleep_raw(start_date='Titanium', user_id='ba77ed68-ff41-4f3f-8077-eae7285ab9bb', end_date='generate', provider='Point')

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
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |


### Response

**[operations.GetUserSleepRawV2SummarySleepUserIDRawGetResponse](../../models/operations/getusersleeprawv2summarysleepuseridrawgetresponse.md)**


## get_user_sleep_stream

Get Daily sleep stream for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_sleep_stream(start_date='quantify', user_id='05f1c352-9503-47bc-8ab0-890f30d313cc', end_date='Account', provider='Dakota')

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
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |


### Response

**[operations.GetUserSleepStreamV2SummarySleepUserIDStreamGetResponse](../../models/operations/getusersleepstreamv2summarysleepuseridstreamgetresponse.md)**


## get_user_workouts

Get Daily workout for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_workouts(start_date='Plutonium', user_id='0edaf060-981f-44a6-ab52-5d09cc6d2663', end_date='Recumbent', provider='next')

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
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |


### Response

**[operations.GetUserWorkoutsV2SummaryWorkoutsUserIDGetResponse](../../models/operations/getuserworkoutsv2summaryworkoutsuseridgetresponse.md)**


## get_user_workouts_raw

Get Daily workout for user_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.get_user_workouts_raw(start_date='Bike', user_id='65358ad8-c074-4b1c-a19b-ac589e4fc044', end_date='Auto', provider='Legacy')

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
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |


### Response

**[operations.GetUserWorkoutsRawV2SummaryWorkoutsUserIDRawGetResponse](../../models/operations/getuserworkoutsrawv2summaryworkoutsuseridrawgetresponse.md)**


## post_user_activity

Post User Activity

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.post_user_activity(user_id='0e4724f5-d113-41c1-bf58-cd7168d06d0c', x_vital_android_sdk_version='primary', x_vital_ios_sdk_version='tesla')

if res.response_post_user_activity_v2_summary_activity_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_vital_android_sdk_version`                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `x_vital_ios_sdk_version`                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.PostUserActivityV2SummaryActivityUserIDPostResponse](../../models/operations/postuseractivityv2summaryactivityuseridpostresponse.md)**


## post_user_body

Post User Body

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.post_user_body(user_id='2aac64a8-1a4b-47b9-b083-c6d33a9beb02', x_vital_android_sdk_version='dicta', x_vital_ios_sdk_version='Cambridgeshire')

if res.response_post_user_body_v2_summary_body_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_vital_android_sdk_version`                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `x_vital_ios_sdk_version`                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.PostUserBodyV2SummaryBodyUserIDPostResponse](../../models/operations/postuserbodyv2summarybodyuseridpostresponse.md)**


## post_user_profile

Post User Profile

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.post_user_profile(user_id='343ee935-de73-408c-a15e-4782d3b864c4', x_vital_android_sdk_version='purple', x_vital_ios_sdk_version='foreground')

if res.response_post_user_profile_v2_summary_profile_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_vital_android_sdk_version`                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `x_vital_ios_sdk_version`                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.PostUserProfileV2SummaryProfileUserIDPostResponse](../../models/operations/postuserprofilev2summaryprofileuseridpostresponse.md)**


## post_user_sleep

Post User Sleep

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.post_user_sleep(user_id='4332e922-db99-44ec-bd9d-77a063c520e5', x_vital_android_sdk_version='Tasty', x_vital_ios_sdk_version='South')

if res.response_post_user_sleep_v2_summary_sleep_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_vital_android_sdk_version`                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `x_vital_ios_sdk_version`                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.PostUserSleepV2SummarySleepUserIDPostResponse](../../models/operations/postusersleepv2summarysleepuseridpostresponse.md)**


## post_user_workout

Post User Workout

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.summary.post_user_workout(user_id='63a9d635-f084-45f5-a781-131420d3a83b', x_vital_android_sdk_version='compress', x_vital_ios_sdk_version='Unbranded')

if res.response_post_user_workout_v2_summary_workouts_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_vital_android_sdk_version`                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `x_vital_ios_sdk_version`                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.PostUserWorkoutV2SummaryWorkoutsUserIDPostResponse](../../models/operations/postuserworkoutv2summaryworkoutsuseridpostresponse.md)**


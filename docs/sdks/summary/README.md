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

req = operations.GetMealsV2SummaryMealUserIDGetRequest(
    start_date='Steel relative',
    user_id='67cc4de4-d24b-45e3-a073-000b0a593dec',
)

res = s.summary.get_meals(req)

if res.client_facing_meal_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetMealsV2SummaryMealUserIDGetRequest](../../models/operations/getmealsv2summarymealuseridgetrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetMealsV2SummaryMealUserIDGetResponse](../../models/operations/getmealsv2summarymealuseridgetresponse.md)**


## get_user_activity

Get Daily Activity for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserActivityV2SummaryActivityUserIDGetRequest(
    start_date='unde',
    user_id='94eda1c8-12f3-4633-bdcb-5592eeffbfef',
)

res = s.summary.get_user_activity(req)

if res.client_activity_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetUserActivityV2SummaryActivityUserIDGetRequest](../../models/operations/getuseractivityv2summaryactivityuseridgetrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetUserActivityV2SummaryActivityUserIDGetResponse](../../models/operations/getuseractivityv2summaryactivityuseridgetresponse.md)**


## get_user_activity_raw

Get Daily Activity for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserActivityRawV2SummaryActivityUserIDRawGetRequest(
    start_date='HEX black indexing',
    user_id='b77c7c61-ed1e-4e88-9ef0-bdc3cdae1f4a',
)

res = s.summary.get_user_activity_raw(req)

if res.raw_activity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.GetUserActivityRawV2SummaryActivityUserIDRawGetRequest](../../models/operations/getuseractivityrawv2summaryactivityuseridrawgetrequest.md) | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |


### Response

**[operations.GetUserActivityRawV2SummaryActivityUserIDRawGetResponse](../../models/operations/getuseractivityrawv2summaryactivityuseridrawgetresponse.md)**


## get_user_body

Get Daily Body data for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserBodyV2SummaryBodyUserIDGetRequest(
    start_date='Northwest West',
    user_id='aa1c702d-4a96-4539-a8a9-e6e4eae9b476',
)

res = s.summary.get_user_body(req)

if res.client_body_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.GetUserBodyV2SummaryBodyUserIDGetRequest](../../models/operations/getuserbodyv2summarybodyuseridgetrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.GetUserBodyV2SummaryBodyUserIDGetResponse](../../models/operations/getuserbodyv2summarybodyuseridgetresponse.md)**


## get_user_body_raw

Get Daily Body data for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserBodyRawV2SummaryBodyUserIDRawGetRequest(
    start_date='Southeast',
    user_id='730e01d9-9c94-457d-a8e7-2c19854893e6',
)

res = s.summary.get_user_body_raw(req)

if res.raw_body is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetUserBodyRawV2SummaryBodyUserIDRawGetRequest](../../models/operations/getuserbodyrawv2summarybodyuseridrawgetrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetUserBodyRawV2SummaryBodyUserIDRawGetResponse](../../models/operations/getuserbodyrawv2summarybodyuseridrawgetresponse.md)**


## get_user_devices_raw

Get Devices for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserDevicesRawV2SummaryDevicesUserIDRawGetRequest(
    user_id='d3afcead-cf24-4987-97fa-74fe26009852',
)

res = s.summary.get_user_devices_raw(req)

if res.raw_devices is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.GetUserDevicesRawV2SummaryDevicesUserIDRawGetRequest](../../models/operations/getuserdevicesrawv2summarydevicesuseridrawgetrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.GetUserDevicesRawV2SummaryDevicesUserIDRawGetResponse](../../models/operations/getuserdevicesrawv2summarydevicesuseridrawgetresponse.md)**


## get_user_profile

Get Daily profile for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserProfileV2SummaryProfileUserIDGetRequest(
    user_id='1e03319e-ca0e-4660-8784-a0581ebdd19f',
)

res = s.summary.get_user_profile(req)

if res.client_facing_profile is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetUserProfileV2SummaryProfileUserIDGetRequest](../../models/operations/getuserprofilev2summaryprofileuseridgetrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetUserProfileV2SummaryProfileUserIDGetResponse](../../models/operations/getuserprofilev2summaryprofileuseridgetresponse.md)**


## get_user_profile_raw

Get Daily profile for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserProfileRawV2SummaryProfileUserIDRawGetRequest(
    user_id='ae101aa4-8797-4dc6-bac7-aa9d64e72a37',
)

res = s.summary.get_user_profile_raw(req)

if res.raw_profile is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.GetUserProfileRawV2SummaryProfileUserIDRawGetRequest](../../models/operations/getuserprofilerawv2summaryprofileuseridrawgetrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.GetUserProfileRawV2SummaryProfileUserIDRawGetResponse](../../models/operations/getuserprofilerawv2summaryprofileuseridrawgetresponse.md)**


## get_user_sleep

Get Daily sleep for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserSleepV2SummarySleepUserIDGetRequest(
    start_date='Corporate quirkily',
    user_id='429e1c88-ab24-43bc-aa94-c896bba7aa1a',
)

res = s.summary.get_user_sleep(req)

if res.client_sleep_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetUserSleepV2SummarySleepUserIDGetRequest](../../models/operations/getusersleepv2summarysleepuseridgetrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.GetUserSleepV2SummarySleepUserIDGetResponse](../../models/operations/getusersleepv2summarysleepuseridgetresponse.md)**


## get_user_sleep_raw

Get Daily sleep for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserSleepRawV2SummarySleepUserIDRawGetRequest(
    start_date='Clothing Agent Account',
    user_id='f41f3fc0-77ea-4e72-85ab-9bb882f3ab0f',
)

res = s.summary.get_user_sleep_raw(req)

if res.raw_sleep is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetUserSleepRawV2SummarySleepUserIDRawGetRequest](../../models/operations/getusersleeprawv2summarysleepuseridrawgetrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetUserSleepRawV2SummarySleepUserIDRawGetResponse](../../models/operations/getusersleeprawv2summarysleepuseridrawgetresponse.md)**


## get_user_sleep_stream

Get Daily sleep stream for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserSleepStreamV2SummarySleepUserIDStreamGetRequest(
    start_date='Rock Southwest',
    user_id='35295037-bc4a-4b08-90f3-0d313cc6ef2c',
)

res = s.summary.get_user_sleep_stream(req)

if res.client_sleep_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.GetUserSleepStreamV2SummarySleepUserIDStreamGetRequest](../../models/operations/getusersleepstreamv2summarysleepuseridstreamgetrequest.md) | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |


### Response

**[operations.GetUserSleepStreamV2SummarySleepUserIDStreamGetResponse](../../models/operations/getusersleepstreamv2summarysleepuseridstreamgetresponse.md)**


## get_user_workouts

Get Daily workout for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserWorkoutsV2SummaryWorkoutsUserIDGetRequest(
    start_date='green whereas Principal',
    user_id='060981f4-a6eb-4525-909c-c6d2663c92f9',
)

res = s.summary.get_user_workouts(req)

if res.client_workout_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetUserWorkoutsV2SummaryWorkoutsUserIDGetRequest](../../models/operations/getuserworkoutsv2summaryworkoutsuseridgetrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetUserWorkoutsV2SummaryWorkoutsUserIDGetResponse](../../models/operations/getuserworkoutsv2summaryworkoutsuseridgetresponse.md)**


## get_user_workouts_raw

Get Daily workout for user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserWorkoutsRawV2SummaryWorkoutsUserIDRawGetRequest(
    start_date='card',
    user_id='3d65358a-d8c0-474b-9c21-9bac589e4fc0',
)

res = s.summary.get_user_workouts_raw(req)

if res.raw_workout is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.GetUserWorkoutsRawV2SummaryWorkoutsUserIDRawGetRequest](../../models/operations/getuserworkoutsrawv2summaryworkoutsuseridrawgetrequest.md) | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |


### Response

**[operations.GetUserWorkoutsRawV2SummaryWorkoutsUserIDRawGetResponse](../../models/operations/getuserworkoutsrawv2summaryworkoutsuseridrawgetresponse.md)**


## post_user_activity

Post User Activity

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.PostUserActivityV2SummaryActivityUserIDPostRequest(
    user_id='0e4724f5-d113-41c1-bf58-cd7168d06d0c',
)

res = s.summary.post_user_activity(req)

if res.response_post_user_activity_v2_summary_activity_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.PostUserActivityV2SummaryActivityUserIDPostRequest](../../models/operations/postuseractivityv2summaryactivityuseridpostrequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |


### Response

**[operations.PostUserActivityV2SummaryActivityUserIDPostResponse](../../models/operations/postuseractivityv2summaryactivityuseridpostresponse.md)**


## post_user_body

Post User Body

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.PostUserBodyV2SummaryBodyUserIDPostRequest(
    user_id='2aac64a8-1a4b-47b9-b083-c6d33a9beb02',
)

res = s.summary.post_user_body(req)

if res.response_post_user_body_v2_summary_body_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.PostUserBodyV2SummaryBodyUserIDPostRequest](../../models/operations/postuserbodyv2summarybodyuseridpostrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.PostUserBodyV2SummaryBodyUserIDPostResponse](../../models/operations/postuserbodyv2summarybodyuseridpostresponse.md)**


## post_user_profile

Post User Profile

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.PostUserProfileV2SummaryProfileUserIDPostRequest(
    user_id='343ee935-de73-408c-a15e-4782d3b864c4',
)

res = s.summary.post_user_profile(req)

if res.response_post_user_profile_v2_summary_profile_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.PostUserProfileV2SummaryProfileUserIDPostRequest](../../models/operations/postuserprofilev2summaryprofileuseridpostrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.PostUserProfileV2SummaryProfileUserIDPostResponse](../../models/operations/postuserprofilev2summaryprofileuseridpostresponse.md)**


## post_user_sleep

Post User Sleep

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.PostUserSleepV2SummarySleepUserIDPostRequest(
    user_id='4332e922-db99-44ec-bd9d-77a063c520e5',
)

res = s.summary.post_user_sleep(req)

if res.response_post_user_sleep_v2_summary_sleep_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PostUserSleepV2SummarySleepUserIDPostRequest](../../models/operations/postusersleepv2summarysleepuseridpostrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.PostUserSleepV2SummarySleepUserIDPostResponse](../../models/operations/postusersleepv2summarysleepuseridpostresponse.md)**


## post_user_workout

Post User Workout

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.PostUserWorkoutV2SummaryWorkoutsUserIDPostRequest(
    user_id='63a9d635-f084-45f5-a781-131420d3a83b',
)

res = s.summary.post_user_workout(req)

if res.response_post_user_workout_v2_summary_workouts_user_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.PostUserWorkoutV2SummaryWorkoutsUserIDPostRequest](../../models/operations/postuserworkoutv2summaryworkoutsuseridpostrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.PostUserWorkoutV2SummaryWorkoutsUserIDPostResponse](../../models/operations/postuserworkoutv2summaryworkoutsuseridpostresponse.md)**


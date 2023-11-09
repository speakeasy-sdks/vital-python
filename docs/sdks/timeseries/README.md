# Timeseries
(*timeseries*)

### Available Operations

* [get_blood_oxygen](#get_blood_oxygen) - Get Timeseries Resource Data
* [get_blood_pressure](#get_blood_pressure) - Get Timeseries Resource Data
* [get_caffeine](#get_caffeine) - Get Timeseries Resource Data
* [get_calories_active](#get_calories_active) - Get Timeseries Resource Data
* [get_calories_basal](#get_calories_basal) - Get Timeseries Resource Data
* [get_cholesterol_all](#get_cholesterol_all) - Get Timeseries Resource Data
* [get_cholesterol_hdl](#get_cholesterol_hdl) - Get Timeseries Resource Data
* [get_cholesterol_ldl](#get_cholesterol_ldl) - Get Timeseries Resource Data
* [get_distance](#get_distance) - Get Timeseries Resource Data
* [get_floors_climbed](#get_floors_climbed) - Get Timeseries Resource Data
* [get_glucose](#get_glucose) - Get Timeseries Resource Data
* [get_heartrate](#get_heartrate) - Get Timeseries Resource Data
* [get_hrv](#get_hrv) - Get Timeseries Resource Data
* [get_hypnogram](#get_hypnogram) - Get Timeseries Resource Data
* [get_ige](#get_ige) - Get Timeseries Resource Data
* [get_igg](#get_igg) - Get Timeseries Resource Data
* [get_mindfulness_minutes](#get_mindfulness_minutes) - Get Timeseries Resource Data
* [get_respiratory_rate](#get_respiratory_rate) - Get Timeseries Resource Data
* [get_steps](#get_steps) - Get Timeseries Resource Data
* [get_total_cholesterol](#get_total_cholesterol) - Get Timeseries Resource Data
* [get_triglycerides](#get_triglycerides) - Get Timeseries Resource Data
* [get_user_sleep_stream](#get_user_sleep_stream) - Get User Sleep Stream
* [get_user_workouts](#get_user_workouts) - Get User Workouts
* [get_water](#get_water) - Get Timeseries Resource Data
* [post_blood_pressure](#post_blood_pressure) - Post User Blood Pressure
* [post_vitals](#post_vitals) - Post User Vitals

## get_blood_oxygen

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_blood_oxygen(start_date='string', user_id='4c167a20-d001-40c6-9f96-363b96cbd8ac', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_blood_oxygen_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDBloodOxygenGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridbloodoxygengetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_blood_pressure

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_blood_pressure(start_date='string', user_id='e91b0b64-4f7b-43ea-a2b5-9387de819d04', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_blood_pressure_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDBloodPressureGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridbloodpressuregetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_caffeine

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_caffeine(start_date='string', user_id='4313a0eb-8609-48dc-86f6-c357cf521cb8', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_caffeine_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaffeineGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcaffeinegetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_calories_active

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_calories_active(start_date='string', user_id='0bc1117e-3cf3-4f90-b776-bb89ae3afbb8', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_calories_active_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaloriesActiveGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcaloriesactivegetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_calories_basal

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_calories_basal(start_date='string', user_id='64ab8090-2f0d-48b8-8aba-6b9f3470ca80', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_calories_basal_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaloriesBasalGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcaloriesbasalgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_cholesterol_all

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_cholesterol_all(start_date='string', user_id='4b6c3b20-9b90-4b59-87cd-42be3036af69', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_cholesterol_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesterolgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_cholesterol_hdl

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_cholesterol_hdl(start_date='string', user_id='f97d0d0e-3b2a-4529-bb1c-2d8b67282043', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_cholesterol_hdl_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolHdlGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesterolhdlgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_cholesterol_ldl

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_cholesterol_ldl(start_date='string', user_id='4f26c698-5e48-4f6e-8ca1-27edeb29d732', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_cholesterol_ldl_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolLdlGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesterolldlgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_distance

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_distance(start_date='string', user_id='19ab33e7-f639-49b8-b73c-69a8c4ea5f81', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_distance_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDDistanceGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseriddistancegetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_floors_climbed

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_floors_climbed(start_date='string', user_id='05b58dc0-4a14-4779-97b8-78666ff90d3c', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_floors_climbed_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDFloorsClimbedGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridfloorsclimbedgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_glucose

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_glucose(start_date='string', user_id='76c755f4-e363-461b-9888-a33b1731a7ae', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_glucose_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDGlucoseGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridglucosegetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_heartrate

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_heartrate(start_date='string', user_id='3a24193a-7e0c-448f-b11f-293d439db945', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_heartrate_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDHeartrateGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridheartrategetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_hrv

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_hrv(start_date='string', user_id='fa8c7b86-cf8a-4c7c-9611-342c13c4a095', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_hrv_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDHrvGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridhrvgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_hypnogram

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_hypnogram(start_date='string', user_id='9016363f-90dd-4ade-b540-c1806b114554', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_hypnogram_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDHypnogramGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridhypnogramgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_ige

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_ige(start_date='string', user_id='ed97cbc2-98b6-4fed-b0c6-813b66be805e', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_ige_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDIgeGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridigegetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_igg

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_igg(start_date='string', user_id='584254a7-0b28-4d95-af79-8c9cf8e7ce7f', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_igg_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDIggGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridigggetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_mindfulness_minutes

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_mindfulness_minutes(start_date='string', user_id='ff42bcd3-0f79-4dd6-a4ec-ae0a26ee2b9d', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_mindfulness_minutes_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDMindfulnessMinutesGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridmindfulnessminutesgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_respiratory_rate

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_respiratory_rate(start_date='string', user_id='f5daa7f6-973a-455e-a3cc-b2e2169f40d6', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_respiratory_rate_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDRespiratoryRateGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridrespiratoryrategetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_steps

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_steps(start_date='string', user_id='f3f7b728-ead1-4ba0-b792-0b80b82a067b', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_steps_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDStepsGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridstepsgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_total_cholesterol

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_total_cholesterol(start_date='string', user_id='b56cf900-a013-495d-92e9-eebe971547d8', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_cholesterol_total_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolTotalGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesteroltotalgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_triglycerides

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_triglycerides(start_date='string', user_id='58c97f14-3ec9-4355-8966-cdc7190c8f2e', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_cholesterol_triglycerides_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolTriglyceridesGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesteroltriglyceridesgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_user_sleep_stream

Get Sleep stream for a user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_user_sleep_stream(sleep_id='string')

if res.client_facing_sleep_stream is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `sleep_id`         | *str*              | :heavy_check_mark: | The Vital Sleep ID |


### Response

**[operations.GetUserSleepStreamV2TimeseriesSleepSleepIDStreamGetResponse](../../models/operations/getusersleepstreamv2timeseriessleepsleepidstreamgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_user_workouts

Get User Workouts

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_user_workouts(workout_id='bc0edaf0-6098-41f4-a6eb-525d09cc6d26')

if res.client_facing_stream is not None:
    # handle response
    pass
```

### Parameters

| Parameter                    | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `workout_id`                 | *str*                        | :heavy_check_mark:           | The Vital ID for the workout |


### Response

**[operations.GetUserWorkoutsV2TimeseriesWorkoutsWorkoutIDStreamGetResponse](../../models/operations/getuserworkoutsv2timeseriesworkoutsworkoutidstreamgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_water

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_water(start_date='string', user_id='2580182b-86b7-45ba-bc67-d64c9e6a0a12', end_date='string', provider='string')

if res.response_get_timeseries_resource_data_v2_timeseries_user_id_water_get is not None:
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

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDWaterGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridwatergetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## post_blood_pressure

Post User Blood Pressure

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.post_blood_pressure(user_id='5d55820e-8c39-4307-91e1-9cdd23720f04', x_vital_android_sdk_version='string', x_vital_ios_sdk_version='string')

if res.response_post_user_blood_pressure_v2_timeseries_user_id_blood_pressure_post is not None:
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

**[operations.PostUserBloodPressureV2TimeseriesUserIDBloodPressurePostResponse](../../models/operations/postuserbloodpressurev2timeseriesuseridbloodpressurepostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## post_vitals

Post User Vitals

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.timeseries.post_vitals(resource=shared.IngestibleTimeseriesResource.BLOOD_OXYGEN, user_id='7a0eca13-40ec-46ac-9433-f77edd2bbc91', x_vital_android_sdk_version='string', x_vital_ios_sdk_version='string')

if res.response_post_user_vitals_v2_timeseries_user_id_resource_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `resource`                                                                                 | [shared.IngestibleTimeseriesResource](../../models/shared/ingestibletimeseriesresource.md) | :heavy_check_mark:                                                                         | An enumeration.                                                                            |
| `user_id`                                                                                  | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `x_vital_android_sdk_version`                                                              | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | N/A                                                                                        |
| `x_vital_ios_sdk_version`                                                                  | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | N/A                                                                                        |


### Response

**[operations.PostUserVitalsV2TimeseriesUserIDResourcePostResponse](../../models/operations/postuservitalsv2timeseriesuseridresourcepostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

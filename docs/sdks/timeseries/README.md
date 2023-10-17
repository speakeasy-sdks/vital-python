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


res = s.timeseries.get_blood_oxygen(start_date='impactful', user_id='167a20d0-010c-46df-9636-3b96cbd8acaa', end_date='Dollar', provider='California')

if res.client_facing_blood_oxygen_timeseries is not None:
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


## get_blood_pressure

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_blood_pressure(start_date='gee', user_id='1b0b644f-7b3e-4a62-b593-87de819d0467', end_date='Silicon', provider='generating')

if res.client_facing_blood_pressure_timeseries is not None:
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


## get_caffeine

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_caffeine(start_date='Bike', user_id='0eb86098-dcc6-4f6c-b57c-f521cb838d86', end_date='Ward', provider='Account')

if res.client_facing_caffeine_timeseries is not None:
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


## get_calories_active

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_calories_active(start_date='Federation', user_id='1117e3cf-3f90-4377-abb8-9ae3afbb8a22', end_date='minor', provider='Officer')

if res.client_facing_calories_active_timeseries is not None:
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


## get_calories_basal

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_calories_basal(start_date='encoding', user_id='ab80902f-0d8b-480a-ba6b-9f3470ca8035', end_date='Cruiser', provider='hm')

if res.client_facing_calories_basal_timeseries is not None:
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


## get_cholesterol_all

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_cholesterol_all(start_date='scale', user_id='6c3b209b-90b5-4907-8d42-be3036af6959', end_date='nulla', provider='deposit')

if res.client_facing_cholesterol_timeseries is not None:
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


## get_cholesterol_hdl

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_cholesterol_hdl(start_date='offer', user_id='7d0d0e3b-2a52-49fb-9c2d-8b672820431e', end_date='sticky', provider='Rap')

if res.client_facing_cholesterol_timeseries is not None:
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


## get_cholesterol_ldl

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_cholesterol_ldl(start_date='Shirt', user_id='6985e48f-6e4c-4a12-bede-b29d7329161d', end_date='Fish', provider='Customer')

if res.client_facing_cholesterol_timeseries is not None:
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


## get_distance

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_distance(start_date='Borders', user_id='ab33e7f6-399b-48f7-bc69-a8c4ea5f811a', end_date='secured', provider='capacitor')

if res.client_facing_distance_timeseries is not None:
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


## get_floors_climbed

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_floors_climbed(start_date='Framingham', user_id='b58dc04a-1477-49d7-b878-666ff90d3c15', end_date='Mazda', provider='aspernatur')

if res.client_facing_floors_climbed_timeseries is not None:
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


## get_glucose

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_glucose(start_date='withdrawal', user_id='c755f4e3-6361-4b98-88a3-3b1731a7aeff', end_date='tinker', provider='New')

if res.client_facing_glucose_timeseries is not None:
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


## get_heartrate

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_heartrate(start_date='Tuna', user_id='24193a7e-0c48-4f71-9f29-3d439db94517', end_date='Bedfordshire', provider='Burundi')

if res.client_facing_heart_rate_timeseries is not None:
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


## get_hrv

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_hrv(start_date='onto', user_id='8c7b86cf-8ac7-4c96-9134-2c13c4a095df', end_date='invoice', provider='Music')

if res.client_facing_hrv_timeseries is not None:
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


## get_hypnogram

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_hypnogram(start_date='Agender', user_id='16363f90-ddad-4e35-80c1-806b114554f6', end_date='South', provider='parsing')

if res.client_facing_hypnogram_timeseries is not None:
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


## get_ige

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_ige(start_date='gosh', user_id='97cbc298-b6fe-4d30-8681-3b66be805e5c', end_date='maroon', provider='Rupee')

if res.client_facing_ige_timeseries is not None:
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


## get_igg

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_igg(start_date='orchestrate', user_id='54a70b28-d95e-4f79-8c9c-f8e7ce7fd8db', end_date='Recumbent', provider='Classical')

if res.client_facing_igg_timeseries is not None:
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


## get_mindfulness_minutes

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_mindfulness_minutes(start_date='win', user_id='42bcd30f-79dd-4664-acae-0a26ee2b9de9', end_date='equally', provider='humming')

if res.client_facing_mindfulness_minutes_timeseries is not None:
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


## get_respiratory_rate

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_respiratory_rate(start_date='circa', user_id='daa7f697-3a55-4ea3-8cb2-e2169f40d62d', end_date='upon', provider='Fluorine')

if res.client_facing_respiratory_rate_timeseries is not None:
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


## get_steps

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_steps(start_date='copying', user_id='f7b728ea-d1ba-4037-920b-80b82a067baf', end_date='optical', provider='platforms')

if res.client_facing_steps_timeseries is not None:
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


## get_total_cholesterol

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_total_cholesterol(start_date='Director', user_id='6cf900a0-1395-4d12-a9ee-be971547d810', end_date='farad', provider='partially')

if res.client_facing_cholesterol_timeseries is not None:
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


## get_triglycerides

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_triglycerides(start_date='Optional', user_id='c97f143e-c935-45c9-a6cd-c7190c8f2e16', end_date='state', provider='female')

if res.client_facing_cholesterol_timeseries is not None:
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


## get_user_sleep_stream

Get Sleep stream for a user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_user_sleep_stream(sleep_id='quantify')

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


## get_water

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.get_water(start_date='Garden', user_id='80182b86-b75b-4a3c-a7d6-4c9e6a0a1275', end_date='construction', provider='withdrawal')

if res.client_facing_water_timeseries is not None:
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


## post_blood_pressure

Post User Blood Pressure

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.timeseries.post_blood_pressure(user_id='5d55820e-8c39-4307-91e1-9cdd23720f04', x_vital_android_sdk_version='Indium', x_vital_ios_sdk_version='Cab')

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


## post_vitals

Post User Vitals

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.timeseries.post_vitals(resource=shared.IngestibleTimeseriesResource.BLOOD_OXYGEN, user_id='7a0eca13-40ec-46ac-9433-f77edd2bbc91', x_vital_android_sdk_version='Arkansas', x_vital_ios_sdk_version='perferendis')

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


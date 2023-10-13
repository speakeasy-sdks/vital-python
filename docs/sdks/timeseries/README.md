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

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDBloodOxygenGetRequest(
    start_date='blue',
    user_id='67a20d00-10c6-4df9-a363-b96cbd8acaa7',
)

res = s.timeseries.get_blood_oxygen(req)

if res.client_facing_blood_oxygen_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDBloodOxygenGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridbloodoxygengetrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDBloodOxygenGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridbloodoxygengetresponse.md)**


## get_blood_pressure

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDBloodPressureGetRequest(
    start_date='man Puerto Shoes',
    user_id='3ea62b59-387d-4e81-9d04-67b189bcd02a',
)

res = s.timeseries.get_blood_pressure(req)

if res.client_facing_blood_pressure_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDBloodPressureGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridbloodpressuregetrequest.md) | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDBloodPressureGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridbloodpressuregetresponse.md)**


## get_caffeine

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaffeineGetRequest(
    start_date='Electronic',
    user_id='3a0eb860-98dc-4c6f-ac35-7cf521cb838d',
)

res = s.timeseries.get_caffeine(req)

if res.client_facing_caffeine_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaffeineGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcaffeinegetrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaffeineGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcaffeinegetresponse.md)**


## get_calories_active

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaloriesActiveGetRequest(
    start_date='Uranium',
    user_id='1117e3cf-3f90-4377-abb8-9ae3afbb8a22',
)

res = s.timeseries.get_calories_active(req)

if res.client_facing_calories_active_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                        | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaloriesActiveGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcaloriesactivegetrequest.md) | :heavy_check_mark:                                                                                                                                                               | The request object to use for the request.                                                                                                                                       |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaloriesActiveGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcaloriesactivegetresponse.md)**


## get_calories_basal

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaloriesBasalGetRequest(
    start_date='Promethium South',
    user_id='02f0d8b8-0aba-46b9-b347-0ca8035c35e5',
)

res = s.timeseries.get_calories_basal(req)

if res.client_facing_calories_basal_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaloriesBasalGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcaloriesbasalgetrequest.md) | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCaloriesBasalGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcaloriesbasalgetresponse.md)**


## get_cholesterol_all

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolGetRequest(
    start_date='joule',
    user_id='c3b209b9-0b59-407c-942b-e3036af69597',
)

res = s.timeseries.get_cholesterol_all(req)

if res.client_facing_cholesterol_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesterolgetrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesterolgetresponse.md)**


## get_cholesterol_hdl

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolHdlGetRequest(
    start_date='in Van West',
    user_id='3b2a529f-b1c2-4d8b-a728-20431e439f53',
)

res = s.timeseries.get_cholesterol_hdl(req)

if res.client_facing_cholesterol_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                        | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolHdlGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesterolhdlgetrequest.md) | :heavy_check_mark:                                                                                                                                                               | The request object to use for the request.                                                                                                                                       |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolHdlGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesterolhdlgetresponse.md)**


## get_cholesterol_ldl

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolLdlGetRequest(
    start_date='construe',
    user_id='6c6985e4-8f6e-44ca-927e-deb29d732916',
)

res = s.timeseries.get_cholesterol_ldl(req)

if res.client_facing_cholesterol_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                        | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolLdlGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesterolldlgetrequest.md) | :heavy_check_mark:                                                                                                                                                               | The request object to use for the request.                                                                                                                                       |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolLdlGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesterolldlgetresponse.md)**


## get_distance

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDDistanceGetRequest(
    start_date='Classical',
    user_id='b33e7f63-99b8-4f73-869a-8c4ea5f811a6',
)

res = s.timeseries.get_distance(req)

if res.client_facing_distance_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDDistanceGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseriddistancegetrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDDistanceGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseriddistancegetresponse.md)**


## get_floors_climbed

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDFloorsClimbedGetRequest(
    start_date='models',
    user_id='58dc04a1-4779-4d7b-8786-66ff90d3c15d',
)

res = s.timeseries.get_floors_climbed(req)

if res.client_facing_floors_climbed_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDFloorsClimbedGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridfloorsclimbedgetrequest.md) | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDFloorsClimbedGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridfloorsclimbedgetresponse.md)**


## get_glucose

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDGlucoseGetRequest(
    start_date='Syrian explicit',
    user_id='f4e36361-b988-48a3-bb17-31a7aefffe29',
)

res = s.timeseries.get_glucose(req)

if res.client_facing_glucose_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                          | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDGlucoseGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridglucosegetrequest.md) | :heavy_check_mark:                                                                                                                                                 | The request object to use for the request.                                                                                                                         |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDGlucoseGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridglucosegetresponse.md)**


## get_heartrate

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDHeartrateGetRequest(
    start_date='Corporate',
    user_id='4193a7e0-c48f-4711-b293-d439db945171',
)

res = s.timeseries.get_heartrate(req)

if res.client_facing_heart_rate_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDHeartrateGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridheartrategetrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDHeartrateGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridheartrategetresponse.md)**


## get_hrv

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDHrvGetRequest(
    start_date='Global violet male',
    user_id='6cf8ac7c-9611-4342-813c-4a095df7f31a',
)

res = s.timeseries.get_hrv(req)

if res.client_facing_hrv_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                  | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                  | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDHrvGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridhrvgetrequest.md) | :heavy_check_mark:                                                                                                                                         | The request object to use for the request.                                                                                                                 |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDHrvGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridhrvgetresponse.md)**


## get_hypnogram

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDHypnogramGetRequest(
    start_date='North Kroon',
    user_id='63f90dda-de35-440c-9806-b114554f66a1',
)

res = s.timeseries.get_hypnogram(req)

if res.client_facing_hypnogram_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDHypnogramGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridhypnogramgetrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDHypnogramGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridhypnogramgetresponse.md)**


## get_ige

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDIgeGetRequest(
    start_date='Minivan TCP male',
    user_id='298b6fed-30c6-4813-b66b-e805e5cc66a9',
)

res = s.timeseries.get_ige(req)

if res.client_facing_ige_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                  | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                  | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDIgeGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridigegetrequest.md) | :heavy_check_mark:                                                                                                                                         | The request object to use for the request.                                                                                                                 |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDIgeGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridigegetresponse.md)**


## get_igg

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDIggGetRequest(
    start_date='compressing pink',
    user_id='4a70b28d-95ef-4798-89cf-8e7ce7fd8dbc',
)

res = s.timeseries.get_igg(req)

if res.client_facing_igg_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                  | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                  | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDIggGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridigggetrequest.md) | :heavy_check_mark:                                                                                                                                         | The request object to use for the request.                                                                                                                 |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDIggGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridigggetresponse.md)**


## get_mindfulness_minutes

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDMindfulnessMinutesGetRequest(
    start_date='emigrate Ohio fuchsia',
    user_id='30f79dd6-64ec-4ae0-a26e-e2b9de9e3e65',
)

res = s.timeseries.get_mindfulness_minutes(req)

if res.client_facing_mindfulness_minutes_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDMindfulnessMinutesGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridmindfulnessminutesgetrequest.md) | :heavy_check_mark:                                                                                                                                                                       | The request object to use for the request.                                                                                                                                               |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDMindfulnessMinutesGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridmindfulnessminutesgetresponse.md)**


## get_respiratory_rate

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDRespiratoryRateGetRequest(
    start_date='systematic Division Intersex',
    user_id='a55ea3cc-b2e2-4169-b40d-62dfeb102d68',
)

res = s.timeseries.get_respiratory_rate(req)

if res.client_facing_respiratory_rate_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                          | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDRespiratoryRateGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridrespiratoryrategetrequest.md) | :heavy_check_mark:                                                                                                                                                                 | The request object to use for the request.                                                                                                                                         |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDRespiratoryRateGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridrespiratoryrategetresponse.md)**


## get_steps

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDStepsGetRequest(
    start_date='Sausages Surinam tan',
    user_id='ead1ba03-7920-4b80-b82a-067baf7e5286',
)

res = s.timeseries.get_steps(req)

if res.client_facing_steps_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDStepsGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridstepsgetrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDStepsGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridstepsgetresponse.md)**


## get_total_cholesterol

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolTotalGetRequest(
    start_date='technologies Tricycle accusantium',
    user_id='0a01395d-12e9-4eeb-a971-547d810cce95',
)

res = s.timeseries.get_total_cholesterol(req)

if res.client_facing_cholesterol_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                            | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolTotalGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesteroltotalgetrequest.md) | :heavy_check_mark:                                                                                                                                                                   | The request object to use for the request.                                                                                                                                           |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolTotalGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesteroltotalgetresponse.md)**


## get_triglycerides

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolTriglyceridesGetRequest(
    start_date='transmit quam',
    user_id='f143ec93-55c9-466c-9c71-90c8f2e167e9',
)

res = s.timeseries.get_triglycerides(req)

if res.client_facing_cholesterol_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                            | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolTriglyceridesGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesteroltriglyceridesgetrequest.md) | :heavy_check_mark:                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                           |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDCholesterolTriglyceridesGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridcholesteroltriglyceridesgetresponse.md)**


## get_user_sleep_stream

Get Sleep stream for a user_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserSleepStreamV2TimeseriesSleepSleepIDStreamGetRequest(
    sleep_id='Rock Southwest',
)

res = s.timeseries.get_user_sleep_stream(req)

if res.client_facing_sleep_stream is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.GetUserSleepStreamV2TimeseriesSleepSleepIDStreamGetRequest](../../models/operations/getusersleepstreamv2timeseriessleepsleepidstreamgetrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.GetUserSleepStreamV2TimeseriesSleepSleepIDStreamGetResponse](../../models/operations/getusersleepstreamv2timeseriessleepsleepidstreamgetresponse.md)**


## get_user_workouts

Get User Workouts

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserWorkoutsV2TimeseriesWorkoutsWorkoutIDStreamGetRequest(
    workout_id='bc0edaf0-6098-41f4-a6eb-525d09cc6d26',
)

res = s.timeseries.get_user_workouts(req)

if res.client_facing_stream is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                          | [operations.GetUserWorkoutsV2TimeseriesWorkoutsWorkoutIDStreamGetRequest](../../models/operations/getuserworkoutsv2timeseriesworkoutsworkoutidstreamgetrequest.md) | :heavy_check_mark:                                                                                                                                                 | The request object to use for the request.                                                                                                                         |


### Response

**[operations.GetUserWorkoutsV2TimeseriesWorkoutsWorkoutIDStreamGetResponse](../../models/operations/getuserworkoutsv2timeseriesworkoutsworkoutidstreamgetresponse.md)**


## get_water

Get timeseries data for user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTimeseriesResourceDataV2TimeseriesUserIDWaterGetRequest(
    start_date='interactive',
    user_id='0182b86b-75ba-43c6-bd64-c9e6a0a1275f',
)

res = s.timeseries.get_water(req)

if res.client_facing_water_timeseries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.GetTimeseriesResourceDataV2TimeseriesUserIDWaterGetRequest](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridwatergetrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.GetTimeseriesResourceDataV2TimeseriesUserIDWaterGetResponse](../../models/operations/gettimeseriesresourcedatav2timeseriesuseridwatergetresponse.md)**


## post_blood_pressure

Post User Blood Pressure

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.PostUserBloodPressureV2TimeseriesUserIDBloodPressurePostRequest(
    user_id='5d55820e-8c39-4307-91e1-9cdd23720f04',
)

res = s.timeseries.post_blood_pressure(req)

if res.response_post_user_blood_pressure_v2_timeseries_user_id_blood_pressure_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                | [operations.PostUserBloodPressureV2TimeseriesUserIDBloodPressurePostRequest](../../models/operations/postuserbloodpressurev2timeseriesuseridbloodpressurepostrequest.md) | :heavy_check_mark:                                                                                                                                                       | The request object to use for the request.                                                                                                                               |


### Response

**[operations.PostUserBloodPressureV2TimeseriesUserIDBloodPressurePostResponse](../../models/operations/postuserbloodpressurev2timeseriesuseridbloodpressurepostresponse.md)**


## post_vitals

Post User Vitals

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()

req = operations.PostUserVitalsV2TimeseriesUserIDResourcePostRequest(
    resource=shared.IngestibleTimeseriesResource.BLOOD_OXYGEN,
    user_id='7a0eca13-40ec-46ac-9433-f77edd2bbc91',
)

res = s.timeseries.post_vitals(req)

if res.response_post_user_vitals_v2_timeseries_user_id_resource_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.PostUserVitalsV2TimeseriesUserIDResourcePostRequest](../../models/operations/postuservitalsv2timeseriesuseridresourcepostrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.PostUserVitalsV2TimeseriesUserIDResourcePostResponse](../../models/operations/postuservitalsv2timeseriesuseridresourcepostresponse.md)**


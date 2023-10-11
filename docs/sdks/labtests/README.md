# LabTests
(*lab_tests*)

### Available Operations

* [create](#create) - Create Lab Test For Team
* [get_labs](#get_labs) - Get Labs
* [get_marker_by_provider](#get_marker_by_provider) - Get Markers By Provider Id
* [get_markers](#get_markers) - Get Markers
* [list](#list) - Get Lab Tests For Team

## create

Create Lab Test For Team

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.CreateLabTestRequest(
    description='Multi-tiered human-resource model',
    lab_id=859213,
    marker_ids=[
        417458,
    ],
    method=shared.LabTestCollectionMethod.TESTKIT,
    name='blue',
    sample_type=shared.LabTestSampleType.URINE,
)

res = s.lab_tests.create(req)

if res.client_facing_lab_test is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.CreateLabTestRequest](../../models/shared/createlabtestrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateLabTestForTeamV3LabTestsPostResponse](../../models/operations/createlabtestforteamv3labtestspostresponse.md)**


## get_labs

GET all the labs.

### Example Usage

```python
import vital


s = vital.Vital()


res = s.lab_tests.get_labs()

if res.client_facing_labs is not None:
    # handle response
```


### Response

**[operations.GetLabsV3LabTestsLabsGetResponse](../../models/operations/getlabsv3labtestslabsgetresponse.md)**


## get_marker_by_provider

GET a specific marker for the given lab and provider_id

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetMarkersByProviderIDV3LabTestsLabIDMarkersProviderIDGetRequest(
    lab_id=263548,
    provider_id='Bronze',
)

res = s.lab_tests.get_marker_by_provider(req)

if res.client_facing_marker is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.GetMarkersByProviderIDV3LabTestsLabIDMarkersProviderIDGetRequest](../../models/operations/getmarkersbyprovideridv3labtestslabidmarkersprovideridgetrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.GetMarkersByProviderIDV3LabTestsLabIDMarkersProviderIDGetResponse](../../models/operations/getmarkersbyprovideridv3labtestslabidmarkersprovideridgetresponse.md)**


## get_markers

GET all the markers for the given lab.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetMarkersV3LabTestsMarkersGetRequest()

res = s.lab_tests.get_markers(req)

if res.get_markers_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetMarkersV3LabTestsMarkersGetRequest](../../models/operations/getmarkersv3labtestsmarkersgetrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetMarkersV3LabTestsMarkersGetResponse](../../models/operations/getmarkersv3labtestsmarkersgetresponse.md)**


## list

GET all the lab tests the team has access to.

### Example Usage

```python
import vital


s = vital.Vital()


res = s.lab_tests.list()

if res.client_facing_lab_tests is not None:
    # handle response
```


### Response

**[operations.GetLabTestsForTeamV3LabTestsGetResponse](../../models/operations/getlabtestsforteamv3labtestsgetresponse.md)**


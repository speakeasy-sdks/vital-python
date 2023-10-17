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

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)

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
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.CreateLabTestRequest](../../models/shared/createlabtestrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |


### Response

**[operations.CreateLabTestForTeamV3LabTestsPostResponse](../../models/operations/createlabtestforteamv3labtestspostresponse.md)**


## get_labs

GET all the labs.

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.lab_tests.get_labs()

if res.client_facing_labs is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetLabsV3LabTestsLabsGetResponse](../../models/operations/getlabsv3labtestslabsgetresponse.md)**


## get_marker_by_provider

GET a specific marker for the given lab and provider_id

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.lab_tests.get_marker_by_provider(lab_id=263548, provider_id='East')

if res.client_facing_marker is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `lab_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `provider_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetMarkersByProviderIDV3LabTestsLabIDMarkersProviderIDGetResponse](../../models/operations/getmarkersbyprovideridv3labtestslabidmarkersprovideridgetresponse.md)**


## get_markers

GET all the markers for the given lab.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.lab_tests.get_markers(lab_id=614936, name='parse', page=301534, size=44930)

if res.get_markers_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `lab_id`                                                                                       | *Optional[int]*                                                                                | :heavy_minus_sign:                                                                             | The identifier Vital assigned to a lab partner.                                                |
| `name`                                                                                         | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | The name of an individual biomarker or a panel. Used as a fuzzy filter when searching markers. |
| `page`                                                                                         | *Optional[int]*                                                                                | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `size`                                                                                         | *Optional[int]*                                                                                | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.GetMarkersV3LabTestsMarkersGetResponse](../../models/operations/getmarkersv3labtestsmarkersgetresponse.md)**


## list

GET all the lab tests the team has access to.

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.lab_tests.list()

if res.client_facing_lab_tests is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetLabTestsForTeamV3LabTestsGetResponse](../../models/operations/getlabtestsforteamv3labtestsgetresponse.md)**


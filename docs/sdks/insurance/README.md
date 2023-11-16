# Insurance
(*insurance*)

### Available Operations

* [search_diagnosis](#search_diagnosis) - Search Diagnosis
* [search_insurance_payor_info](#search_insurance_payor_info) - Search Insurance Payor Information

## search_diagnosis

Search Diagnosis

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.insurance.search_diagnosis(diagnosis_query='string')

if res.response_search_diagnosis_v3_insurance_search_diagnosis_get is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `diagnosis_query`  | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.SearchDiagnosisV3InsuranceSearchDiagnosisGetResponse](../../models/operations/searchdiagnosisv3insurancesearchdiagnosisgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## search_insurance_payor_info

Search Insurance Payor Information

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.PayorSearchRequest(
    insurance_name='string',
)

res = s.insurance.search_insurance_payor_info(req)

if res.response_search_insurance_payor_information_v3_insurance_search_payor_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.PayorSearchRequest](../../models/shared/payorsearchrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.SearchInsurancePayorInformationV3InsuranceSearchPayorPostResponse](../../models/operations/searchinsurancepayorinformationv3insurancesearchpayorpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

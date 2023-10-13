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

req = operations.SearchDiagnosisV3InsuranceSearchDiagnosisGetRequest(
    diagnosis_query='deposit Car',
)

res = s.insurance.search_diagnosis(req)

if res.client_facing_diagnosis_informations is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.SearchDiagnosisV3InsuranceSearchDiagnosisGetRequest](../../models/operations/searchdiagnosisv3insurancesearchdiagnosisgetrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.SearchDiagnosisV3InsuranceSearchDiagnosisGetResponse](../../models/operations/searchdiagnosisv3insurancesearchdiagnosisgetresponse.md)**


## search_insurance_payor_info

Search Insurance Payor Information

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.PayorSearchRequest(
    insurance_name='South entry Bicycle',
)

res = s.insurance.search_insurance_payor_info(req)

if res.client_facing_payor_search_responses is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.PayorSearchRequest](../../models/shared/payorsearchrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.SearchInsurancePayorInformationV3InsuranceSearchPayorPostResponse](../../models/operations/searchinsurancepayorinformationv3insurancesearchpayorpostresponse.md)**


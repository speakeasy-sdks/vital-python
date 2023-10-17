# Providers
(*providers*)

### Available Operations

* [list](#list) - Get List Of Providers

## list

Get Provider list

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.providers.list()

if res.client_facing_provider_detaileds is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetListOfProvidersV2ProvidersGetResponse](../../models/operations/getlistofprovidersv2providersgetresponse.md)**


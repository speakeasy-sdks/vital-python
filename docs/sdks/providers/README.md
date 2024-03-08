# Providers
(*providers*)

### Available Operations

* [list](#list) - Get List Of Providers

## list

Get Provider list

### Example Usage

```python
import vital

s = vital.Vital()


res = s.providers.list()

if res.response_get_list_of_providers_v2_providers_get is not None:
    # handle response
    pass

```


### Response

**[operations.GetListOfProvidersV2ProvidersGetResponse](../../models/operations/getlistofprovidersv2providersgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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

if res.client_facing_provider_detaileds is not None:
    # handle response
    pass
```


### Response

**[operations.GetListOfProvidersV2ProvidersGetResponse](../../models/operations/getlistofprovidersv2providersgetresponse.md)**


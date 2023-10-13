# User
(*user*)

### Available Operations

* [create_user](#create_user) - Create User
* [delete](#delete) - Delete User
* [deregister_provider_v2_user_user_id_provider_delete](#deregister_provider_v2_user_user_id_provider_delete) - Deregister Provider
* [get](#get) - Get User
* [get_all](#get_all) - Get Teams Users
* [get_connected_providers](#get_connected_providers) - Get Connected Providers
* [get_metrics](#get_metrics) - Get Teams Metrics
* [get_sign_in_token](#get_sign_in_token) - Get User Sign In Token
* [patch_user_v2_user_user_id_patch](#patch_user_v2_user_user_id_patch) - Patch User
* [refresh_user_id_v2_user_refresh_user_id_post](#refresh_user_id_v2_user_refresh_user_id_post) - Refresh User Id
* [resolve_by_user_id](#resolve_by_user_id) - Get User By Client User Id

## create_user

POST Create a Vital user given a client_user_id and returns the user_id.

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.UserCreateBody(
    client_user_id='dicta Forward',
)

res = s.user.create_user(req)

if res.client_facing_user_key is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.UserCreateBody](../../models/shared/usercreatebody.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.CreateUserV2UserPostResponse](../../models/operations/createuserv2userpostresponse.md)**


## delete

Delete User

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.DeleteUserV2UserUserIDDeleteRequest(
    user_id='8db863f6-ef9b-413a-8a70-cb816b33de6b',
)

res = s.user.delete(req)

if res.user_success_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.DeleteUserV2UserUserIDDeleteRequest](../../models/operations/deleteuserv2useruseriddeleterequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.DeleteUserV2UserUserIDDeleteResponse](../../models/operations/deleteuserv2useruseriddeleteresponse.md)**


## deregister_provider_v2_user_user_id_provider_delete

Deregister Provider

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()

req = operations.DeregisterProviderV2UserUserIDProviderDeleteRequest(
    provider=shared.Providers.GARMIN,
    user_id='6d48b1ec-267e-4530-bcf8-b4f041e375ee',
)

res = s.user.deregister_provider_v2_user_user_id_provider_delete(req)

if res.user_success_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.DeregisterProviderV2UserUserIDProviderDeleteRequest](../../models/operations/deregisterproviderv2useruseridproviderdeleterequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.DeregisterProviderV2UserUserIDProviderDeleteResponse](../../models/operations/deregisterproviderv2useruseridproviderdeleteresponse.md)**


## get

GET User details given the user_id.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserV2UserUserIDGetRequest(
    user_id='b18d8d81-fd7b-4764-a31e-475cb1f36591',
)

res = s.user.get(req)

if res.client_facing_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetUserV2UserUserIDGetRequest](../../models/operations/getuserv2useruseridgetrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetUserV2UserUserIDGetResponse](../../models/operations/getuserv2useruseridgetresponse.md)**


## get_all

GET All users for team.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetTeamsUsersV2UserGetRequest()

res = s.user.get_all(req)

if res.paginated_users_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetTeamsUsersV2UserGetRequest](../../models/operations/getteamsusersv2usergetrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetTeamsUsersV2UserGetResponse](../../models/operations/getteamsusersv2usergetresponse.md)**


## get_connected_providers

GET Users connected providers

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetConnectedProvidersV2UserProvidersUserIDGetRequest(
    user_id='30ef9033-9974-45c7-af5c-ddc9369dd7a0',
)

res = s.user.get_connected_providers(req)

if res.response_get_connected_providers_v2_user_providers_user_id_get is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.GetConnectedProvidersV2UserProvidersUserIDGetRequest](../../models/operations/getconnectedprovidersv2userprovidersuseridgetrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.GetConnectedProvidersV2UserProvidersUserIDGetResponse](../../models/operations/getconnectedprovidersv2userprovidersuseridgetresponse.md)**


## get_metrics

GET metrics for team.

### Example Usage

```python
import vital


s = vital.Vital()


res = s.user.get_metrics()

if res.metrics_result is not None:
    # handle response
    pass
```


### Response

**[operations.GetTeamsMetricsV2UserMetricsGetResponse](../../models/operations/getteamsmetricsv2usermetricsgetresponse.md)**


## get_sign_in_token

Get User Sign In Token

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserSignInTokenV2UserUserIDSignInTokenPostRequest(
    user_id='d738147a-606f-41ac-a296-81a3993405ee',
)

res = s.user.get_sign_in_token(req)

if res.user_sign_in_token_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.GetUserSignInTokenV2UserUserIDSignInTokenPostRequest](../../models/operations/getusersignintokenv2useruseridsignintokenpostrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.GetUserSignInTokenV2UserUserIDSignInTokenPostResponse](../../models/operations/getusersignintokenv2useruseridsignintokenpostresponse.md)**


## patch_user_v2_user_user_id_patch

Patch User

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()

req = operations.PatchUserV2UserUserIDPatchRequest(
    user_patch_body=shared.UserPatchBody(),
    user_id='02c6960d-b280-4a76-8c76-467d647deb43',
)

res = s.user.patch_user_v2_user_user_id_patch(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchUserV2UserUserIDPatchRequest](../../models/operations/patchuserv2useruseridpatchrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchUserV2UserUserIDPatchResponse](../../models/operations/patchuserv2useruseridpatchresponse.md)**


## refresh_user_id_v2_user_refresh_user_id_post

Trigger a manual refresh for a specific user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.RefreshUserIDV2UserRefreshUserIDPostRequest(
    user_id='1d35a855-b124-4dda-9838-fdeec970978f',
)

res = s.user.refresh_user_id_v2_user_refresh_user_id_post(req)

if res.user_refresh_success_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.RefreshUserIDV2UserRefreshUserIDPostRequest](../../models/operations/refreshuseridv2userrefreshuseridpostrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.RefreshUserIDV2UserRefreshUserIDPostResponse](../../models/operations/refreshuseridv2userrefreshuseridpostresponse.md)**


## resolve_by_user_id

GET user_id from client_user_id.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetUserByClientUserIDV2UserResolveClientUserIDGetRequest(
    client_user_id='Granite whiteboard excluding',
)

res = s.user.resolve_by_user_id(req)

if res.client_facing_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                  | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                  | [operations.GetUserByClientUserIDV2UserResolveClientUserIDGetRequest](../../models/operations/getuserbyclientuseridv2userresolveclientuseridgetrequest.md) | :heavy_check_mark:                                                                                                                                         | The request object to use for the request.                                                                                                                 |


### Response

**[operations.GetUserByClientUserIDV2UserResolveClientUserIDGetResponse](../../models/operations/getuserbyclientuseridv2userresolveclientuseridgetresponse.md)**


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


res = s.user.delete(user_id='8db863f6-ef9b-413a-8a70-cb816b33de6b')

if res.user_success_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteUserV2UserUserIDDeleteResponse](../../models/operations/deleteuserv2useruseriddeleteresponse.md)**


## deregister_provider_v2_user_user_id_provider_delete

Deregister Provider

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.user.deregister_provider_v2_user_user_id_provider_delete(provider=shared.Providers.GARMIN, user_id='6d48b1ec-267e-4530-bcf8-b4f041e375ee')

if res.user_success_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `provider`                                           | [shared.Providers](../../models/shared/providers.md) | :heavy_check_mark:                                   | Provider slug. e.g., `oura`, `fitbit`, `garmin`.     |
| `user_id`                                            | *str*                                                | :heavy_check_mark:                                   | N/A                                                  |


### Response

**[operations.DeregisterProviderV2UserUserIDProviderDeleteResponse](../../models/operations/deregisterproviderv2useruseridproviderdeleteresponse.md)**


## get

GET User details given the user_id.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.user.get(user_id='b18d8d81-fd7b-4764-a31e-475cb1f36591')

if res.client_facing_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetUserV2UserUserIDGetResponse](../../models/operations/getuserv2useruseridgetresponse.md)**


## get_all

GET All users for team.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.user.get_all(limit=178225, offset=64345)

if res.paginated_users_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `limit`            | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `offset`           | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetTeamsUsersV2UserGetResponse](../../models/operations/getteamsusersv2usergetresponse.md)**


## get_connected_providers

GET Users connected providers

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.user.get_connected_providers(user_id='30ef9033-9974-45c7-af5c-ddc9369dd7a0')

if res.response_get_connected_providers_v2_user_providers_user_id_get is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |


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


res = s.user.get_sign_in_token(user_id='d738147a-606f-41ac-a296-81a3993405ee')

if res.user_sign_in_token_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetUserSignInTokenV2UserUserIDSignInTokenPostResponse](../../models/operations/getusersignintokenv2useruseridsignintokenpostresponse.md)**


## patch_user_v2_user_user_id_patch

Patch User

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.user.patch_user_v2_user_user_id_patch(user_patch_body=shared.UserPatchBody(), user_id='02c6960d-b280-4a76-8c76-467d647deb43')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `user_patch_body`                                            | [shared.UserPatchBody](../../models/shared/userpatchbody.md) | :heavy_check_mark:                                           | N/A                                                          |
| `user_id`                                                    | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |


### Response

**[operations.PatchUserV2UserUserIDPatchResponse](../../models/operations/patchuserv2useruseridpatchresponse.md)**


## refresh_user_id_v2_user_refresh_user_id_post

Trigger a manual refresh for a specific user

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.user.refresh_user_id_v2_user_refresh_user_id_post(user_id='1d35a855-b124-4dda-9838-fdeec970978f')

if res.user_refresh_success_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.RefreshUserIDV2UserRefreshUserIDPostResponse](../../models/operations/refreshuseridv2userrefreshuseridpostresponse.md)**


## resolve_by_user_id

GET user_id from client_user_id.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.user.resolve_by_user_id(client_user_id='Bicycle')

if res.client_facing_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_user_id`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                             | A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id. |


### Response

**[operations.GetUserByClientUserIDV2UserResolveClientUserIDGetResponse](../../models/operations/getuserbyclientuseridv2userresolveclientuseridgetresponse.md)**


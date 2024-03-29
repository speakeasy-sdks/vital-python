# Team
(*team*)

### Available Operations

* [create](#create) - Create Team
* [create_api_key](#create_api_key) - Create Api Key
* [create_priority](#create_priority) - Create Priority
* [delete_api_key](#delete_api_key) - Delete Api Key
* [get](#get) - Get Team
* [get_api_keys](#get_api_keys) - Get Api Keys For Team
* [get_config](#get_config) - Get Team Config
* [get_source_priorities](#get_source_priorities) - Get Source Priorities
* [get_user_count](#get_user_count) - Get Team User Count
* [get_webhook_url](#get_webhook_url) - Get Svix Webhook Url
* [rotate_api_key_v2_team_team_id_apikey_api_key_id_rotate_patch](#rotate_api_key_v2_team_team_id_apikey_api_key_id_rotate_patch) - Rotate Api Key
* [search_users_by_uuid](#search_users_by_uuid) - Search Team Users By Uuid Or Client User Id
* [update_api_key_label_v2_team_team_id_apikey_api_key_id_patch](#update_api_key_label_v2_team_team_id_apikey_api_key_id_patch) - Update Api Key Label
* [update_source_priorities_v2_team_source_priorities_patch](#update_source_priorities_v2_team_source_priorities_patch) - Update Source Priorities
* [update_team_v2_team_team_id_patch](#update_team_v2_team_team_id_patch) - Update Team

## create

Create Team.

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.TeamCreate(
    name='<value>',
)

res = s.team.create(req)

if res.team_in_db is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.TeamCreate](../../models/shared/teamcreate.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.CreateTeamV2TeamPostResponse](../../models/operations/createteamv2teampostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## create_api_key

Create api key.

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()


res = s.team.create_api_key(create_api_key_body=shared.CreateAPIKeyBody(
    label='<value>',
), team_id='<value>')

if res.api_key_in_db is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `create_api_key_body`                                              | [shared.CreateAPIKeyBody](../../models/shared/createapikeybody.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `team_id`                                                          | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |


### Response

**[operations.CreateAPIKeyV2TeamTeamIDApikeyPostResponse](../../models/operations/createapikeyv2teamteamidapikeypostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## create_priority

Add Team priority row for source

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()


res = s.team.create_priority(priority_create=shared.PriorityCreate(
    priority=548209,
    source_id=168326,
    team_id='0d4e3a38-5a06-40f0-b144-d921de79168b',
), team_id='<value>')

if res.priority is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `priority_create`                                              | [shared.PriorityCreate](../../models/shared/prioritycreate.md) | :heavy_check_mark:                                             | N/A                                                            |
| `team_id`                                                      | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |


### Response

**[operations.CreatePriorityV2TeamTeamIDPriorityPostResponse](../../models/operations/createpriorityv2teamteamidprioritypostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## delete_api_key

Invalidate api key by key value.

### Example Usage

```python
import vital

s = vital.Vital()


res = s.team.delete_api_key(api_key_id='<value>', team_id='<value>')

if res.api_key_in_db is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `api_key_id`       | *str*              | :heavy_check_mark: | N/A                |
| `team_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIKeyV2TeamTeamIDApikeyAPIKeyIDDeleteResponse](../../models/operations/deleteapikeyv2teamteamidapikeyapikeyiddeleteresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## get

Get team.

### Example Usage

```python
import vital

s = vital.Vital()


res = s.team.get(team_id='b18d8d81-fd7b-4764-a31e-475cb1f36591')

if res.client_facing_team is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `team_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTeamV2TeamTeamIDGetResponse](../../models/operations/getteamv2teamteamidgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## get_api_keys

Invalidate api key by key value.

### Example Usage

```python
import vital

s = vital.Vital()


res = s.team.get_api_keys(team_id='<value>')

if res.response_get_api_keys_for_team_v2_team_team_id_apikeys_get is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `team_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIKeysForTeamV2TeamTeamIDApikeysGetResponse](../../models/operations/getapikeysforteamv2teamteamidapikeysgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## get_config

Post teams.

### Example Usage

```python
import vital

s = vital.Vital()


res = s.team.get_config()

if res.response_get_team_config_v2_team_link_config_get is not None:
    # handle response
    pass

```


### Response

**[operations.GetTeamConfigV2TeamLinkConfigGetResponse](../../models/operations/getteamconfigv2teamlinkconfiggetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_source_priorities

GET source priorities.

### Example Usage

```python
import vital

s = vital.Vital()


res = s.team.get_source_priorities(data_type='<value>')

if res.response_get_source_priorities_v2_team_source_priorities_get is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `data_type`        | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetSourcePrioritiesV2TeamSourcePrioritiesGetResponse](../../models/operations/getsourceprioritiesv2teamsourceprioritiesgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## get_user_count

Get the current user count for a team.

### Example Usage

```python
import vital

s = vital.Vital()


res = s.team.get_user_count(team_id='3021769b-866d-4c37-8307-789796d71ace')

if res.response_get_team_user_count_v2_team_team_id_users_count_get is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `team_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTeamUserCountV2TeamTeamIDUsersCountGetResponse](../../models/operations/getteamusercountv2teamteamiduserscountgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## get_webhook_url

Get Svix Webhook Url

### Example Usage

```python
import vital

s = vital.Vital()


res = s.team.get_webhook_url()

if res.response_get_svix_webhook_url_v2_team_svix_url_get is not None:
    # handle response
    pass

```


### Response

**[operations.GetSvixWebhookURLV2TeamSvixURLGetResponse](../../models/operations/getsvixwebhookurlv2teamsvixurlgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## rotate_api_key_v2_team_team_id_apikey_api_key_id_rotate_patch

Deprecated. Rotate api key.

### Example Usage

```python
import vital

s = vital.Vital()


res = s.team.rotate_api_key_v2_team_team_id_apikey_api_key_id_rotate_patch(api_key_id='<value>', team_id='<value>')

if res.api_key_in_db is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `api_key_id`       | *str*              | :heavy_check_mark: | N/A                |
| `team_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.RotateAPIKeyV2TeamTeamIDApikeyAPIKeyIDRotatePatchResponse](../../models/operations/rotateapikeyv2teamteamidapikeyapikeyidrotatepatchresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## search_users_by_uuid

Search team users by user_id

### Example Usage

```python
import vital

s = vital.Vital()


res = s.team.search_users_by_uuid(query_id='<value>')

if res.response_search_team_users_by_uuid_or_client_user_id_v2_team_users_search_get is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `query_id`         | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.SearchTeamUsersByUUIDOrClientUserIDV2TeamUsersSearchGetResponse](../../models/operations/searchteamusersbyuuidorclientuseridv2teamuserssearchgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## update_api_key_label_v2_team_team_id_apikey_api_key_id_patch

Update API key label.

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()


res = s.team.update_api_key_label_v2_team_team_id_apikey_api_key_id_patch(update_api_key_body=shared.UpdateAPIKeyBody(
    label='<value>',
), api_key_id='<value>', team_id='<value>')

if res.api_key_in_db is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `update_api_key_body`                                              | [shared.UpdateAPIKeyBody](../../models/shared/updateapikeybody.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `api_key_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `team_id`                                                          | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |


### Response

**[operations.UpdateAPIKeyLabelV2TeamTeamIDApikeyAPIKeyIDPatchResponse](../../models/operations/updateapikeylabelv2teamteamidapikeyapikeyidpatchresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## update_source_priorities_v2_team_source_priorities_patch

Patch source priorities.

### Example Usage

```python
import vital

s = vital.Vital()


res = s.team.update_source_priorities_v2_team_source_priorities_patch(team_id='<value>')

if res.response_update_source_priorities_v2_team_source_priorities_patch is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `team_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateSourcePrioritiesV2TeamSourcePrioritiesPatchResponse](../../models/operations/updatesourceprioritiesv2teamsourceprioritiespatchresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## update_team_v2_team_team_id_patch

Update team.

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()


res = s.team.update_team_v2_team_team_id_patch(team_update=shared.TeamUpdate(), team_id='<value>')

if res.team_in_db is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `team_update`                                          | [shared.TeamUpdate](../../models/shared/teamupdate.md) | :heavy_check_mark:                                     | N/A                                                    |
| `team_id`                                              | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |


### Response

**[operations.UpdateTeamV2TeamTeamIDPatchResponse](../../models/operations/updateteamv2teamteamidpatchresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

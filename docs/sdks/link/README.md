# Link
(*link*)

### Available Operations

* [check_token_state](#check_token_state) - Check Link Token State
* [check_token_validity](#check_token_validity) - Check Token Valid
* [connect_ble_provider](#connect_ble_provider) - Connect Ble Provider
* [connect_email_auth](#connect_email_auth) - Connect Email Auth
* [connect_email_provider](#connect_email_provider) - Connect Email Auth Provider
* [connect_individual_provider](#connect_individual_provider) - Connect Individual Provider
* [connect_password_auth](#connect_password_auth) - Connect Password Auth
* [connect_provider](#connect_provider) - Connect Provider
* [create_demo_connection](#create_demo_connection) - Create Demo Connection
* [create_token](#create_token) - Create Token
* [exchange_token](#exchange_token) - Exchange Token
* [generate](#generate) - Generate Vital Link Token
* [get_oauth_provider](#get_oauth_provider) - Get Oauth Provider
* [get_providers](#get_providers) - Get Providers
* [start_connect_process](#start_connect_process) - Start Connect Process

## check_token_state

REQUEST_SOURCE: VITAL-LINK
Check link token state - can be hit continuously used as heartbeat

### Example Usage

```python
import vital


s = vital.Vital()


res = s.link.check_token_state()

if res.response_check_link_token_state_v2_link_state_get is not None:
    # handle response
    pass
```


### Response

**[operations.CheckLinkTokenStateV2LinkStateGetResponse](../../models/operations/checklinktokenstatev2linkstategetresponse.md)**


## check_token_validity

Check Token Valid

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.LinkTokenBase(
    oauth_info=shared.LinkTokenBaseOauthInfo(),
    token='string',
)

res = s.link.check_token_validity(req)

if res.response_check_token_valid_v2_link_token_isvalid_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.LinkTokenBase](../../models/shared/linktokenbase.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CheckTokenValidV2LinkTokenIsValidPostResponse](../../models/operations/checktokenvalidv2linktokenisvalidpostresponse.md)**


## connect_ble_provider

REQUEST_SOURCE: CUSTOMER
PROVIDER_TYPE: MANUAL-PROVIDER
This connects auth providers that are password based.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.link.connect_ble_provider(manual_connection_data=shared.ManualConnectionData(
    user_id='string',
), provider=operations.ConnectBleProviderV2LinkProviderManualProviderPostProviderManualProviders.BEURER_BLE)

if res.response_connect_ble_provider_v2_link_provider_manual_provider_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `manual_connection_data`                                                                                                                                                                     | [shared.ManualConnectionData](../../models/shared/manualconnectiondata.md)                                                                                                                   | :heavy_check_mark:                                                                                                                                                                           | N/A                                                                                                                                                                                          |
| `provider`                                                                                                                                                                                   | [operations.ConnectBleProviderV2LinkProviderManualProviderPostProviderManualProviders](../../models/operations/connectbleproviderv2linkprovidermanualproviderpostprovidermanualproviders.md) | :heavy_check_mark:                                                                                                                                                                           | An enumeration.                                                                                                                                                                              |


### Response

**[operations.ConnectBleProviderV2LinkProviderManualProviderPostResponse](../../models/operations/connectbleproviderv2linkprovidermanualproviderpostresponse.md)**


## connect_email_auth

REQUEST_SOURCE: VITAL-LINK
PROVIDER_TYPE: EMAIL-AUTH
This function is hit by vital-link to authenticate a email provider.

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.EmailAuthLink(
    auth_type=shared.AuthType.PASSWORD,
    email='Samara_Haley@gmail.com',
    provider=shared.Providers.BEURER_BLE,
)

res = s.link.connect_email_auth(req)

if res.connection_status is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.EmailAuthLink](../../models/shared/emailauthlink.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.ConnectEmailAuthV2LinkAuthEmailPostResponse](../../models/operations/connectemailauthv2linkauthemailpostresponse.md)**


## connect_email_provider

This connects auth providers that are email based.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.link.connect_email_provider(email_provider_auth_link=shared.EmailProviderAuthLink(
    email='Mabelle_Medhurst23@gmail.com',
), provider=operations.ConnectEmailAuthProviderV2LinkProviderEmailProviderPostProviderEmailProviders.FREESTYLE_LIBRE)

if res.connection_status is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `email_provider_auth_link`                                                                                                                                                                           | [shared.EmailProviderAuthLink](../../models/shared/emailproviderauthlink.md)                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                   | N/A                                                                                                                                                                                                  |
| `provider`                                                                                                                                                                                           | [operations.ConnectEmailAuthProviderV2LinkProviderEmailProviderPostProviderEmailProviders](../../models/operations/connectemailauthproviderv2linkprovideremailproviderpostprovideremailproviders.md) | :heavy_check_mark:                                                                                                                                                                                   | An enumeration.                                                                                                                                                                                      |


### Response

**[operations.ConnectEmailAuthProviderV2LinkProviderEmailProviderPostResponse](../../models/operations/connectemailauthproviderv2linkprovideremailproviderpostresponse.md)**


## connect_individual_provider

This connects auth providers that are password based.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.link.connect_individual_provider(individual_provider_data=shared.IndividualProviderData(
    password='U7xJdvB5pT6rvW2',
    username='Chanel73',
), provider=operations.ConnectIndividualProviderV2LinkProviderPasswordProviderPostProviderPasswordProviders.RENPHO, x_vital_link_client_region='string')

if res.provider_link_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                                          | Type                                                                                                                                                                                                               | Required                                                                                                                                                                                                           | Description                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `individual_provider_data`                                                                                                                                                                                         | [shared.IndividualProviderData](../../models/shared/individualproviderdata.md)                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                |
| `provider`                                                                                                                                                                                                         | [operations.ConnectIndividualProviderV2LinkProviderPasswordProviderPostProviderPasswordProviders](../../models/operations/connectindividualproviderv2linkproviderpasswordproviderpostproviderpasswordproviders.md) | :heavy_check_mark:                                                                                                                                                                                                 | An enumeration.                                                                                                                                                                                                    |
| `x_vital_link_client_region`                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                |


### Response

**[operations.ConnectIndividualProviderV2LinkProviderPasswordProviderPostResponse](../../models/operations/connectindividualproviderv2linkproviderpasswordproviderpostresponse.md)**


## connect_password_auth

REQUEST_SOURCE: VITAL-LINK
PROVIDER_TYPE: PASSWORD-AUTH
This function is hit by vital-link to authenticate a password provider.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.link.connect_password_auth(password_auth_link=shared.PasswordAuthLink(
    auth_type=shared.AuthType.PASSWORD,
    password='HuGgl1Kl3rSJCBn',
    provider=shared.Providers.WAHOO,
    username='Brett32',
), x_vital_link_client_region='string')

if res.connection_status is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `password_auth_link`                                               | [shared.PasswordAuthLink](../../models/shared/passwordauthlink.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `x_vital_link_client_region`                                       | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |


### Response

**[operations.ConnectPasswordAuthV2LinkAuthPostResponse](../../models/operations/connectpasswordauthv2linkauthpostresponse.md)**


## connect_provider

REQUEST_SOURCE: VITAL-LINK
PROVIDER_TYPE: OAUTH
Connect oauth providers

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.link.connect_provider(provider='string', x_vital_sdk_no_redirect='string')

if res.response_connect_provider_v2_link_connect_provider_get is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `provider`                                       | *str*                                            | :heavy_check_mark:                               | Provider slug. e.g., `oura`, `fitbit`, `garmin`. |
| `x_vital_sdk_no_redirect`                        | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |


### Response

**[operations.ConnectProviderV2LinkConnectProviderGetResponse](../../models/operations/connectproviderv2linkconnectprovidergetresponse.md)**


## create_demo_connection

POST Connect the given Vital user to a demo provider.

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.DemoConnectionCreationPayload(
    provider=shared.DemoProviders.APPLE_HEALTH_KIT,
    user_id='string',
)

res = s.link.create_demo_connection(req)

if res.demo_connection_status is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.DemoConnectionCreationPayload](../../models/shared/democonnectioncreationpayload.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateDemoConnectionV2LinkConnectDemoPostResponse](../../models/operations/createdemoconnectionv2linkconnectdemopostresponse.md)**


## create_token

Generate a token to invite a user of Vital mobile app to your team

### Example Usage

```python
import vital
import dateutil.parser
from vital.models import operations

s = vital.Vital()


res = s.link.create_token(user_id='2795b4e3-bfe4-4e25-a003-d249bbaf85eb', expires_at=dateutil.parser.isoparse('2021-12-10T10:53:22.771Z'))

if res.vital_token_created_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `user_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `expires_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |


### Response

**[operations.CreateTokenV2LinkCodeCreatePostResponse](../../models/operations/createtokenv2linkcodecreatepostresponse.md)**


## exchange_token

Redeem an invite token for an api key

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.link.exchange_token(code='string')

if res.vital_token_exchange_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `code`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ExchangeTokenV2LinkCodeExchangePostResponse](../../models/operations/exchangetokenv2linkcodeexchangepostresponse.md)**


## generate

Endpoint to generate a user link token, to be used throughout the vital
link process. The vital link token is a one time use token, that
expires after 10 minutes. If you would like vital-link widget to launch
with a specific provider, pass in a provider in the body. If you would
like to redirect to a custom url after successful or error connection,
pass in your own custom redirect_url parameter.

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.LinkTokenExchange(
    filter_on_providers=[
        shared.Providers.ACCUCHEK_BLE,
    ],
    user_key='8785044a-13a2-491c-af01-0449531f483f',
)

res = s.link.generate(req)

if res.link_token_exchange_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.LinkTokenExchange](../../models/shared/linktokenexchange.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.GenerateVitalLinkTokenV2LinkTokenPostResponse](../../models/operations/generatevitallinktokenv2linktokenpostresponse.md)**


## get_oauth_provider

This endpoint generates an OAuth link for oauth provider

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.link.get_oauth_provider(oauth_provider=shared.OAuthProviders.POLAR)

if res.source is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `oauth_provider`                                               | [shared.OAuthProviders](../../models/shared/oauthproviders.md) | :heavy_check_mark:                                             | An enumeration.                                                |


### Response

**[operations.GetOauthProviderV2LinkProviderOauthOauthProviderGetResponse](../../models/operations/getoauthproviderv2linkprovideroauthoauthprovidergetresponse.md)**


## get_providers

GET List of all available providers given the generated link token.

### Example Usage

```python
import vital


s = vital.Vital()


res = s.link.get_providers()

if res.source_links is not None:
    # handle response
    pass
```


### Response

**[operations.GetProvidersV2LinkProvidersGetResponse](../../models/operations/getprovidersv2linkprovidersgetresponse.md)**


## start_connect_process

REQUEST_SOURCE: VITAL-LINK
Start link token process

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.BeginLinkTokenRequest(
    link_token='string',
    provider=shared.Providers.PELOTON,
)

res = s.link.start_connect_process(req)

if res.response_start_connect_process_v2_link_start_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.BeginLinkTokenRequest](../../models/shared/beginlinktokenrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.StartConnectProcessV2LinkStartPostResponse](../../models/operations/startconnectprocessv2linkstartpostresponse.md)**


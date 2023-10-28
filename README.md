# Vital Python SDK

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/vital-python.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/vital-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/vital-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import vital


s = vital.Vital()


res = s.vital.robots_robots_txt_get()

if res.robots_robots_txt_get_200_text_plain_string is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations

### [Vital SDK](docs/sdks/vital/README.md)

* [robots_robots_txt_get](docs/sdks/vital/README.md#robots_robots_txt_get) - Robots

### [insurance](docs/sdks/insurance/README.md)

* [search_diagnosis](docs/sdks/insurance/README.md#search_diagnosis) - Search Diagnosis
* [search_insurance_payor_info](docs/sdks/insurance/README.md#search_insurance_payor_info) - Search Insurance Payor Information

### [lab_tests](docs/sdks/labtests/README.md)

* [create](docs/sdks/labtests/README.md#create) - Create Lab Test For Team
* [get_labs](docs/sdks/labtests/README.md#get_labs) - Get Labs
* [get_marker_by_provider](docs/sdks/labtests/README.md#get_marker_by_provider) - Get Markers By Provider Id
* [get_markers](docs/sdks/labtests/README.md#get_markers) - Get Markers
* [list](docs/sdks/labtests/README.md#list) - Get Lab Tests For Team

### [link](docs/sdks/link/README.md)

* [check_token_state](docs/sdks/link/README.md#check_token_state) - Check Link Token State
* [check_token_validity](docs/sdks/link/README.md#check_token_validity) - Check Token Valid
* [connect_ble_provider](docs/sdks/link/README.md#connect_ble_provider) - Connect Ble Provider
* [connect_email_auth](docs/sdks/link/README.md#connect_email_auth) - Connect Email Auth
* [connect_email_provider](docs/sdks/link/README.md#connect_email_provider) - Connect Email Auth Provider
* [connect_individual_provider](docs/sdks/link/README.md#connect_individual_provider) - Connect Individual Provider
* [connect_password_auth](docs/sdks/link/README.md#connect_password_auth) - Connect Password Auth
* [connect_provider](docs/sdks/link/README.md#connect_provider) - Connect Provider
* [create_demo_connection](docs/sdks/link/README.md#create_demo_connection) - Create Demo Connection
* [create_token](docs/sdks/link/README.md#create_token) - Create Token
* [exchange_token](docs/sdks/link/README.md#exchange_token) - Exchange Token
* [generate](docs/sdks/link/README.md#generate) - Generate Vital Link Token
* [get_oauth_provider](docs/sdks/link/README.md#get_oauth_provider) - Get Oauth Provider
* [get_providers](docs/sdks/link/README.md#get_providers) - Get Providers
* [start_connect_process](docs/sdks/link/README.md#start_connect_process) - Start Connect Process

### [order](docs/sdks/order/README.md)

* [book_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_book_post](docs/sdks/order/README.md#book_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_book_post) - Book Phlebotomy Appointment
* [cancel_order_v3_order_order_id_cancel_post](docs/sdks/order/README.md#cancel_order_v3_order_order_id_cancel_post) - Cancel Order
* [cancel_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_cancel_patch](docs/sdks/order/README.md#cancel_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_cancel_patch) - Cancel Phlebotomy Appointment
* [create](docs/sdks/order/README.md#create) - Create Order
* [create_testkit](docs/sdks/order/README.md#create_testkit) - Create Testkit Order
* [dispatch_status](docs/sdks/order/README.md#dispatch_status) - Dispatch Order Status
* [get](docs/sdks/order/README.md#get) - Get Order
* [get_appointment_availability](docs/sdks/order/README.md#get_appointment_availability) - Get Order Appointment Availability
* [get_area_info](docs/sdks/order/README.md#get_area_info) - Get Area Info
* [get_lab_test_result](docs/sdks/order/README.md#get_lab_test_result) - Get Lab Test Result
* [get_lab_test_result_metadata](docs/sdks/order/README.md#get_lab_test_result_metadata) - Get Lab Test Result Metadata
* [get_lab_test_result_raw](docs/sdks/order/README.md#get_lab_test_result_raw) - Get Lab Test Result Raw
* [get_phlebotomy_appointment](docs/sdks/order/README.md#get_phlebotomy_appointment) - Get Phlebotomy Appointment
* [get_phlebotomy_cancellation_reasons](docs/sdks/order/README.md#get_phlebotomy_cancellation_reasons) - Get Phlebotomy Appointment Cancellation Reasons
* [get_requisition_url](docs/sdks/order/README.md#get_requisition_url) - Get Order Requisition Url
* [order_process_simulate_v3_order_order_id_test_post](docs/sdks/order/README.md#order_process_simulate_v3_order_order_id_test_post) - Order Process Simulate
* [process_testkit_order_v3_order_testkit_process_team_id_order_id_post](docs/sdks/order/README.md#process_testkit_order_v3_order_testkit_process_team_id_order_id_post) - Process Testkit Order
* [process_testkit_ship_hero_order_shipped_v3_order_testkit_webhook_shiphero_shipment_update_post](docs/sdks/order/README.md#process_testkit_ship_hero_order_shipped_v3_order_testkit_webhook_shiphero_shipment_update_post) - Process Testkit Ship Hero Order Shipped
* [register_testkit_v3_order_testkit_register_post](docs/sdks/order/README.md#register_testkit_v3_order_testkit_register_post) - Register Testkit
* [reschedule_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_reschedule_patch](docs/sdks/order/README.md#reschedule_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_reschedule_patch) - Reschedule Phlebotomy Appointment
* [sync_testkit_order_status_v3_order_testkit_status_post](docs/sdks/order/README.md#sync_testkit_order_status_v3_order_testkit_status_post) - Sync Testkit Order Status

### [orders](docs/sdks/orders/README.md)

* [list](docs/sdks/orders/README.md#list) - Get Orders

### [physician](docs/sdks/physician/README.md)

* [review_openloop_v2_physician_review_openloop_post](docs/sdks/physician/README.md#review_openloop_v2_physician_review_openloop_post) - Review Openloop

### [providers](docs/sdks/providers/README.md)

* [list](docs/sdks/providers/README.md#list) - Get List Of Providers

### [summary](docs/sdks/summary/README.md)

* [get_meals](docs/sdks/summary/README.md#get_meals) - Get Meals
* [get_user_activity](docs/sdks/summary/README.md#get_user_activity) - Get User Activity
* [get_user_activity_raw](docs/sdks/summary/README.md#get_user_activity_raw) - Get User Activity Raw
* [get_user_body](docs/sdks/summary/README.md#get_user_body) - Get User Body
* [get_user_body_raw](docs/sdks/summary/README.md#get_user_body_raw) - Get User Body Raw
* [get_user_devices_raw](docs/sdks/summary/README.md#get_user_devices_raw) - Get User Devices Raw
* [get_user_profile](docs/sdks/summary/README.md#get_user_profile) - Get User Profile
* [get_user_profile_raw](docs/sdks/summary/README.md#get_user_profile_raw) - Get User Profile Raw
* [get_user_sleep](docs/sdks/summary/README.md#get_user_sleep) - Get User Sleep
* [get_user_sleep_raw](docs/sdks/summary/README.md#get_user_sleep_raw) - Get User Sleep Raw
* [get_user_sleep_stream](docs/sdks/summary/README.md#get_user_sleep_stream) - Get User Sleep Stream
* [get_user_workouts](docs/sdks/summary/README.md#get_user_workouts) - Get User Workouts
* [get_user_workouts_raw](docs/sdks/summary/README.md#get_user_workouts_raw) - Get User Workouts Raw
* [post_user_activity](docs/sdks/summary/README.md#post_user_activity) - Post User Activity
* [post_user_body](docs/sdks/summary/README.md#post_user_body) - Post User Body
* [post_user_profile](docs/sdks/summary/README.md#post_user_profile) - Post User Profile
* [post_user_sleep](docs/sdks/summary/README.md#post_user_sleep) - Post User Sleep
* [post_user_workout](docs/sdks/summary/README.md#post_user_workout) - Post User Workout

### [team](docs/sdks/team/README.md)

* [create](docs/sdks/team/README.md#create) - Create Team
* [create_api_key](docs/sdks/team/README.md#create_api_key) - Create Api Key
* [create_priority](docs/sdks/team/README.md#create_priority) - Create Priority
* [delete_api_key](docs/sdks/team/README.md#delete_api_key) - Delete Api Key
* [get](docs/sdks/team/README.md#get) - Get Team
* [get_api_keys](docs/sdks/team/README.md#get_api_keys) - Get Api Keys For Team
* [get_config](docs/sdks/team/README.md#get_config) - Get Team Config
* [get_source_priorities](docs/sdks/team/README.md#get_source_priorities) - Get Source Priorities
* [get_user_count](docs/sdks/team/README.md#get_user_count) - Get Team User Count
* [get_webhook_url](docs/sdks/team/README.md#get_webhook_url) - Get Svix Webhook Url
* [rotate_api_key_v2_team_team_id_apikey_api_key_id_rotate_patch](docs/sdks/team/README.md#rotate_api_key_v2_team_team_id_apikey_api_key_id_rotate_patch) - Rotate Api Key
* [search_users_by_uuid](docs/sdks/team/README.md#search_users_by_uuid) - Search Team Users By Uuid Or Client User Id
* [update_api_key_label_v2_team_team_id_apikey_api_key_id_patch](docs/sdks/team/README.md#update_api_key_label_v2_team_team_id_apikey_api_key_id_patch) - Update Api Key Label
* [update_source_priorities_v2_team_source_priorities_patch](docs/sdks/team/README.md#update_source_priorities_v2_team_source_priorities_patch) - Update Source Priorities
* [update_team_v2_team_team_id_patch](docs/sdks/team/README.md#update_team_v2_team_team_id_patch) - Update Team

### [timeseries](docs/sdks/timeseries/README.md)

* [get_blood_oxygen](docs/sdks/timeseries/README.md#get_blood_oxygen) - Get Timeseries Resource Data
* [get_blood_pressure](docs/sdks/timeseries/README.md#get_blood_pressure) - Get Timeseries Resource Data
* [get_caffeine](docs/sdks/timeseries/README.md#get_caffeine) - Get Timeseries Resource Data
* [get_calories_active](docs/sdks/timeseries/README.md#get_calories_active) - Get Timeseries Resource Data
* [get_calories_basal](docs/sdks/timeseries/README.md#get_calories_basal) - Get Timeseries Resource Data
* [get_cholesterol_all](docs/sdks/timeseries/README.md#get_cholesterol_all) - Get Timeseries Resource Data
* [get_cholesterol_hdl](docs/sdks/timeseries/README.md#get_cholesterol_hdl) - Get Timeseries Resource Data
* [get_cholesterol_ldl](docs/sdks/timeseries/README.md#get_cholesterol_ldl) - Get Timeseries Resource Data
* [get_distance](docs/sdks/timeseries/README.md#get_distance) - Get Timeseries Resource Data
* [get_floors_climbed](docs/sdks/timeseries/README.md#get_floors_climbed) - Get Timeseries Resource Data
* [get_glucose](docs/sdks/timeseries/README.md#get_glucose) - Get Timeseries Resource Data
* [get_heartrate](docs/sdks/timeseries/README.md#get_heartrate) - Get Timeseries Resource Data
* [get_hrv](docs/sdks/timeseries/README.md#get_hrv) - Get Timeseries Resource Data
* [get_hypnogram](docs/sdks/timeseries/README.md#get_hypnogram) - Get Timeseries Resource Data
* [get_ige](docs/sdks/timeseries/README.md#get_ige) - Get Timeseries Resource Data
* [get_igg](docs/sdks/timeseries/README.md#get_igg) - Get Timeseries Resource Data
* [get_mindfulness_minutes](docs/sdks/timeseries/README.md#get_mindfulness_minutes) - Get Timeseries Resource Data
* [get_respiratory_rate](docs/sdks/timeseries/README.md#get_respiratory_rate) - Get Timeseries Resource Data
* [get_steps](docs/sdks/timeseries/README.md#get_steps) - Get Timeseries Resource Data
* [get_total_cholesterol](docs/sdks/timeseries/README.md#get_total_cholesterol) - Get Timeseries Resource Data
* [get_triglycerides](docs/sdks/timeseries/README.md#get_triglycerides) - Get Timeseries Resource Data
* [get_user_sleep_stream](docs/sdks/timeseries/README.md#get_user_sleep_stream) - Get User Sleep Stream
* [get_user_workouts](docs/sdks/timeseries/README.md#get_user_workouts) - Get User Workouts
* [get_water](docs/sdks/timeseries/README.md#get_water) - Get Timeseries Resource Data
* [post_blood_pressure](docs/sdks/timeseries/README.md#post_blood_pressure) - Post User Blood Pressure
* [post_vitals](docs/sdks/timeseries/README.md#post_vitals) - Post User Vitals

### [user](docs/sdks/user/README.md)

* [create_user](docs/sdks/user/README.md#create_user) - Create User
* [delete](docs/sdks/user/README.md#delete) - Delete User
* [deregister_provider_v2_user_user_id_provider_delete](docs/sdks/user/README.md#deregister_provider_v2_user_user_id_provider_delete) - Deregister Provider
* [get](docs/sdks/user/README.md#get) - Get User
* [get_all](docs/sdks/user/README.md#get_all) - Get Teams Users
* [get_connected_providers](docs/sdks/user/README.md#get_connected_providers) - Get Connected Providers
* [get_metrics](docs/sdks/user/README.md#get_metrics) - Get Teams Metrics
* [get_sign_in_token](docs/sdks/user/README.md#get_sign_in_token) - Get User Sign In Token
* [patch_user_v2_user_user_id_patch](docs/sdks/user/README.md#patch_user_v2_user_user_id_patch) - Patch User
* [refresh_user_id_v2_user_refresh_user_id_post](docs/sdks/user/README.md#refresh_user_id_v2_user_refresh_user_id_post) - Refresh User Id
* [resolve_by_user_id](docs/sdks/user/README.md#resolve_by_user_id) - Get User By Client User Id
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


## Example

```python
import vital
from vital.models import operations

s = vital.Vital()


res = None
try:
    res = s.insurance.search_diagnosis(diagnosis_query='string')

except (HTTPValidationError) as e:
    print(e) # handle exception


if res.client_facing_diagnosis_informations is not None:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.tryvital.io` | None |

For example:


```python
import vital


s = vital.Vital(
    server_idx=0
)


res = s.vital.robots_robots_txt_get()

if res.robots_robots_txt_get_200_text_plain_string is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import vital


s = vital.Vital(
    server_url="https://api.tryvital.io"
)


res = s.vital.robots_robots_txt_get()

if res.robots_robots_txt_get_200_text_plain_string is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import vital
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = vital.Vital(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)

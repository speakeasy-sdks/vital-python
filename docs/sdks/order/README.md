# Order
(*order*)

### Available Operations

* [book_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_book_post](#book_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_book_post) - Book Phlebotomy Appointment
* [cancel_order_v3_order_order_id_cancel_post](#cancel_order_v3_order_order_id_cancel_post) - Cancel Order
* [cancel_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_cancel_patch](#cancel_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_cancel_patch) - Cancel Phlebotomy Appointment
* [create](#create) - Create Order
* [create_testkit](#create_testkit) - Create Testkit Order
* [dispatch_status](#dispatch_status) - Dispatch Order Status
* [get](#get) - Get Order
* [get_appointment_availability](#get_appointment_availability) - Get Order Appointment Availability
* [get_area_info](#get_area_info) - Get Area Info
* [get_lab_test_result](#get_lab_test_result) - Get Lab Test Result
* [get_lab_test_result_metadata](#get_lab_test_result_metadata) - Get Lab Test Result Metadata
* [get_lab_test_result_raw](#get_lab_test_result_raw) - Get Lab Test Result Raw
* [get_phlebotomy_appointment](#get_phlebotomy_appointment) - Get Phlebotomy Appointment
* [get_phlebotomy_cancellation_reasons](#get_phlebotomy_cancellation_reasons) - Get Phlebotomy Appointment Cancellation Reasons
* [get_requisition_url](#get_requisition_url) - Get Order Requisition Url
* [order_process_simulate_v3_order_order_id_test_post](#order_process_simulate_v3_order_order_id_test_post) - Order Process Simulate
* [process_testkit_order_v3_order_testkit_process_team_id_order_id_post](#process_testkit_order_v3_order_testkit_process_team_id_order_id_post) - Process Testkit Order
* [process_testkit_ship_hero_order_shipped_v3_order_testkit_webhook_shiphero_shipment_update_post](#process_testkit_ship_hero_order_shipped_v3_order_testkit_webhook_shiphero_shipment_update_post) - Process Testkit Ship Hero Order Shipped
* [register_testkit_v3_order_testkit_register_post](#register_testkit_v3_order_testkit_register_post) - Register Testkit
* [reschedule_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_reschedule_patch](#reschedule_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_reschedule_patch) - Reschedule Phlebotomy Appointment
* [sync_testkit_order_status_v3_order_testkit_status_post](#sync_testkit_order_status_v3_order_testkit_status_post) - Sync Testkit Order Status

## book_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_book_post

Book an at-home phlebotomy appointment.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()

req = operations.BookPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentBookPostRequest(
    appointment_booking_request=shared.AppointmentBookingRequest(
        booking_key='how index Electric',
    ),
    order_id='0b1d8151-82e6-4c0e-bd72-ca79bcf3d5ba',
)

res = s.order.book_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_book_post(req)

if res.client_facing_appointment is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                        | Type                                                                                                                                                                                             | Required                                                                                                                                                                                         | Description                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                        | [operations.BookPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentBookPostRequest](../../models/operations/bookphlebotomyappointmentv3orderorderidphlebotomyappointmentbookpostrequest.md) | :heavy_check_mark:                                                                                                                                                                               | The request object to use for the request.                                                                                                                                                       |


### Response

**[operations.BookPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentBookPostResponse](../../models/operations/bookphlebotomyappointmentv3orderorderidphlebotomyappointmentbookpostresponse.md)**


## cancel_order_v3_order_order_id_cancel_post

POST cancel order

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.CancelOrderV3OrderOrderIDCancelPostRequest(
    order_id='b9d919c2-b9aa-4759-bba5-fb974a744f9a',
)

res = s.order.cancel_order_v3_order_order_id_cancel_post(req)

if res.post_order_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.CancelOrderV3OrderOrderIDCancelPostRequest](../../models/operations/cancelorderv3orderorderidcancelpostrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.CancelOrderV3OrderOrderIDCancelPostResponse](../../models/operations/cancelorderv3orderorderidcancelpostresponse.md)**


## cancel_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_cancel_patch

Cancel a previously booked at-home phlebotomy appointment.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()

req = operations.CancelPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentCancelPatchRequest(
    appointment_cancel_request=shared.AppointmentCancelRequest(
        cancellation_reason_id='Sandy Minivan',
    ),
    order_id='528ddb0d-27a7-4e90-9ccf-3b9448c5e365',
)

res = s.order.cancel_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_cancel_patch(req)

if res.client_facing_appointment is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                  | Type                                                                                                                                                                                                       | Required                                                                                                                                                                                                   | Description                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                  | [operations.CancelPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentCancelPatchRequest](../../models/operations/cancelphlebotomyappointmentv3orderorderidphlebotomyappointmentcancelpatchrequest.md) | :heavy_check_mark:                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                 |


### Response

**[operations.CancelPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentCancelPatchResponse](../../models/operations/cancelphlebotomyappointmentv3orderorderidphlebotomyappointmentcancelpatchresponse.md)**


## create

POST create new order

### Example Usage

```python
import vital
import dateutil.parser
from vital.models import shared

s = vital.Vital()

req = shared.CreateOrderRequestCompatible(
    consents=[
        shared.Consent(
            consent_type=shared.ConsentType.MOBILE_TERMS_AND_CONDITIONS,
        ),
    ],
    health_insurance=shared.HealthInsuranceCreateRequest(
        shared.Jpeg(
            content='\pG;-j\'}kD'.encode(),
            content_type=shared.JpegContentType.IMAGE_JPEG,
        ),
        diagnosis_codes=[
            'technology',
        ],
        shared.Jpeg(
            content='K0=)cjplTW'.encode(),
            content_type=shared.JpegContentType.IMAGE_JPEG,
        ),
        shared.Png(
            content='fNz^B#9t"Q'.encode(),
            content_type=shared.PngContentType.IMAGE_PNG,
        ),
        responsible_details=shared.HealthInsuranceCreateRequestPersonDetails(
            address=shared.Address(
                city='East Cory',
                country='Portugal',
                first_line='Fiat',
                state='Grocery Borders Northwest',
                zip='Kentucky animated',
            ),
            first_name='Roosevelt',
            last_name='Mueller',
            phone_number='Senior Mouse West',
        ),
    ),
    lab_test_id='8504aa8c-e67b-47c4-9cf2-4bdebcfc23e7',
    patient_address=shared.PatientAddressCompatible(
        city='Jefferson City',
        country='Zimbabwe',
        state='Electronic digital',
        street='Arne Via',
        zip='Mongolia Maine sexy',
    ),
    patient_details=shared.PatientDetails(
        dob=dateutil.parser.isoparse('2022-10-01T18:30:31.591Z'),
        email='Josiane81@yahoo.com',
        first_name='Hailee',
        gender=shared.Gender.OTHER,
        last_name='Bradtke',
        phone_number='Toys Electric readily',
    ),
    physician=shared.PhysicianCreateRequest(
        first_name='Abner',
        last_name='Steuber',
        licensed_states=[
            'yet',
        ],
        npi='modest aged Account',
        shared.Png(
            content='_A`H,`:\'+q'.encode(),
            content_type=shared.PngContentType.IMAGE_PNG,
        ),
    ),
    user_id='6fd9e403-c67b-4cfa-9731-944d98437394',
)

res = s.order.create(req)

if res.post_order_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.CreateOrderRequestCompatible](../../models/shared/createorderrequestcompatible.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateOrderV3OrderPostResponse](../../models/operations/createorderv3orderpostresponse.md)**


## create_testkit

Creates an order for an unregistered testkit

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.CreateRegistrableTestkitOrderRequest(
    lab_test_id='eb480e87-d170-4ada-8df4-8f4bbca14aec',
    shipping_details=shared.ShippingAddress(
        city='West Esmeraldaborough',
        country='Antarctica (the territory South of 60 deg S)',
        first_line='Bedfordshire Research',
        phone_number='reinvent',
        receiver_name='Minivan',
        state='Soul plus',
        zip='kookily capacitor er',
    ),
    user_id='df371333-0afb-4f06-a4cd-2f36154eee26',
)

res = s.order.create_testkit(req)

if res.post_order_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [shared.CreateRegistrableTestkitOrderRequest](../../models/shared/createregistrabletestkitorderrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.CreateTestkitOrderV3OrderTestkitPostResponse](../../models/operations/createtestkitorderv3ordertestkitpostresponse.md)**


## dispatch_status

Dispatch Order Status

### Example Usage

```python
import vital


s = vital.Vital()


res = s.order.dispatch_status()

if res.response_dispatch_order_status_v3_order_dispatch_status_checks_post is not None:
    # handle response
```


### Response

**[operations.DispatchOrderStatusV3OrderDispatchStatusChecksPostResponse](../../models/operations/dispatchorderstatusv3orderdispatchstatuscheckspostresponse.md)**


## get

GET individual order by ID.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetOrderV3OrderOrderIDGetRequest(
    order_id='b18d8d81-fd7b-4764-a31e-475cb1f36591',
)

res = s.order.get(req)

if res.client_facing_order is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetOrderV3OrderOrderIDGetRequest](../../models/operations/getorderv3orderorderidgetrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetOrderV3OrderOrderIDGetResponse](../../models/operations/getorderv3orderorderidgetresponse.md)**


## get_appointment_availability

Return the available time slots to book an appointment with a phlebotomist
for the given address and order.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetOrderAppointmentAvailabilityV3OrderOrderIDPhlebotomyAppointmentAvailabilityPostRequest(
    request_body=operations.GetOrderAppointmentAvailabilityV3OrderOrderIDPhlebotomyAppointmentAvailabilityPostUSAddress(
        city='Beierfurt',
        first_line='Gasoline',
        state='quietly',
        zip_code='90180-6043',
    ),
    order_id='be1f658f-f11c-4cd4-b893-8a333321e842',
)

res = s.order.get_appointment_availability(req)

if res.appointment_availability_slots is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                                    | [operations.GetOrderAppointmentAvailabilityV3OrderOrderIDPhlebotomyAppointmentAvailabilityPostRequest](../../models/operations/getorderappointmentavailabilityv3orderorderidphlebotomyappointmentavailabilitypostrequest.md) | :heavy_check_mark:                                                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                                                   |


### Response

**[operations.GetOrderAppointmentAvailabilityV3OrderOrderIDPhlebotomyAppointmentAvailabilityPostResponse](../../models/operations/getorderappointmentavailabilityv3orderorderidphlebotomyappointmentavailabilitypostresponse.md)**


## get_area_info

GET information about an area with respect to lab-testing.

Information returned:
* Whether a given zip code is served by our Phlebotomy network.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetAreaInfoV3OrderAreaInfoGetRequest(
    zip_code='94836',
)

res = s.order.get_area_info(req)

if res.area_info is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAreaInfoV3OrderAreaInfoGetRequest](../../models/operations/getareainfov3orderareainfogetrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAreaInfoV3OrderAreaInfoGetResponse](../../models/operations/getareainfov3orderareainfogetresponse.md)**


## get_lab_test_result

This endpoint returns the lab results for the order.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetLabTestResultV3OrderOrderIDResultPdfGetRequest(
    order_id='c9229487-8f86-47ef-848e-7eb7243713ad',
)

res = s.order.get_lab_test_result(req)

if res.response_get_lab_test_result_v3_order_order_id_result_pdf_get is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetLabTestResultV3OrderOrderIDResultPdfGetRequest](../../models/operations/getlabtestresultv3orderorderidresultpdfgetrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetLabTestResultV3OrderOrderIDResultPdfGetResponse](../../models/operations/getlabtestresultv3orderorderidresultpdfgetresponse.md)**


## get_lab_test_result_metadata

Return metadata related to order results, such as lab metadata,
provider and sample dates.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetLabTestResultMetadataV3OrderOrderIDResultMetadataGetRequest(
    order_id='daf5fdc5-7c54-4772-826b-69600571af0f',
)

res = s.order.get_lab_test_result_metadata(req)

if res.lab_results_metadata is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.GetLabTestResultMetadataV3OrderOrderIDResultMetadataGetRequest](../../models/operations/getlabtestresultmetadatav3orderorderidresultmetadatagetrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |


### Response

**[operations.GetLabTestResultMetadataV3OrderOrderIDResultMetadataGetResponse](../../models/operations/getlabtestresultmetadatav3orderorderidresultmetadatagetresponse.md)**


## get_lab_test_result_raw

Return both metadata and raw json test data

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetLabTestResultRawV3OrderOrderIDResultGetRequest(
    order_id='2cfa7265-4a8d-45d9-b8ea-42e844b02385',
)

res = s.order.get_lab_test_result_raw(req)

if res.lab_results_raw is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetLabTestResultRawV3OrderOrderIDResultGetRequest](../../models/operations/getlabtestresultrawv3orderorderidresultgetrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetLabTestResultRawV3OrderOrderIDResultGetResponse](../../models/operations/getlabtestresultrawv3orderorderidresultgetresponse.md)**


## get_phlebotomy_appointment

Get the appointment associated with an order.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentGetRequest(
    order_id='3e95493c-2969-4eab-9aaf-61adbf59533c',
)

res = s.order.get_phlebotomy_appointment(req)

if res.client_facing_appointment is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                            | [operations.GetPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentGetRequest](../../models/operations/getphlebotomyappointmentv3orderorderidphlebotomyappointmentgetrequest.md) | :heavy_check_mark:                                                                                                                                                                   | The request object to use for the request.                                                                                                                                           |


### Response

**[operations.GetPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentGetResponse](../../models/operations/getphlebotomyappointmentv3orderorderidphlebotomyappointmentgetresponse.md)**


## get_phlebotomy_cancellation_reasons

Get the list of reasons for cancelling an at-home phlebotomy appointment.

### Example Usage

```python
import vital


s = vital.Vital()


res = s.order.get_phlebotomy_cancellation_reasons()

if res.client_facing_appointment_cancellation_reasons is not None:
    # handle response
```


### Response

**[operations.GetPhlebotomyAppointmentCancellationReasonsV3OrderPhlebotomyAppointmentCancellationReasonsGetResponse](../../models/operations/getphlebotomyappointmentcancellationreasonsv3orderphlebotomyappointmentcancellationreasonsgetresponse.md)**


## get_requisition_url

GET requisition pdf for an order

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.GetOrderRequisitionURLV3OrderOrderIDRequisitionPdfGetRequest(
    order_id='bfbbc5db-bd5f-47b5-9a88-6ef4ccfaf335',
)

res = s.order.get_requisition_url(req)

if res.get_order_requisition_url_v3_order_order_id_requisition_pdf_get_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                          | [operations.GetOrderRequisitionURLV3OrderOrderIDRequisitionPdfGetRequest](../../models/operations/getorderrequisitionurlv3orderorderidrequisitionpdfgetrequest.md) | :heavy_check_mark:                                                                                                                                                 | The request object to use for the request.                                                                                                                         |


### Response

**[operations.GetOrderRequisitionURLV3OrderOrderIDRequisitionPdfGetResponse](../../models/operations/getorderrequisitionurlv3orderorderidrequisitionpdfgetresponse.md)**


## order_process_simulate_v3_order_order_id_test_post

Get available test kits.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()

req = operations.OrderProcessSimulateV3OrderOrderIDTestPostRequest(
    order_id='03c5e046-8598-4154-ab3e-444d34fe425a',
)

res = s.order.order_process_simulate_v3_order_order_id_test_post(req)

if res.response_order_process_simulate_v3_order_order_id_test_post is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.OrderProcessSimulateV3OrderOrderIDTestPostRequest](../../models/operations/orderprocesssimulatev3orderorderidtestpostrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.OrderProcessSimulateV3OrderOrderIDTestPostResponse](../../models/operations/orderprocesssimulatev3orderorderidtestpostresponse.md)**


## process_testkit_order_v3_order_testkit_process_team_id_order_id_post

POST Create shipment for order

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()

req = operations.ProcessTestkitOrderV3OrderTestkitProcessTeamIDOrderIDPostRequest(
    order_id='21061e75-f548-42fd-90f0-d372d63dff6e',
    team_id='26a256a9-b0f5-4854-8814-40907e852835',
)

res = s.order.process_testkit_order_v3_order_testkit_process_team_id_order_id_post(req)

if res.response_process_testkit_order_v3_order_testkit_process_team_id_order_id_post is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.ProcessTestkitOrderV3OrderTestkitProcessTeamIDOrderIDPostRequest](../../models/operations/processtestkitorderv3ordertestkitprocessteamidorderidpostrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.ProcessTestkitOrderV3OrderTestkitProcessTeamIDOrderIDPostResponse](../../models/operations/processtestkitorderv3ordertestkitprocessteamidorderidpostresponse.md)**


## process_testkit_ship_hero_order_shipped_v3_order_testkit_webhook_shiphero_shipment_update_post

Process Testkit Ship Hero Order Shipped

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.ShipmentWebhookUpdate(
    fulfillment=shared.Fulfillment(
        order_number='Shoals',
        order_uuid='City Southeast',
    ),
    webhook_type=shared.ShipmentWebhookUpdateWebhookType.SHIPMENT_UPDATE,
)

res = s.order.process_testkit_ship_hero_order_shipped_v3_order_testkit_webhook_shiphero_shipment_update_post(req)

if res.response_process_testkit_ship_hero_order_shipped_v3_order_testkit_webhook_shiphero_shipment_update_post is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.ShipmentWebhookUpdate](../../models/shared/shipmentwebhookupdate.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ProcessTestkitShipHeroOrderShippedV3OrderTestkitWebhookShipheroShipmentUpdatePostResponse](../../models/operations/processtestkitshipheroordershippedv3ordertestkitwebhookshipheroshipmentupdatepostresponse.md)**


## register_testkit_v3_order_testkit_register_post

Register Testkit

### Example Usage

```python
import vital
import dateutil.parser
from vital.models import shared

s = vital.Vital()

req = shared.RegisterTestkitRequest(
    consents=[
        shared.Consent(
            consent_type=shared.ConsentType.MOBILE_TERMS_AND_CONDITIONS,
        ),
    ],
    patient_address=shared.PatientAddressCompatible(
        city='Phoenix',
        country='Netherlands',
        state='software',
        street='Cole Motorway',
        zip='olive plagiarism visualize',
    ),
    patient_details=shared.PatientDetails(
        dob=dateutil.parser.isoparse('2021-03-31T18:31:24.365Z'),
        email='Sylvan86@yahoo.com',
        first_name='Johnny',
        gender=shared.Gender.FEMALE,
        last_name='Armstrong',
        phone_number='Constantin',
    ),
    physician=shared.PhysicianCreateRequestBase(
        first_name='Dina',
        last_name='Koss',
        licensed_states=[
            'female',
        ],
        npi='Gasoline Developer',
    ),
    sample_id='ruler Cerium',
    user_id='ed536a4e-3800-4791-aee9-d389c73aa02f',
)

res = s.order.register_testkit_v3_order_testkit_register_post(req)

if res.post_order_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.RegisterTestkitRequest](../../models/shared/registertestkitrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.RegisterTestkitV3OrderTestkitRegisterPostResponse](../../models/operations/registertestkitv3ordertestkitregisterpostresponse.md)**


## reschedule_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_reschedule_patch

Reschedule a previously booked at-home phlebotomy appointment.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()

req = operations.ReschedulePhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentReschedulePatchRequest(
    appointment_reschedule_request=shared.AppointmentRescheduleRequest(
        booking_key='Shoes',
    ),
    order_id='372e4ddd-b832-434a-962c-b3ddc204a698',
)

res = s.order.reschedule_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_reschedule_patch(req)

if res.client_facing_appointment is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                                  | [operations.ReschedulePhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentReschedulePatchRequest](../../models/operations/reschedulephlebotomyappointmentv3orderorderidphlebotomyappointmentreschedulepatchrequest.md) | :heavy_check_mark:                                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                                 |


### Response

**[operations.ReschedulePhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentReschedulePatchResponse](../../models/operations/reschedulephlebotomyappointmentv3orderorderidphlebotomyappointmentreschedulepatchresponse.md)**


## sync_testkit_order_status_v3_order_testkit_status_post

This function receives requests from cloud_scheduler
and checks the order status of the order if the order status
in terms of the inbound delivery and outbound delivery status has
changed. If changed then the order status is updated and a webhook
is sent to the respective team.

### Example Usage

```python
import vital


s = vital.Vital()


res = s.order.sync_testkit_order_status_v3_order_testkit_status_post()

if res.response_sync_testkit_order_status_v3_order_testkit_status_post is not None:
    # handle response
```


### Response

**[operations.SyncTestkitOrderStatusV3OrderTestkitStatusPostResponse](../../models/operations/synctestkitorderstatusv3ordertestkitstatuspostresponse.md)**


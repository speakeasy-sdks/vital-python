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


res = s.order.book_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_book_post(appointment_booking_request=shared.AppointmentBookingRequest(
    booking_key='string',
), order_id='ce486d40-b1d8-4151-82e6-c0e7d72ca79b')

if res.client_facing_appointment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `appointment_booking_request`                                                        | [shared.AppointmentBookingRequest](../../models/shared/appointmentbookingrequest.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `order_id`                                                                           | *str*                                                                                | :heavy_check_mark:                                                                   | Your Order ID.                                                                       |


### Response

**[operations.BookPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentBookPostResponse](../../models/operations/bookphlebotomyappointmentv3orderorderidphlebotomyappointmentbookpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## cancel_order_v3_order_order_id_cancel_post

POST cancel order

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.order.cancel_order_v3_order_order_id_cancel_post(order_id='b9d919c2-b9aa-4759-bba5-fb974a744f9a')

if res.post_order_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `order_id`         | *str*              | :heavy_check_mark: | Your Order ID.     |


### Response

**[operations.CancelOrderV3OrderOrderIDCancelPostResponse](../../models/operations/cancelorderv3orderorderidcancelpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## cancel_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_cancel_patch

Cancel a previously booked at-home phlebotomy appointment.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.order.cancel_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_cancel_patch(appointment_cancel_request=shared.AppointmentCancelRequest(
    cancellation_reason_id='string',
), order_id='a0cd9528-ddb0-4d27-a7e9-01ccf3b9448c')

if res.client_facing_appointment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `appointment_cancel_request`                                                       | [shared.AppointmentCancelRequest](../../models/shared/appointmentcancelrequest.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `order_id`                                                                         | *str*                                                                              | :heavy_check_mark:                                                                 | Your Order ID.                                                                     |


### Response

**[operations.CancelPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentCancelPatchResponse](../../models/operations/cancelphlebotomyappointmentv3orderorderidphlebotomyappointmentcancelpatchresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## create

POST create new order

### Example Usage

```python
import dateutil.parser
import vital
from vital.models import shared

s = vital.Vital()

req = shared.CreateOrderRequestCompatible(
    consents=[
        shared.Consent(
            consent_type=shared.ConsentType.MOBILE_TERMS_AND_CONDITIONS,
        ),
    ],
    health_insurance=shared.HealthInsuranceCreateRequest(
        back_image=shared.Jpeg(
        content='0xeC962B1FB8'.encode(),
        content_type=shared.ContentType.IMAGE_JPEG,
    ),
        diagnosis_codes=[
            'string',
        ],
        front_image=shared.Png(
        content='0xD0a361fBCB'.encode(),
        content_type=shared.PngContentType.IMAGE_PNG,
    ),
        patient_signature_image=shared.Png(
        content='0xcCAaFe705D'.encode(),
        content_type=shared.PngContentType.IMAGE_PNG,
    ),
        responsible_details=shared.PersonDetails(
            address=shared.Address(
                city='New Darenberg',
                country='Cote d\'Ivoire',
                first_line='string',
                state='string',
                zip='string',
            ),
            first_name='Micah',
            last_name='Bergnaum',
            phone_number='string',
        ),
    ),
    lab_test_id='d5e26191-5a25-4d0d-9ea1-320e8504aa8c',
    patient_address=shared.PatientAddressCompatible(
        city='Jacksonville',
        country='Kazakhstan',
        state='string',
        street='Kunze Shoals',
        zip='string',
    ),
    patient_details=shared.PatientDetails(
        dob=dateutil.parser.isoparse('2021-10-12T10:48:28.067Z'),
        email='Otho27@yahoo.com',
        first_name='Mazie',
        gender=shared.Gender.UNKNOWN,
        last_name='Waelchi',
        phone_number='string',
    ),
    physician=shared.PhysicianCreateRequest(
        first_name='Myrtice',
        last_name='Sauer',
        licensed_states=[
            'string',
        ],
        npi='string',
        signature_image=shared.Png(
        content='0xA34D9D9Fc5'.encode(),
        content_type=shared.PngContentType.IMAGE_PNG,
    ),
    ),
    user_id='15747251-ef09-4254-8958-35d6b1b39d7e',
)

res = s.order.create(req)

if res.post_order_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.CreateOrderRequestCompatible](../../models/shared/createorderrequestcompatible.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateOrderV3OrderPostResponse](../../models/operations/createorderv3orderpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

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
        first_line='string',
        phone_number='string',
        receiver_name='string',
        state='string',
        zip='string',
    ),
    user_id='6c614a14-431d-4979-8fbf-e68efedf3713',
)

res = s.order.create_testkit(req)

if res.post_order_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [shared.CreateRegistrableTestkitOrderRequest](../../models/shared/createregistrabletestkitorderrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.CreateTestkitOrderV3OrderTestkitPostResponse](../../models/operations/createtestkitorderv3ordertestkitpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## dispatch_status

Dispatch Order Status

### Example Usage

```python
import vital

s = vital.Vital()


res = s.order.dispatch_status()

if res.response_dispatch_order_status_v3_order_dispatch_status_checks_post is not None:
    # handle response
    pass
```


### Response

**[operations.DispatchOrderStatusV3OrderDispatchStatusChecksPostResponse](../../models/operations/dispatchorderstatusv3orderdispatchstatuscheckspostresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get

GET individual order by ID.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.order.get(order_id='b18d8d81-fd7b-4764-a31e-475cb1f36591')

if res.client_facing_order is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `order_id`         | *str*              | :heavy_check_mark: | Your Order ID.     |


### Response

**[operations.GetOrderV3OrderOrderIDGetResponse](../../models/operations/getorderv3orderorderidgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_appointment_availability

Return the available time slots to book an appointment with a phlebotomist
for the given address and order.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.order.get_appointment_availability(order_id='c094c82e-a8e0-42d1-a065-be1f658ff11c', request_body=operations.GetOrderAppointmentAvailabilityV3OrderOrderIDPhlebotomyAppointmentAvailabilityPostUSAddress(
    city='Shanahanboro',
    first_line='string',
    state='string',
    zip_code='56156',
))

if res.appointment_availability_slots is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `order_id`                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                         | Your Order ID.                                                                                                                                                                                                                             |
| `request_body`                                                                                                                                                                                                                             | [Optional[operations.GetOrderAppointmentAvailabilityV3OrderOrderIDPhlebotomyAppointmentAvailabilityPostUSAddress]](../../models/operations/getorderappointmentavailabilityv3orderorderidphlebotomyappointmentavailabilitypostusaddress.md) | :heavy_minus_sign:                                                                                                                                                                                                                         | N/A                                                                                                                                                                                                                                        |


### Response

**[operations.GetOrderAppointmentAvailabilityV3OrderOrderIDPhlebotomyAppointmentAvailabilityPostResponse](../../models/operations/getorderappointmentavailabilityv3orderorderidphlebotomyappointmentavailabilitypostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_area_info

GET information about an area with respect to lab-testing.

Information returned:
* Whether a given zip code is served by our Phlebotomy network.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.order.get_area_info(zip_code='string')

if res.area_info is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `zip_code`                    | *str*                         | :heavy_check_mark:            | Zip code of the area to check |


### Response

**[operations.GetAreaInfoV3OrderAreaInfoGetResponse](../../models/operations/getareainfov3orderareainfogetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_lab_test_result

This endpoint returns the lab results for the order.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.order.get_lab_test_result(order_id='c9229487-8f86-47ef-848e-7eb7243713ad')

if res.response_get_lab_test_result_v3_order_order_id_result_pdf_get is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `order_id`         | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetLabTestResultV3OrderOrderIDResultPdfGetResponse](../../models/operations/getlabtestresultv3orderorderidresultpdfgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_lab_test_result_metadata

Return metadata related to order results, such as lab metadata,
provider and sample dates.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.order.get_lab_test_result_metadata(order_id='daf5fdc5-7c54-4772-826b-69600571af0f')

if res.lab_results_metadata is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `order_id`         | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetLabTestResultMetadataV3OrderOrderIDResultMetadataGetResponse](../../models/operations/getlabtestresultmetadatav3orderorderidresultmetadatagetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_lab_test_result_raw

Return both metadata and raw json test data

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.order.get_lab_test_result_raw(order_id='2cfa7265-4a8d-45d9-b8ea-42e844b02385')

if res.lab_results_raw is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `order_id`         | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetLabTestResultRawV3OrderOrderIDResultGetResponse](../../models/operations/getlabtestresultrawv3orderorderidresultgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_phlebotomy_appointment

Get the appointment associated with an order.

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.order.get_phlebotomy_appointment(order_id='3e95493c-2969-4eab-9aaf-61adbf59533c')

if res.client_facing_appointment is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `order_id`         | *str*              | :heavy_check_mark: | Your Order ID.     |


### Response

**[operations.GetPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentGetResponse](../../models/operations/getphlebotomyappointmentv3orderorderidphlebotomyappointmentgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get_phlebotomy_cancellation_reasons

Get the list of reasons for cancelling an at-home phlebotomy appointment.

### Example Usage

```python
import vital

s = vital.Vital()


res = s.order.get_phlebotomy_cancellation_reasons()

if res.response_get_phlebotomy_appointment_cancellation_reasons_v3_order_phlebotomy_appointment_cancellation_reasons_get is not None:
    # handle response
    pass
```


### Response

**[operations.GetPhlebotomyAppointmentCancellationReasonsV3OrderPhlebotomyAppointmentCancellationReasonsGetResponse](../../models/operations/getphlebotomyappointmentcancellationreasonsv3orderphlebotomyappointmentcancellationreasonsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_requisition_url

GET requisition pdf for an order

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.order.get_requisition_url(order_id='bfbbc5db-bd5f-47b5-9a88-6ef4ccfaf335')

if res.any is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `order_id`         | *str*              | :heavy_check_mark: | Your Order ID.     |


### Response

**[operations.GetOrderRequisitionURLV3OrderOrderIDRequisitionPdfGetResponse](../../models/operations/getorderrequisitionurlv3orderorderidrequisitionpdfgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## order_process_simulate_v3_order_order_id_test_post

Get available test kits.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.order.order_process_simulate_v3_order_order_id_test_post(order_id='03c5e046-8598-4154-ab3e-444d34fe425a', delay=560672, final_status=shared.OrderStatus.COLLECTING_SAMPLE_AT_HOME_PHLEBOTOMY_APPOINTMENT_SCHEDULED)

if res.response_order_process_simulate_v3_order_order_id_test_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `order_id`                                                         | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `delay`                                                            | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `final_status`                                                     | [Optional[shared.OrderStatus]](../../models/shared/orderstatus.md) | :heavy_minus_sign:                                                 | An enumeration.                                                    |


### Response

**[operations.OrderProcessSimulateV3OrderOrderIDTestPostResponse](../../models/operations/orderprocesssimulatev3orderorderidtestpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## process_testkit_order_v3_order_testkit_process_team_id_order_id_post

POST Create shipment for order

### Example Usage

```python
import vital
from vital.models import operations

s = vital.Vital()


res = s.order.process_testkit_order_v3_order_testkit_process_team_id_order_id_post(order_id='21061e75-f548-42fd-90f0-d372d63dff6e', team_id='26a256a9-b0f5-4854-8814-40907e852835')

if res.response_process_testkit_order_v3_order_testkit_process_team_id_order_id_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `order_id`         | *str*              | :heavy_check_mark: | N/A                |
| `team_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ProcessTestkitOrderV3OrderTestkitProcessTeamIDOrderIDPostResponse](../../models/operations/processtestkitorderv3ordertestkitprocessteamidorderidpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## process_testkit_ship_hero_order_shipped_v3_order_testkit_webhook_shiphero_shipment_update_post

Process Testkit Ship Hero Order Shipped

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital()

req = shared.ShipmentWebhookUpdate(
    fulfillment=shared.Fulfillment(
        order_number='string',
        order_uuid='string',
    ),
    webhook_type=shared.WebhookType.SHIPMENT_UPDATE,
)

res = s.order.process_testkit_ship_hero_order_shipped_v3_order_testkit_webhook_shiphero_shipment_update_post(req)

if res.response_process_testkit_ship_hero_order_shipped_v3_order_testkit_webhook_shiphero_shipment_update_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.ShipmentWebhookUpdate](../../models/shared/shipmentwebhookupdate.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ProcessTestkitShipHeroOrderShippedV3OrderTestkitWebhookShipheroShipmentUpdatePostResponse](../../models/operations/processtestkitshipheroordershippedv3ordertestkitwebhookshipheroshipmentupdatepostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## register_testkit_v3_order_testkit_register_post

Register Testkit

### Example Usage

```python
import dateutil.parser
import vital
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
        state='string',
        street='Gloria Stream',
        zip='string',
    ),
    patient_details=shared.PatientDetails(
        dob=dateutil.parser.isoparse('2022-10-13T05:29:20.564Z'),
        email='Keanu_Schoen95@gmail.com',
        first_name='Manley',
        gender=shared.Gender.MALE,
        last_name='Pouros',
        phone_number='string',
    ),
    physician=shared.PhysicianCreateRequestBase(
        first_name='Arne',
        last_name='Keeling',
        licensed_states=[
            'string',
        ],
        npi='string',
    ),
    sample_id='string',
    user_id='e51d8103-2436-4747-b05c-ba39bbafcb7e',
)

res = s.order.register_testkit_v3_order_testkit_register_post(req)

if res.post_order_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.RegisterTestkitRequest](../../models/shared/registertestkitrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.RegisterTestkitV3OrderTestkitRegisterPostResponse](../../models/operations/registertestkitv3ordertestkitregisterpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## reschedule_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_reschedule_patch

Reschedule a previously booked at-home phlebotomy appointment.

### Example Usage

```python
import vital
from vital.models import operations, shared

s = vital.Vital()


res = s.order.reschedule_phlebotomy_appointment_v3_order_order_id_phlebotomy_appointment_reschedule_patch(appointment_reschedule_request=shared.AppointmentRescheduleRequest(
    booking_key='string',
), order_id='337372e4-dddb-4832-b4a5-62cb3ddc204a')

if res.client_facing_appointment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `appointment_reschedule_request`                                                           | [shared.AppointmentRescheduleRequest](../../models/shared/appointmentreschedulerequest.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `order_id`                                                                                 | *str*                                                                                      | :heavy_check_mark:                                                                         | Your Order ID.                                                                             |


### Response

**[operations.ReschedulePhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentReschedulePatchResponse](../../models/operations/reschedulephlebotomyappointmentv3orderorderidphlebotomyappointmentreschedulepatchresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

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
    pass
```


### Response

**[operations.SyncTestkitOrderStatusV3OrderTestkitStatusPostResponse](../../models/operations/synctestkitorderstatusv3ordertestkitstatuspostresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

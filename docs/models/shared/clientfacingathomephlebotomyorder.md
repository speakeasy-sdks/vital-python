# ClientFacingAtHomePhlebotomyOrder

Schema for a at-home-phlebotomy test order in the client facing API.

To be used as part of a ClientFacingOrder.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `appointment_id`                                                     | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_check_mark:                                                   | The Vital at-home phlebotomy Order ID                                |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
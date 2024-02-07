# ClientFacingTestkitOrder

Schema for a testkit order in the client facing API.

To be used as part of a ClientFacingOrder.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The Vital TestKit Order ID                                           |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `shipment`                                                           | [Optional[shared.Shipment]](../../models/shared/shipment.md)         | :heavy_minus_sign:                                                   | Shipment object                                                      |
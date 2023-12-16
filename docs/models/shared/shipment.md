# Shipment

Shipment object


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `id`                                     | *str*                                    | :heavy_check_mark:                       | The Vital Shipment ID                    |
| `inbound_courier`                        | *Optional[str]*                          | :heavy_minus_sign:                       | Courier used for delivery to lab         |
| `inbound_tracking_number`                | *Optional[str]*                          | :heavy_minus_sign:                       | Tracking number for delivery to lab      |
| `inbound_tracking_url`                   | *Optional[str]*                          | :heavy_minus_sign:                       | Tracking url for delivery to lab         |
| `notes`                                  | *Optional[str]*                          | :heavy_minus_sign:                       | Notes associated to the Vital shipment   |
| `outbound_courier`                       | *Optional[str]*                          | :heavy_minus_sign:                       | Courier used for delivery to customer    |
| `outbound_tracking_number`               | *Optional[str]*                          | :heavy_minus_sign:                       | Tracking number for delivery to customer |
| `outbound_tracking_url`                  | *Optional[str]*                          | :heavy_minus_sign:                       | Tracking url for delivery to customer    |
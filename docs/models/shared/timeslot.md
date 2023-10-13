# TimeSlot


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `booking_key`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `end`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Time is in UTC                                                       |
| `expires_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `is_priority`                                                        | *bool*                                                               | :heavy_check_mark:                                                   | N/A                                                                  |
| `num_appointments_available`                                         | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `price`                                                              | *float*                                                              | :heavy_check_mark:                                                   | N/A                                                                  |
| `start`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Time is in UTC                                                       |
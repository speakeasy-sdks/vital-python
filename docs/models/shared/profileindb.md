# ProfileInDb


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `data`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `priority_id`                                                        | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `source`                                                             | [ClientFacingProvider](../../models/shared/clientfacingprovider.md)  | :heavy_check_mark:                                                   | A vendor, a service, or a platform which Vital can connect with.     |
| `source_id`                                                          | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `user_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
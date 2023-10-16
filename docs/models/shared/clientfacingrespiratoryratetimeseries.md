# ClientFacingRespiratoryRateTimeseries


## Fields

| Field                                                                                                                                                                                 | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                  | *Optional[Any]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Deprecated                                                                                                                                                                            |
| `timestamp`                                                                                                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                  | :heavy_check_mark:                                                                                                                                                                    | The timestamp of the measurement.                                                                                                                                                     |
| `timezone_offset`                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Time zone UTC offset in seconds. Positive offset indicates east of UTC; negative offset indicates west of UTC; and null indicates the time zone information is unavailable at source. |
| `type`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | The reading type of the measurement. This is applicable only to Cholesterol, IGG and IGE.                                                                                             |
| `unit`                                                                                                                                                                                | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Measured in bpm.                                                                                                                                                                      |
| `value`                                                                                                                                                                               | *float*                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                    | Average respiratory rate::breaths per minute                                                                                                                                          |
# ClientFacingCaloriesActiveTimeseries


## Fields

| Field                                                                                                                                                                                 | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `end`                                                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                  | :heavy_check_mark:                                                                                                                                                                    | The end time (exclusive) of the interval.                                                                                                                                             |
| `id`                                                                                                                                                                                  | *Optional[Any]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Deprecated                                                                                                                                                                            |
| `start`                                                                                                                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                  | :heavy_check_mark:                                                                                                                                                                    | The start time (inclusive) of the interval.                                                                                                                                           |
| `timestamp`                                                                                                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                  | :heavy_check_mark:                                                                                                                                                                    | Depracated. The start time (inclusive) of the interval.                                                                                                                               |
| `timezone_offset`                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Time zone UTC offset in seconds. Positive offset indicates east of UTC; negative offset indicates west of UTC; and null indicates the time zone information is unavailable at source. |
| `type`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | The reading type of the measurement. This is applicable only to Cholesterol, IGG and IGE.                                                                                             |
| `unit`                                                                                                                                                                                | [ClientFacingCaloriesActiveTimeseriesUnit](../../models/shared/clientfacingcaloriesactivetimeseriesunit.md)                                                                           | :heavy_check_mark:                                                                                                                                                                    | Measured in kilocalories (kcal)                                                                                                                                                       |
| `value`                                                                                                                                                                               | *float*                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                    | Energy consumption caused by the physical activity at the time or interval::kilocalories                                                                                              |
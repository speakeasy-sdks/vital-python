# ClientFacingStream


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `altitude`                                          | list[*float*]                                       | :heavy_minus_sign:                                  | Data points for altitude                            |
| `cadence`                                           | list[*float*]                                       | :heavy_minus_sign:                                  | RPM for cycling, Steps per minute for running       |
| `distance`                                          | list[*float*]                                       | :heavy_minus_sign:                                  | Cumulated distance for exercise                     |
| `heartrate`                                         | list[*int*]                                         | :heavy_minus_sign:                                  | Heart rate in bpm                                   |
| `lat`                                               | list[*float*]                                       | :heavy_minus_sign:                                  | Latitude for data point                             |
| `lng`                                               | list[*float*]                                       | :heavy_minus_sign:                                  | Longitude for data point                            |
| `power`                                             | list[*float*]                                       | :heavy_minus_sign:                                  | Power in watts                                      |
| `resistance`                                        | list[*float*]                                       | :heavy_minus_sign:                                  | Resistance on bike                                  |
| `time`                                              | list[*int*]                                         | :heavy_minus_sign:                                  | Corresponding time stamp in unix time for datapoint |
| `velocity_smooth`                                   | list[*float*]                                       | :heavy_minus_sign:                                  | Velocity in m/s                                     |
# ClientFacingStream


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `altitude`                                          | List[*float*]                                       | :heavy_minus_sign:                                  | Data points for altitude                            |
| `cadence`                                           | List[*float*]                                       | :heavy_minus_sign:                                  | RPM for cycling, Steps per minute for running       |
| `distance`                                          | List[*float*]                                       | :heavy_minus_sign:                                  | Cumulated distance for exercise                     |
| `heartrate`                                         | List[*int*]                                         | :heavy_minus_sign:                                  | Heart rate in bpm                                   |
| `lat`                                               | List[*float*]                                       | :heavy_minus_sign:                                  | Latitude for data point                             |
| `lng`                                               | List[*float*]                                       | :heavy_minus_sign:                                  | Longitude for data point                            |
| `power`                                             | List[*float*]                                       | :heavy_minus_sign:                                  | Power in watts                                      |
| `resistance`                                        | List[*float*]                                       | :heavy_minus_sign:                                  | Resistance on bike                                  |
| `time`                                              | List[*int*]                                         | :heavy_minus_sign:                                  | Corresponding time stamp in unix time for datapoint |
| `velocity_smooth`                                   | List[*float*]                                       | :heavy_minus_sign:                                  | Velocity in m/s                                     |
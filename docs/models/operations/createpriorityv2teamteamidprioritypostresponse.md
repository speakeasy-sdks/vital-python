# CreatePriorityV2TeamTeamIDPriorityPostResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | HTTP response content type for this operation                                         |
| `priority`                                                                            | [Optional[shared.Priority]](../../models/shared/priority.md)                          | :heavy_minus_sign:                                                                    | Successful Response                                                                   |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | HTTP response status code for this operation                                          |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | Raw HTTP response; suitable for custom response parsing                               |
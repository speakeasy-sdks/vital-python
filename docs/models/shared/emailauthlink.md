# EmailAuthLink


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `auth_type`                                              | [shared.AuthType](../../models/shared/authtype.md)       | :heavy_check_mark:                                       | An enumeration.                                          |
| `email`                                                  | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `provider`                                               | [shared.Providers](../../models/shared/providers.md)     | :heavy_check_mark:                                       | An enumeration.                                          |
| `region`                                                 | [Optional[shared.Region]](../../models/shared/region.md) | :heavy_minus_sign:                                       | An enumeration.                                          |
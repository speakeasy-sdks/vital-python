# ClientFacingOrderClientFacingLabTest

The Vital Test associated with the order


## Fields

| Field                                                                                                                  | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `fasting`                                                                                                              | *Optional[bool]*                                                                                                       | :heavy_minus_sign:                                                                                                     | Defines whether a lab test requires fasting. Only available for Labcorp.                                               |
| `id`                                                                                                                   | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | N/A                                                                                                                    |
| `is_active`                                                                                                            | *bool*                                                                                                                 | :heavy_check_mark:                                                                                                     | N/A                                                                                                                    |
| `is_delegated`                                                                                                         | *Optional[bool]*                                                                                                       | :heavy_minus_sign:                                                                                                     | Denotes whether a lab test requires using non-Vital physician networks. If it does then it's delegated - no otherwise. |
| `lab`                                                                                                                  | [Optional[ClientFacingLab]](../../models/shared/clientfacinglab.md)                                                    | :heavy_minus_sign:                                                                                                     | N/A                                                                                                                    |
| `markers`                                                                                                              | list[[ClientFacingMarker](../../models/shared/clientfacingmarker.md)]                                                  | :heavy_minus_sign:                                                                                                     | N/A                                                                                                                    |
| `method`                                                                                                               | [LabTestCollectionMethod](../../models/shared/labtestcollectionmethod.md)                                              | :heavy_check_mark:                                                                                                     | The method used to perform a lab test.                                                                                 |
| `name`                                                                                                                 | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | N/A                                                                                                                    |
| `price`                                                                                                                | *float*                                                                                                                | :heavy_check_mark:                                                                                                     | N/A                                                                                                                    |
| `sample_type`                                                                                                          | [LabTestSampleType](../../models/shared/labtestsampletype.md)                                                          | :heavy_check_mark:                                                                                                     | The type of sample used to perform a lab test.                                                                         |
| `slug`                                                                                                                 | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | N/A                                                                                                                    |
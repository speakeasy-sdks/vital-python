# Orders
(*orders*)

### Available Operations

* [list](#list) - Get Orders

## list

GET many orders with filters.

### Example Usage

```python
import vital
import dateutil.parser
from vital.models import operations

s = vital.Vital()

req = operations.GetOrdersV3OrdersGetRequest(
    order_ids=[
        'c184a429-302e-4aca-80db-f1718b882a50',
    ],
)

res = s.orders.list(req)

if res.get_orders_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetOrdersV3OrdersGetRequest](../../models/operations/getordersv3ordersgetrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetOrdersV3OrdersGetResponse](../../models/operations/getordersv3ordersgetresponse.md)**


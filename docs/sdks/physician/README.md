# Physician
(*physician*)

### Available Operations

* [review_openloop_v2_physician_review_openloop_post](#review_openloop_v2_physician_review_openloop_post) - Review Openloop

## review_openloop_v2_physician_review_openloop_post

Review Openloop

### Example Usage

```python
import vital
from vital.models import shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)

req = shared.OpenLoopEvent(
    event_type=shared.OpenLoopWebhookType.PAYMENT_DELETED,
    resource_id='soak',
    resource_id_type=shared.OpenLoopResourceIDType.NOTE,
)

res = s.physician.review_openloop_v2_physician_review_openloop_post(req)

if res.response_review_openloop_v2_physician_review_openloop_post is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.OpenLoopEvent](../../models/shared/openloopevent.md)        | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.ReviewOpenloopV2PhysicianReviewOpenloopPostResponse](../../models/operations/reviewopenloopv2physicianreviewopenlooppostresponse.md)**


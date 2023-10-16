<!-- Start SDK Example Usage -->


```python
import vital
from vital.models import operations, shared

s = vital.Vital(
    api_key="<YOUR-API-KEY>",
)


res = s.insurance.search_diagnosis(diagnosis_query='JBOD')

if res.client_facing_diagnosis_informations is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->
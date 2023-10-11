<!-- Start SDK Example Usage -->


```python
import vital


s = vital.Vital()


res = s.vital.robots_robots_txt_get()

if res.robots_robots_txt_get_200_text_plain_string is not None:
    # handle response
```
<!-- End SDK Example Usage -->
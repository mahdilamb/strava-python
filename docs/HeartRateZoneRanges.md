# HeartRateZoneRanges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_zones** | **bool** | Whether the athlete has set their own custom heart rate zones | [optional] 
**zones** | [**List[ZoneRange]**](ZoneRange.md) |  | [optional] 

## Example

```python
from strava_python.models.heart_rate_zone_ranges import HeartRateZoneRanges

# TODO update the JSON string below
json = "{}"
# create an instance of HeartRateZoneRanges from a JSON string
heart_rate_zone_ranges_instance = HeartRateZoneRanges.from_json(json)
# print the JSON string representation of the object
print HeartRateZoneRanges.to_json()

# convert the object into a dict
heart_rate_zone_ranges_dict = heart_rate_zone_ranges_instance.to_dict()
# create an instance of HeartRateZoneRanges from a dict
heart_rate_zone_ranges_form_dict = heart_rate_zone_ranges.from_dict(heart_rate_zone_ranges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PowerZoneRanges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zones** | [**List[ZoneRange]**](ZoneRange.md) |  | [optional] 

## Example

```python
from strava_python.models.power_zone_ranges import PowerZoneRanges

# TODO update the JSON string below
json = "{}"
# create an instance of PowerZoneRanges from a JSON string
power_zone_ranges_instance = PowerZoneRanges.from_json(json)
# print the JSON string representation of the object
print PowerZoneRanges.to_json()

# convert the object into a dict
power_zone_ranges_dict = power_zone_ranges_instance.to_dict()
# create an instance of PowerZoneRanges from a dict
power_zone_ranges_form_dict = power_zone_ranges.from_dict(power_zone_ranges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



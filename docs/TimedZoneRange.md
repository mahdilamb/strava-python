# TimedZoneRange

A union type representing the time spent in a given zone.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | The minimum value in the range. | [optional] 
**max** | **int** | The maximum value in the range. | [optional] 
**time** | **int** | The number of seconds spent in this zone | [optional] 

## Example

```python
from strava_python.models.timed_zone_range import TimedZoneRange

# TODO update the JSON string below
json = "{}"
# create an instance of TimedZoneRange from a JSON string
timed_zone_range_instance = TimedZoneRange.from_json(json)
# print the JSON string representation of the object
print TimedZoneRange.to_json()

# convert the object into a dict
timed_zone_range_dict = timed_zone_range_instance.to_dict()
# create an instance of TimedZoneRange from a dict
timed_zone_range_form_dict = timed_zone_range.from_dict(timed_zone_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



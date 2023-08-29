# ZoneRange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | The minimum value in the range. | [optional] 
**max** | **int** | The maximum value in the range. | [optional] 

## Example

```python
from strava_python.models.zone_range import ZoneRange

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneRange from a JSON string
zone_range_instance = ZoneRange.from_json(json)
# print the JSON string representation of the object
print ZoneRange.to_json()

# convert the object into a dict
zone_range_dict = zone_range_instance.to_dict()
# create an instance of ZoneRange from a dict
zone_range_form_dict = zone_range.from_dict(zone_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



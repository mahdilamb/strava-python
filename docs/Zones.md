# Zones


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**heart_rate** | [**HeartRateZoneRanges**](HeartRateZoneRanges.md) |  | [optional] 
**power** | [**PowerZoneRanges**](PowerZoneRanges.md) |  | [optional] 

## Example

```python
from strava_python.models.zones import Zones

# TODO update the JSON string below
json = "{}"
# create an instance of Zones from a JSON string
zones_instance = Zones.from_json(json)
# print the JSON string representation of the object
print Zones.to_json()

# convert the object into a dict
zones_dict = zones_instance.to_dict()
# create an instance of Zones from a dict
zones_form_dict = zones.from_dict(zones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



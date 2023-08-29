# ActivityZone


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** |  | [optional] 
**distribution_buckets** | [**List[TimedZoneRange]**](TimedZoneRange.md) | Stores the exclusive ranges representing zones and the time spent in each. | [optional] 
**type** | **str** |  | [optional] 
**sensor_based** | **bool** |  | [optional] 
**points** | **int** |  | [optional] 
**custom_zones** | **bool** |  | [optional] 
**max** | **int** |  | [optional] 

## Example

```python
from strava_python.models.activity_zone import ActivityZone

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityZone from a JSON string
activity_zone_instance = ActivityZone.from_json(json)
# print the JSON string representation of the object
print ActivityZone.to_json()

# convert the object into a dict
activity_zone_dict = activity_zone_instance.to_dict()
# create an instance of ActivityZone from a dict
activity_zone_form_dict = activity_zone.from_dict(activity_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



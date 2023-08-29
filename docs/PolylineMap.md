# PolylineMap


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the map | [optional] 
**polyline** | **str** | The polyline of the map, only returned on detailed representation of an object | [optional] 
**summary_polyline** | **str** | The summary polyline of the map | [optional] 

## Example

```python
from strava_python.models.polyline_map import PolylineMap

# TODO update the JSON string below
json = "{}"
# create an instance of PolylineMap from a JSON string
polyline_map_instance = PolylineMap.from_json(json)
# print the JSON string representation of the object
print PolylineMap.to_json()

# convert the object into a dict
polyline_map_dict = polyline_map_instance.to_dict()
# create an instance of PolylineMap from a dict
polyline_map_form_dict = polyline_map.from_dict(polyline_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



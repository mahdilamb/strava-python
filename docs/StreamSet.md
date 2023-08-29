# StreamSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**TimeStream**](TimeStream.md) |  | [optional] 
**distance** | [**DistanceStream**](DistanceStream.md) |  | [optional] 
**latlng** | [**LatLngStream**](LatLngStream.md) |  | [optional] 
**altitude** | [**AltitudeStream**](AltitudeStream.md) |  | [optional] 
**velocity_smooth** | [**SmoothVelocityStream**](SmoothVelocityStream.md) |  | [optional] 
**heartrate** | [**HeartrateStream**](HeartrateStream.md) |  | [optional] 
**cadence** | [**CadenceStream**](CadenceStream.md) |  | [optional] 
**watts** | [**PowerStream**](PowerStream.md) |  | [optional] 
**temp** | [**TemperatureStream**](TemperatureStream.md) |  | [optional] 
**moving** | [**MovingStream**](MovingStream.md) |  | [optional] 
**grade_smooth** | [**SmoothGradeStream**](SmoothGradeStream.md) |  | [optional] 

## Example

```python
from strava_python.models.stream_set import StreamSet

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSet from a JSON string
stream_set_instance = StreamSet.from_json(json)
# print the JSON string representation of the object
print StreamSet.to_json()

# convert the object into a dict
stream_set_dict = stream_set_instance.to_dict()
# create an instance of StreamSet from a dict
stream_set_form_dict = stream_set.from_dict(stream_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



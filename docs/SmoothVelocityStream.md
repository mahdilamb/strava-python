# SmoothVelocityStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 
**data** | **List[float]** | The sequence of velocity values for this stream, in meters per second | [optional] 

## Example

```python
from strava_python.models.smooth_velocity_stream import SmoothVelocityStream

# TODO update the JSON string below
json = "{}"
# create an instance of SmoothVelocityStream from a JSON string
smooth_velocity_stream_instance = SmoothVelocityStream.from_json(json)
# print the JSON string representation of the object
print SmoothVelocityStream.to_json()

# convert the object into a dict
smooth_velocity_stream_dict = smooth_velocity_stream_instance.to_dict()
# create an instance of SmoothVelocityStream from a dict
smooth_velocity_stream_form_dict = smooth_velocity_stream.from_dict(smooth_velocity_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



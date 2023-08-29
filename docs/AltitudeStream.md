# AltitudeStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 
**data** | **List[float]** | The sequence of altitude values for this stream, in meters | [optional] 

## Example

```python
from strava_python.models.altitude_stream import AltitudeStream

# TODO update the JSON string below
json = "{}"
# create an instance of AltitudeStream from a JSON string
altitude_stream_instance = AltitudeStream.from_json(json)
# print the JSON string representation of the object
print AltitudeStream.to_json()

# convert the object into a dict
altitude_stream_dict = altitude_stream_instance.to_dict()
# create an instance of AltitudeStream from a dict
altitude_stream_form_dict = altitude_stream.from_dict(altitude_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TimeStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 
**data** | **List[int]** | The sequence of time values for this stream, in seconds | [optional] 

## Example

```python
from strava_python.models.time_stream import TimeStream

# TODO update the JSON string below
json = "{}"
# create an instance of TimeStream from a JSON string
time_stream_instance = TimeStream.from_json(json)
# print the JSON string representation of the object
print TimeStream.to_json()

# convert the object into a dict
time_stream_dict = time_stream_instance.to_dict()
# create an instance of TimeStream from a dict
time_stream_form_dict = time_stream.from_dict(time_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



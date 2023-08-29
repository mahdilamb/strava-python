# MovingStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 
**data** | **List[bool]** | The sequence of moving values for this stream, as boolean values | [optional] 

## Example

```python
from strava_python.models.moving_stream import MovingStream

# TODO update the JSON string below
json = "{}"
# create an instance of MovingStream from a JSON string
moving_stream_instance = MovingStream.from_json(json)
# print the JSON string representation of the object
print MovingStream.to_json()

# convert the object into a dict
moving_stream_dict = moving_stream_instance.to_dict()
# create an instance of MovingStream from a dict
moving_stream_form_dict = moving_stream.from_dict(moving_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



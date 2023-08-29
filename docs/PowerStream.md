# PowerStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 
**data** | **List[int]** | The sequence of power values for this stream, in watts | [optional] 

## Example

```python
from strava_python.models.power_stream import PowerStream

# TODO update the JSON string below
json = "{}"
# create an instance of PowerStream from a JSON string
power_stream_instance = PowerStream.from_json(json)
# print the JSON string representation of the object
print PowerStream.to_json()

# convert the object into a dict
power_stream_dict = power_stream_instance.to_dict()
# create an instance of PowerStream from a dict
power_stream_form_dict = power_stream.from_dict(power_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



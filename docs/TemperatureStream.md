# TemperatureStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 
**data** | **List[int]** | The sequence of temperature values for this stream, in celsius degrees | [optional] 

## Example

```python
from strava_python.models.temperature_stream import TemperatureStream

# TODO update the JSON string below
json = "{}"
# create an instance of TemperatureStream from a JSON string
temperature_stream_instance = TemperatureStream.from_json(json)
# print the JSON string representation of the object
print TemperatureStream.to_json()

# convert the object into a dict
temperature_stream_dict = temperature_stream_instance.to_dict()
# create an instance of TemperatureStream from a dict
temperature_stream_form_dict = temperature_stream.from_dict(temperature_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



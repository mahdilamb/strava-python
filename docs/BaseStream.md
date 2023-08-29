# BaseStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 

## Example

```python
from strava_python.models.base_stream import BaseStream

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStream from a JSON string
base_stream_instance = BaseStream.from_json(json)
# print the JSON string representation of the object
print BaseStream.to_json()

# convert the object into a dict
base_stream_dict = base_stream_instance.to_dict()
# create an instance of BaseStream from a dict
base_stream_form_dict = base_stream.from_dict(base_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



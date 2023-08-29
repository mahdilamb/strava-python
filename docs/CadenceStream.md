# CadenceStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 
**data** | **List[int]** | The sequence of cadence values for this stream, in rotations per minute | [optional] 

## Example

```python
from strava_python.models.cadence_stream import CadenceStream

# TODO update the JSON string below
json = "{}"
# create an instance of CadenceStream from a JSON string
cadence_stream_instance = CadenceStream.from_json(json)
# print the JSON string representation of the object
print CadenceStream.to_json()

# convert the object into a dict
cadence_stream_dict = cadence_stream_instance.to_dict()
# create an instance of CadenceStream from a dict
cadence_stream_form_dict = cadence_stream.from_dict(cadence_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



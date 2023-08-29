# DistanceStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 
**data** | **List[float]** | The sequence of distance values for this stream, in meters | [optional] 

## Example

```python
from strava_python.models.distance_stream import DistanceStream

# TODO update the JSON string below
json = "{}"
# create an instance of DistanceStream from a JSON string
distance_stream_instance = DistanceStream.from_json(json)
# print the JSON string representation of the object
print DistanceStream.to_json()

# convert the object into a dict
distance_stream_dict = distance_stream_instance.to_dict()
# create an instance of DistanceStream from a dict
distance_stream_form_dict = distance_stream.from_dict(distance_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



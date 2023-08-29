# LatLngStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 
**data** | **List[List[float]]** | The sequence of lat/long values for this stream | [optional] 

## Example

```python
from strava_python.models.lat_lng_stream import LatLngStream

# TODO update the JSON string below
json = "{}"
# create an instance of LatLngStream from a JSON string
lat_lng_stream_instance = LatLngStream.from_json(json)
# print the JSON string representation of the object
print LatLngStream.to_json()

# convert the object into a dict
lat_lng_stream_dict = lat_lng_stream_instance.to_dict()
# create an instance of LatLngStream from a dict
lat_lng_stream_form_dict = lat_lng_stream.from_dict(lat_lng_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# HeartrateStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 
**data** | **List[int]** | The sequence of heart rate values for this stream, in beats per minute | [optional] 

## Example

```python
from strava_python.models.heartrate_stream import HeartrateStream

# TODO update the JSON string below
json = "{}"
# create an instance of HeartrateStream from a JSON string
heartrate_stream_instance = HeartrateStream.from_json(json)
# print the JSON string representation of the object
print HeartrateStream.to_json()

# convert the object into a dict
heartrate_stream_dict = heartrate_stream_instance.to_dict()
# create an instance of HeartrateStream from a dict
heartrate_stream_form_dict = heartrate_stream.from_dict(heartrate_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SmoothGradeStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **int** | The number of data points in this stream | [optional] 
**resolution** | **str** | The level of detail (sampling) in which this stream was returned | [optional] 
**series_type** | **str** | The base series used in the case the stream was downsampled | [optional] 
**data** | **List[float]** | The sequence of grade values for this stream, as percents of a grade | [optional] 

## Example

```python
from strava_python.models.smooth_grade_stream import SmoothGradeStream

# TODO update the JSON string below
json = "{}"
# create an instance of SmoothGradeStream from a JSON string
smooth_grade_stream_instance = SmoothGradeStream.from_json(json)
# print the JSON string representation of the object
print SmoothGradeStream.to_json()

# convert the object into a dict
smooth_grade_stream_dict = smooth_grade_stream_instance.to_dict()
# create an instance of SmoothGradeStream from a dict
smooth_grade_stream_form_dict = smooth_grade_stream.from_dict(smooth_grade_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



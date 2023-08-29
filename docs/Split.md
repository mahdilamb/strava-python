# Split


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_speed** | **float** | The average speed of this split, in meters per second | [optional] 
**distance** | **float** | The distance of this split, in meters | [optional] 
**elapsed_time** | **int** | The elapsed time of this split, in seconds | [optional] 
**elevation_difference** | **float** | The elevation difference of this split, in meters | [optional] 
**pace_zone** | **int** | The pacing zone of this split | [optional] 
**moving_time** | **int** | The moving time of this split, in seconds | [optional] 
**split** | **int** | N/A | [optional] 

## Example

```python
from strava_python.models.split import Split

# TODO update the JSON string below
json = "{}"
# create an instance of Split from a JSON string
split_instance = Split.from_json(json)
# print the JSON string representation of the object
print Split.to_json()

# convert the object into a dict
split_dict = split_instance.to_dict()
# create an instance of Split from a dict
split_form_dict = split.from_dict(split_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



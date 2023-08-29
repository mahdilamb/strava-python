# ActivityTotal

A roll-up of metrics pertaining to a set of activities. Values are in seconds and meters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of activities considered in this total. | [optional] 
**distance** | **float** | The total distance covered by the considered activities. | [optional] 
**moving_time** | **int** | The total moving time of the considered activities. | [optional] 
**elapsed_time** | **int** | The total elapsed time of the considered activities. | [optional] 
**elevation_gain** | **float** | The total elevation gain of the considered activities. | [optional] 
**achievement_count** | **int** | The total number of achievements of the considered activities. | [optional] 

## Example

```python
from strava_python.models.activity_total import ActivityTotal

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityTotal from a JSON string
activity_total_instance = ActivityTotal.from_json(json)
# print the JSON string representation of the object
print ActivityTotal.to_json()

# convert the object into a dict
activity_total_dict = activity_total_instance.to_dict()
# create an instance of ActivityTotal from a dict
activity_total_form_dict = activity_total.from_dict(activity_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



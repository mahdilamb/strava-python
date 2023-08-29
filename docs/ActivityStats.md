# ActivityStats

A set of rolled-up statistics and totals for an athlete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biggest_ride_distance** | **float** | The longest distance ridden by the athlete. | [optional] 
**biggest_climb_elevation_gain** | **float** | The highest climb ridden by the athlete. | [optional] 
**recent_ride_totals** | [**ActivityTotal**](ActivityTotal.md) |  | [optional] 
**recent_run_totals** | [**ActivityTotal**](ActivityTotal.md) |  | [optional] 
**recent_swim_totals** | [**ActivityTotal**](ActivityTotal.md) |  | [optional] 
**ytd_ride_totals** | [**ActivityTotal**](ActivityTotal.md) |  | [optional] 
**ytd_run_totals** | [**ActivityTotal**](ActivityTotal.md) |  | [optional] 
**ytd_swim_totals** | [**ActivityTotal**](ActivityTotal.md) |  | [optional] 
**all_ride_totals** | [**ActivityTotal**](ActivityTotal.md) |  | [optional] 
**all_run_totals** | [**ActivityTotal**](ActivityTotal.md) |  | [optional] 
**all_swim_totals** | [**ActivityTotal**](ActivityTotal.md) |  | [optional] 

## Example

```python
from strava_python.models.activity_stats import ActivityStats

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityStats from a JSON string
activity_stats_instance = ActivityStats.from_json(json)
# print the JSON string representation of the object
print ActivityStats.to_json()

# convert the object into a dict
activity_stats_dict = activity_stats_instance.to_dict()
# create an instance of ActivityStats from a dict
activity_stats_form_dict = activity_stats.from_dict(activity_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



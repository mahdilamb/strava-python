# ClubActivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete** | [**MetaAthlete**](MetaAthlete.md) |  | [optional] 
**name** | **str** | The name of the activity | [optional] 
**distance** | **float** | The activity&#39;s distance, in meters | [optional] 
**moving_time** | **int** | The activity&#39;s moving time, in seconds | [optional] 
**elapsed_time** | **int** | The activity&#39;s elapsed time, in seconds | [optional] 
**total_elevation_gain** | **float** | The activity&#39;s total elevation gain. | [optional] 
**type** | [**ActivityType**](ActivityType.md) |  | [optional] 
**sport_type** | [**SportType**](SportType.md) |  | [optional] 
**workout_type** | **int** | The activity&#39;s workout type | [optional] 

## Example

```python
from strava_python.models.club_activity import ClubActivity

# TODO update the JSON string below
json = "{}"
# create an instance of ClubActivity from a JSON string
club_activity_instance = ClubActivity.from_json(json)
# print the JSON string representation of the object
print ClubActivity.to_json()

# convert the object into a dict
club_activity_dict = club_activity_instance.to_dict()
# create an instance of ClubActivity from a dict
club_activity_form_dict = club_activity.from_dict(club_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



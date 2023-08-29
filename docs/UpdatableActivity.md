# UpdatableActivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commute** | **bool** | Whether this activity is a commute | [optional] 
**trainer** | **bool** | Whether this activity was recorded on a training machine | [optional] 
**hide_from_home** | **bool** | Whether this activity is muted | [optional] 
**description** | **str** | The description of the activity | [optional] 
**name** | **str** | The name of the activity | [optional] 
**type** | [**ActivityType**](ActivityType.md) |  | [optional] 
**sport_type** | [**SportType**](SportType.md) |  | [optional] 
**gear_id** | **str** | Identifier for the gear associated with the activity. ‘none’ clears gear from activity | [optional] 

## Example

```python
from strava_python.models.updatable_activity import UpdatableActivity

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatableActivity from a JSON string
updatable_activity_instance = UpdatableActivity.from_json(json)
# print the JSON string representation of the object
print UpdatableActivity.to_json()

# convert the object into a dict
updatable_activity_dict = updatable_activity_instance.to_dict()
# create an instance of UpdatableActivity from a dict
updatable_activity_form_dict = updatable_activity.from_dict(updatable_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MetaActivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the activity | [optional] 

## Example

```python
from strava_python.models.meta_activity import MetaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of MetaActivity from a JSON string
meta_activity_instance = MetaActivity.from_json(json)
# print the JSON string representation of the object
print MetaActivity.to_json()

# convert the object into a dict
meta_activity_dict = meta_activity_instance.to_dict()
# create an instance of MetaActivity from a dict
meta_activity_form_dict = meta_activity.from_dict(meta_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



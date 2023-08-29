# MetaClub


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The club&#39;s unique identifier. | [optional] 
**resource_state** | **int** | Resource state, indicates level of detail. Possible values: 1 -&gt; \&quot;meta\&quot;, 2 -&gt; \&quot;summary\&quot;, 3 -&gt; \&quot;detail\&quot; | [optional] 
**name** | **str** | The club&#39;s name. | [optional] 

## Example

```python
from strava_python.models.meta_club import MetaClub

# TODO update the JSON string below
json = "{}"
# create an instance of MetaClub from a JSON string
meta_club_instance = MetaClub.from_json(json)
# print the JSON string representation of the object
print MetaClub.to_json()

# convert the object into a dict
meta_club_dict = meta_club_instance.to_dict()
# create an instance of MetaClub from a dict
meta_club_form_dict = meta_club.from_dict(meta_club_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



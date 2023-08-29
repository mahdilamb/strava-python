# SummaryAthlete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the athlete | [optional] 
**resource_state** | **int** | Resource state, indicates level of detail. Possible values: 1 -&gt; \&quot;meta\&quot;, 2 -&gt; \&quot;summary\&quot;, 3 -&gt; \&quot;detail\&quot; | [optional] 
**firstname** | **str** | The athlete&#39;s first name. | [optional] 
**lastname** | **str** | The athlete&#39;s last name. | [optional] 
**profile_medium** | **str** | URL to a 62x62 pixel profile picture. | [optional] 
**profile** | **str** | URL to a 124x124 pixel profile picture. | [optional] 
**city** | **str** | The athlete&#39;s city. | [optional] 
**state** | **str** | The athlete&#39;s state or geographical region. | [optional] 
**country** | **str** | The athlete&#39;s country. | [optional] 
**sex** | **str** | The athlete&#39;s sex. | [optional] 
**premium** | **bool** | Deprecated.  Use summit field instead. Whether the athlete has any Summit subscription. | [optional] 
**summit** | **bool** | Whether the athlete has any Summit subscription. | [optional] 
**created_at** | **datetime** | The time at which the athlete was created. | [optional] 
**updated_at** | **datetime** | The time at which the athlete was last updated. | [optional] 

## Example

```python
from strava_python.models.summary_athlete import SummaryAthlete

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryAthlete from a JSON string
summary_athlete_instance = SummaryAthlete.from_json(json)
# print the JSON string representation of the object
print SummaryAthlete.to_json()

# convert the object into a dict
summary_athlete_dict = summary_athlete_instance.to_dict()
# create an instance of SummaryAthlete from a dict
summary_athlete_form_dict = summary_athlete.from_dict(summary_athlete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



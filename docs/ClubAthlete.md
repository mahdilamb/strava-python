# ClubAthlete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_state** | **int** | Resource state, indicates level of detail. Possible values: 1 -&gt; \&quot;meta\&quot;, 2 -&gt; \&quot;summary\&quot;, 3 -&gt; \&quot;detail\&quot; | [optional] 
**firstname** | **str** | The athlete&#39;s first name. | [optional] 
**lastname** | **str** | The athlete&#39;s last initial. | [optional] 
**member** | **str** | The athlete&#39;s member status. | [optional] 
**admin** | **bool** | Whether the athlete is a club admin. | [optional] 
**owner** | **bool** | Whether the athlete is club owner. | [optional] 

## Example

```python
from strava_python.models.club_athlete import ClubAthlete

# TODO update the JSON string below
json = "{}"
# create an instance of ClubAthlete from a JSON string
club_athlete_instance = ClubAthlete.from_json(json)
# print the JSON string representation of the object
print ClubAthlete.to_json()

# convert the object into a dict
club_athlete_dict = club_athlete_instance.to_dict()
# create an instance of ClubAthlete from a dict
club_athlete_form_dict = club_athlete.from_dict(club_athlete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



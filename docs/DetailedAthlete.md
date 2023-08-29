# DetailedAthlete


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
**follower_count** | **int** | The athlete&#39;s follower count. | [optional] 
**friend_count** | **int** | The athlete&#39;s friend count. | [optional] 
**measurement_preference** | **str** | The athlete&#39;s preferred unit system. | [optional] 
**ftp** | **int** | The athlete&#39;s FTP (Functional Threshold Power). | [optional] 
**weight** | **float** | The athlete&#39;s weight. | [optional] 
**clubs** | [**List[SummaryClub]**](SummaryClub.md) | The athlete&#39;s clubs. | [optional] 
**bikes** | [**List[SummaryGear]**](SummaryGear.md) | The athlete&#39;s bikes. | [optional] 
**shoes** | [**List[SummaryGear]**](SummaryGear.md) | The athlete&#39;s shoes. | [optional] 

## Example

```python
from strava_python.models.detailed_athlete import DetailedAthlete

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedAthlete from a JSON string
detailed_athlete_instance = DetailedAthlete.from_json(json)
# print the JSON string representation of the object
print DetailedAthlete.to_json()

# convert the object into a dict
detailed_athlete_dict = detailed_athlete_instance.to_dict()
# create an instance of DetailedAthlete from a dict
detailed_athlete_form_dict = detailed_athlete.from_dict(detailed_athlete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



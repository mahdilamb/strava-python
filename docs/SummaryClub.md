# SummaryClub


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The club&#39;s unique identifier. | [optional] 
**resource_state** | **int** | Resource state, indicates level of detail. Possible values: 1 -&gt; \&quot;meta\&quot;, 2 -&gt; \&quot;summary\&quot;, 3 -&gt; \&quot;detail\&quot; | [optional] 
**name** | **str** | The club&#39;s name. | [optional] 
**profile_medium** | **str** | URL to a 60x60 pixel profile picture. | [optional] 
**cover_photo** | **str** | URL to a ~1185x580 pixel cover photo. | [optional] 
**cover_photo_small** | **str** | URL to a ~360x176  pixel cover photo. | [optional] 
**sport_type** | **str** | Deprecated. Prefer to use activity_types. | [optional] 
**activity_types** | [**List[ActivityType]**](ActivityType.md) | The activity types that count for a club. This takes precedence over sport_type. | [optional] 
**city** | **str** | The club&#39;s city. | [optional] 
**state** | **str** | The club&#39;s state or geographical region. | [optional] 
**country** | **str** | The club&#39;s country. | [optional] 
**private** | **bool** | Whether the club is private. | [optional] 
**member_count** | **int** | The club&#39;s member count. | [optional] 
**featured** | **bool** | Whether the club is featured or not. | [optional] 
**verified** | **bool** | Whether the club is verified or not. | [optional] 
**url** | **str** | The club&#39;s vanity URL. | [optional] 

## Example

```python
from strava_python.models.summary_club import SummaryClub

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryClub from a JSON string
summary_club_instance = SummaryClub.from_json(json)
# print the JSON string representation of the object
print SummaryClub.to_json()

# convert the object into a dict
summary_club_dict = summary_club_instance.to_dict()
# create an instance of SummaryClub from a dict
summary_club_form_dict = summary_club.from_dict(summary_club_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



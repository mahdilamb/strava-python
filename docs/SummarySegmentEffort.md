# SummarySegmentEffort


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of this effort | [optional] 
**activity_id** | **int** | The unique identifier of the activity related to this effort | [optional] 
**elapsed_time** | **int** | The effort&#39;s elapsed time | [optional] 
**start_date** | **datetime** | The time at which the effort was started. | [optional] 
**start_date_local** | **datetime** | The time at which the effort was started in the local timezone. | [optional] 
**distance** | **float** | The effort&#39;s distance in meters | [optional] 
**is_kom** | **bool** | Whether this effort is the current best on the leaderboard | [optional] 

## Example

```python
from strava_python.models.summary_segment_effort import SummarySegmentEffort

# TODO update the JSON string below
json = "{}"
# create an instance of SummarySegmentEffort from a JSON string
summary_segment_effort_instance = SummarySegmentEffort.from_json(json)
# print the JSON string representation of the object
print SummarySegmentEffort.to_json()

# convert the object into a dict
summary_segment_effort_dict = summary_segment_effort_instance.to_dict()
# create an instance of SummarySegmentEffort from a dict
summary_segment_effort_form_dict = summary_segment_effort.from_dict(summary_segment_effort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



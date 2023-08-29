# SummaryPRSegmentEffort


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pr_activity_id** | **int** | The unique identifier of the activity related to the PR effort. | [optional] 
**pr_elapsed_time** | **int** | The elapsed time ot the PR effort. | [optional] 
**pr_date** | **datetime** | The time at which the PR effort was started. | [optional] 
**effort_count** | **int** | Number of efforts by the authenticated athlete on this segment. | [optional] 

## Example

```python
from strava_python.models.summary_pr_segment_effort import SummaryPRSegmentEffort

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryPRSegmentEffort from a JSON string
summary_pr_segment_effort_instance = SummaryPRSegmentEffort.from_json(json)
# print the JSON string representation of the object
print SummaryPRSegmentEffort.to_json()

# convert the object into a dict
summary_pr_segment_effort_dict = summary_pr_segment_effort_instance.to_dict()
# create an instance of SummaryPRSegmentEffort from a dict
summary_pr_segment_effort_form_dict = summary_pr_segment_effort.from_dict(summary_pr_segment_effort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



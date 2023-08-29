# SummarySegment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of this segment | [optional] 
**name** | **str** | The name of this segment | [optional] 
**activity_type** | **str** |  | [optional] 
**distance** | **float** | The segment&#39;s distance, in meters | [optional] 
**average_grade** | **float** | The segment&#39;s average grade, in percents | [optional] 
**maximum_grade** | **float** | The segments&#39;s maximum grade, in percents | [optional] 
**elevation_high** | **float** | The segments&#39;s highest elevation, in meters | [optional] 
**elevation_low** | **float** | The segments&#39;s lowest elevation, in meters | [optional] 
**start_latlng** | **List[float]** | A pair of latitude/longitude coordinates, represented as an array of 2 floating point numbers. | [optional] 
**end_latlng** | **List[float]** | A pair of latitude/longitude coordinates, represented as an array of 2 floating point numbers. | [optional] 
**climb_category** | **int** | The category of the climb [0, 5]. Higher is harder ie. 5 is Hors catégorie, 0 is uncategorized in climb_category. | [optional] 
**city** | **str** | The segments&#39;s city. | [optional] 
**state** | **str** | The segments&#39;s state or geographical region. | [optional] 
**country** | **str** | The segment&#39;s country. | [optional] 
**private** | **bool** | Whether this segment is private. | [optional] 
**athlete_pr_effort** | [**SummaryPRSegmentEffort**](SummaryPRSegmentEffort.md) |  | [optional] 
**athlete_segment_stats** | [**SummarySegmentEffort**](SummarySegmentEffort.md) |  | [optional] 

## Example

```python
from strava_python.models.summary_segment import SummarySegment

# TODO update the JSON string below
json = "{}"
# create an instance of SummarySegment from a JSON string
summary_segment_instance = SummarySegment.from_json(json)
# print the JSON string representation of the object
print SummarySegment.to_json()

# convert the object into a dict
summary_segment_dict = summary_segment_instance.to_dict()
# create an instance of SummarySegment from a dict
summary_segment_form_dict = summary_segment.from_dict(summary_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



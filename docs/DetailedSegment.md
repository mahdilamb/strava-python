# DetailedSegment


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
**created_at** | **datetime** | The time at which the segment was created. | [optional] 
**updated_at** | **datetime** | The time at which the segment was last updated. | [optional] 
**total_elevation_gain** | **float** | The segment&#39;s total elevation gain. | [optional] 
**map** | [**PolylineMap**](PolylineMap.md) |  | [optional] 
**effort_count** | **int** | The total number of efforts for this segment | [optional] 
**athlete_count** | **int** | The number of unique athletes who have an effort for this segment | [optional] 
**hazardous** | **bool** | Whether this segment is considered hazardous | [optional] 
**star_count** | **int** | The number of stars for this segment | [optional] 

## Example

```python
from strava_python.models.detailed_segment import DetailedSegment

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedSegment from a JSON string
detailed_segment_instance = DetailedSegment.from_json(json)
# print the JSON string representation of the object
print DetailedSegment.to_json()

# convert the object into a dict
detailed_segment_dict = detailed_segment_instance.to_dict()
# create an instance of DetailedSegment from a dict
detailed_segment_form_dict = detailed_segment.from_dict(detailed_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



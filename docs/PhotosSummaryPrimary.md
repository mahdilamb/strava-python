# PhotosSummaryPrimary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**source** | **int** |  | [optional] 
**unique_id** | **str** |  | [optional] 
**urls** | **Dict[str, str]** |  | [optional] 

## Example

```python
from strava_python.models.photos_summary_primary import PhotosSummaryPrimary

# TODO update the JSON string below
json = "{}"
# create an instance of PhotosSummaryPrimary from a JSON string
photos_summary_primary_instance = PhotosSummaryPrimary.from_json(json)
# print the JSON string representation of the object
print PhotosSummaryPrimary.to_json()

# convert the object into a dict
photos_summary_primary_dict = photos_summary_primary_instance.to_dict()
# create an instance of PhotosSummaryPrimary from a dict
photos_summary_primary_form_dict = photos_summary_primary.from_dict(photos_summary_primary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



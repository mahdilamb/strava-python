# PhotosSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of photos | [optional] 
**primary** | [**PhotosSummaryPrimary**](PhotosSummaryPrimary.md) |  | [optional] 

## Example

```python
from strava_python.models.photos_summary import PhotosSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PhotosSummary from a JSON string
photos_summary_instance = PhotosSummary.from_json(json)
# print the JSON string representation of the object
print PhotosSummary.to_json()

# convert the object into a dict
photos_summary_dict = photos_summary_instance.to_dict()
# create an instance of PhotosSummary from a dict
photos_summary_form_dict = photos_summary.from_dict(photos_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



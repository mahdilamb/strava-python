# ExplorerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segments** | [**List[ExplorerSegment]**](ExplorerSegment.md) | The set of segments matching an explorer request | [optional] 

## Example

```python
from strava_python.models.explorer_response import ExplorerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerResponse from a JSON string
explorer_response_instance = ExplorerResponse.from_json(json)
# print the JSON string representation of the object
print ExplorerResponse.to_json()

# convert the object into a dict
explorer_response_dict = explorer_response_instance.to_dict()
# create an instance of ExplorerResponse from a dict
explorer_response_form_dict = explorer_response.from_dict(explorer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



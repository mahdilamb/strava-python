# Fault

Encapsulates the errors that may be returned from the API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) | The set of specific errors associated with this fault, if any. | [optional] 
**message** | **str** | The message of the fault. | [optional] 

## Example

```python
from strava_python.models.fault import Fault

# TODO update the JSON string below
json = "{}"
# create an instance of Fault from a JSON string
fault_instance = Fault.from_json(json)
# print the JSON string representation of the object
print Fault.to_json()

# convert the object into a dict
fault_dict = fault_instance.to_dict()
# create an instance of Fault from a dict
fault_form_dict = fault.from_dict(fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



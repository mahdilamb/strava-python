# SummaryGear


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The gear&#39;s unique identifier. | [optional] 
**resource_state** | **int** | Resource state, indicates level of detail. Possible values: 2 -&gt; \&quot;summary\&quot;, 3 -&gt; \&quot;detail\&quot; | [optional] 
**primary** | **bool** | Whether this gear&#39;s is the owner&#39;s default one. | [optional] 
**name** | **str** | The gear&#39;s name. | [optional] 
**distance** | **float** | The distance logged with this gear. | [optional] 

## Example

```python
from strava_python.models.summary_gear import SummaryGear

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryGear from a JSON string
summary_gear_instance = SummaryGear.from_json(json)
# print the JSON string representation of the object
print SummaryGear.to_json()

# convert the object into a dict
summary_gear_dict = summary_gear_instance.to_dict()
# create an instance of SummaryGear from a dict
summary_gear_form_dict = summary_gear.from_dict(summary_gear_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



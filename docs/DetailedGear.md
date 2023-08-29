# DetailedGear


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The gear&#39;s unique identifier. | [optional] 
**resource_state** | **int** | Resource state, indicates level of detail. Possible values: 2 -&gt; \&quot;summary\&quot;, 3 -&gt; \&quot;detail\&quot; | [optional] 
**primary** | **bool** | Whether this gear&#39;s is the owner&#39;s default one. | [optional] 
**name** | **str** | The gear&#39;s name. | [optional] 
**distance** | **float** | The distance logged with this gear. | [optional] 
**brand_name** | **str** | The gear&#39;s brand name. | [optional] 
**model_name** | **str** | The gear&#39;s model name. | [optional] 
**frame_type** | **int** | The gear&#39;s frame type (bike only). | [optional] 
**description** | **str** | The gear&#39;s description. | [optional] 

## Example

```python
from strava_python.models.detailed_gear import DetailedGear

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedGear from a JSON string
detailed_gear_instance = DetailedGear.from_json(json)
# print the JSON string representation of the object
print DetailedGear.to_json()

# convert the object into a dict
detailed_gear_dict = detailed_gear_instance.to_dict()
# create an instance of DetailedGear from a dict
detailed_gear_form_dict = detailed_gear.from_dict(detailed_gear_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



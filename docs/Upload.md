# Upload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the upload | [optional] 
**id_str** | **str** | The unique identifier of the upload in string format | [optional] 
**external_id** | **str** | The external identifier of the upload | [optional] 
**error** | **str** | The error associated with this upload | [optional] 
**status** | **str** | The status of this upload | [optional] 
**activity_id** | **int** | The identifier of the activity this upload resulted into | [optional] 

## Example

```python
from strava_python.models.upload import Upload

# TODO update the JSON string below
json = "{}"
# create an instance of Upload from a JSON string
upload_instance = Upload.from_json(json)
# print the JSON string representation of the object
print Upload.to_json()

# convert the object into a dict
upload_dict = upload_instance.to_dict()
# create an instance of Upload from a dict
upload_form_dict = upload.from_dict(upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Comment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of this comment | [optional] 
**activity_id** | **int** | The identifier of the activity this comment is related to | [optional] 
**text** | **str** | The content of the comment | [optional] 
**athlete** | [**SummaryAthlete**](SummaryAthlete.md) |  | [optional] 
**created_at** | **datetime** | The time at which this comment was created. | [optional] 

## Example

```python
from strava_python.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print Comment.to_json()

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_form_dict = comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



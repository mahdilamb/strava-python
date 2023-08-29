# MetaAthlete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the athlete | [optional] 

## Example

```python
from strava_python.models.meta_athlete import MetaAthlete

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAthlete from a JSON string
meta_athlete_instance = MetaAthlete.from_json(json)
# print the JSON string representation of the object
print MetaAthlete.to_json()

# convert the object into a dict
meta_athlete_dict = meta_athlete_instance.to_dict()
# create an instance of MetaAthlete from a dict
meta_athlete_form_dict = meta_athlete.from_dict(meta_athlete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



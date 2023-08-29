# strava_python.ActivitiesApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity**](ActivitiesApi.md#create_activity) | **POST** /activities | Create an Activity
[**get_activity_by_id**](ActivitiesApi.md#get_activity_by_id) | **GET** /activities/{id} | Get Activity
[**get_comments_by_activity_id**](ActivitiesApi.md#get_comments_by_activity_id) | **GET** /activities/{id}/comments | List Activity Comments
[**get_kudoers_by_activity_id**](ActivitiesApi.md#get_kudoers_by_activity_id) | **GET** /activities/{id}/kudos | List Activity Kudoers
[**get_laps_by_activity_id**](ActivitiesApi.md#get_laps_by_activity_id) | **GET** /activities/{id}/laps | List Activity Laps
[**get_logged_in_athlete_activities**](ActivitiesApi.md#get_logged_in_athlete_activities) | **GET** /athlete/activities | List Athlete Activities
[**get_zones_by_activity_id**](ActivitiesApi.md#get_zones_by_activity_id) | **GET** /activities/{id}/zones | Get Activity Zones
[**update_activity_by_id**](ActivitiesApi.md#update_activity_by_id) | **PUT** /activities/{id} | Update Activity


# **create_activity**
> DetailedActivity create_activity(name, sport_type, start_date_local, elapsed_time, type=type, description=description, distance=distance, trainer=trainer, commute=commute)

Create an Activity

Creates a manual activity for an athlete, requires activity:write scope.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.detailed_activity import DetailedActivity
from strava_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.strava.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = strava_python.Configuration(
    host = "https://www.strava.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with strava_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = strava_python.ActivitiesApi(api_client)
    name = 'name_example' # str | The name of the activity.
    sport_type = 'sport_type_example' # str | Sport type of activity. For example - Run, MountainBikeRide, Ride, etc.
    start_date_local = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 formatted date time.
    elapsed_time = 56 # int | In seconds.
    type = 'type_example' # str | Type of activity. For example - Run, Ride etc. (optional)
    description = 'description_example' # str | Description of the activity. (optional)
    distance = 3.4 # float | In meters. (optional)
    trainer = 56 # int | Set to 1 to mark as a trainer activity. (optional)
    commute = 56 # int | Set to 1 to mark as commute. (optional)

    try:
        # Create an Activity
        api_response = api_instance.create_activity(name, sport_type, start_date_local, elapsed_time, type=type, description=description, distance=distance, trainer=trainer, commute=commute)
        print("The response of ActivitiesApi->create_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->create_activity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the activity. | 
 **sport_type** | **str**| Sport type of activity. For example - Run, MountainBikeRide, Ride, etc. | 
 **start_date_local** | **datetime**| ISO 8601 formatted date time. | 
 **elapsed_time** | **int**| In seconds. | 
 **type** | **str**| Type of activity. For example - Run, Ride etc. | [optional] 
 **description** | **str**| Description of the activity. | [optional] 
 **distance** | **float**| In meters. | [optional] 
 **trainer** | **int**| Set to 1 to mark as a trainer activity. | [optional] 
 **commute** | **int**| Set to 1 to mark as commute. | [optional] 

### Return type

[**DetailedActivity**](DetailedActivity.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The activity&#39;s detailed representation. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_by_id**
> DetailedActivity get_activity_by_id(id, include_all_efforts=include_all_efforts)

Get Activity

Returns the given activity that is owned by the authenticated athlete. Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.detailed_activity import DetailedActivity
from strava_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.strava.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = strava_python.Configuration(
    host = "https://www.strava.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with strava_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = strava_python.ActivitiesApi(api_client)
    id = 56 # int | The identifier of the activity.
    include_all_efforts = True # bool | To include all segments efforts. (optional)

    try:
        # Get Activity
        api_response = api_instance.get_activity_by_id(id, include_all_efforts=include_all_efforts)
        print("The response of ActivitiesApi->get_activity_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activity_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 
 **include_all_efforts** | **bool**| To include all segments efforts. | [optional] 

### Return type

[**DetailedActivity**](DetailedActivity.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The activity&#39;s detailed representation. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments_by_activity_id**
> List[Comment] get_comments_by_activity_id(id, page=page, per_page=per_page, page_size=page_size, after_cursor=after_cursor)

List Activity Comments

Returns the comments on the given activity. Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.comment import Comment
from strava_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.strava.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = strava_python.Configuration(
    host = "https://www.strava.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with strava_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = strava_python.ActivitiesApi(api_client)
    id = 56 # int | The identifier of the activity.
    page = 56 # int | Deprecated. Prefer to use after_cursor. (optional)
    per_page = 30 # int | Deprecated. Prefer to use page_size. (optional) (default to 30)
    page_size = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)
    after_cursor = 'after_cursor_example' # str | Cursor of the last item in the previous page of results, used to request the subsequent page of results.  When omitted, the first page of results is fetched. (optional)

    try:
        # List Activity Comments
        api_response = api_instance.get_comments_by_activity_id(id, page=page, per_page=per_page, page_size=page_size, after_cursor=after_cursor)
        print("The response of ActivitiesApi->get_comments_by_activity_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_comments_by_activity_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 
 **page** | **int**| Deprecated. Prefer to use after_cursor. | [optional] 
 **per_page** | **int**| Deprecated. Prefer to use page_size. | [optional] [default to 30]
 **page_size** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]
 **after_cursor** | **str**| Cursor of the last item in the previous page of results, used to request the subsequent page of results.  When omitted, the first page of results is fetched. | [optional] 

### Return type

[**List[Comment]**](Comment.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comments. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kudoers_by_activity_id**
> List[SummaryAthlete] get_kudoers_by_activity_id(id, page=page, per_page=per_page)

List Activity Kudoers

Returns the athletes who kudoed an activity identified by an identifier. Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.summary_athlete import SummaryAthlete
from strava_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.strava.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = strava_python.Configuration(
    host = "https://www.strava.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with strava_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = strava_python.ActivitiesApi(api_client)
    id = 56 # int | The identifier of the activity.
    page = 56 # int | Page number. Defaults to 1. (optional)
    per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

    try:
        # List Activity Kudoers
        api_response = api_instance.get_kudoers_by_activity_id(id, page=page, per_page=per_page)
        print("The response of ActivitiesApi->get_kudoers_by_activity_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_kudoers_by_activity_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 
 **page** | **int**| Page number. Defaults to 1. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**List[SummaryAthlete]**](SummaryAthlete.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comments. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_laps_by_activity_id**
> List[Lap] get_laps_by_activity_id(id)

List Activity Laps

Returns the laps of an activity identified by an identifier. Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.lap import Lap
from strava_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.strava.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = strava_python.Configuration(
    host = "https://www.strava.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with strava_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = strava_python.ActivitiesApi(api_client)
    id = 56 # int | The identifier of the activity.

    try:
        # List Activity Laps
        api_response = api_instance.get_laps_by_activity_id(id)
        print("The response of ActivitiesApi->get_laps_by_activity_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_laps_by_activity_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 

### Return type

[**List[Lap]**](Lap.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activity Laps. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_in_athlete_activities**
> List[SummaryActivity] get_logged_in_athlete_activities(before=before, after=after, page=page, per_page=per_page)

List Athlete Activities

Returns the activities of an athlete for a specific identifier. Requires activity:read. Only Me activities will be filtered out unless requested by a token with activity:read_all.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.summary_activity import SummaryActivity
from strava_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.strava.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = strava_python.Configuration(
    host = "https://www.strava.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with strava_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = strava_python.ActivitiesApi(api_client)
    before = 56 # int | An epoch timestamp to use for filtering activities that have taken place before a certain time. (optional)
    after = 56 # int | An epoch timestamp to use for filtering activities that have taken place after a certain time. (optional)
    page = 56 # int | Page number. Defaults to 1. (optional)
    per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

    try:
        # List Athlete Activities
        api_response = api_instance.get_logged_in_athlete_activities(before=before, after=after, page=page, per_page=per_page)
        print("The response of ActivitiesApi->get_logged_in_athlete_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_logged_in_athlete_activities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **int**| An epoch timestamp to use for filtering activities that have taken place before a certain time. | [optional] 
 **after** | **int**| An epoch timestamp to use for filtering activities that have taken place after a certain time. | [optional] 
 **page** | **int**| Page number. Defaults to 1. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**List[SummaryActivity]**](SummaryActivity.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The authenticated athlete&#39;s activities |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zones_by_activity_id**
> List[ActivityZone] get_zones_by_activity_id(id)

Get Activity Zones

Summit Feature. Returns the zones of a given activity. Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.activity_zone import ActivityZone
from strava_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.strava.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = strava_python.Configuration(
    host = "https://www.strava.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with strava_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = strava_python.ActivitiesApi(api_client)
    id = 56 # int | The identifier of the activity.

    try:
        # Get Activity Zones
        api_response = api_instance.get_zones_by_activity_id(id)
        print("The response of ActivitiesApi->get_zones_by_activity_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_zones_by_activity_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 

### Return type

[**List[ActivityZone]**](ActivityZone.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activity Zones. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity_by_id**
> DetailedActivity update_activity_by_id(id, body=body)

Update Activity

Updates the given activity that is owned by the authenticated athlete. Requires activity:write. Also requires activity:read_all in order to update Only Me activities

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.detailed_activity import DetailedActivity
from strava_python.models.updatable_activity import UpdatableActivity
from strava_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.strava.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = strava_python.Configuration(
    host = "https://www.strava.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with strava_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = strava_python.ActivitiesApi(api_client)
    id = 56 # int | The identifier of the activity.
    body = strava_python.UpdatableActivity() # UpdatableActivity |  (optional)

    try:
        # Update Activity
        api_response = api_instance.update_activity_by_id(id, body=body)
        print("The response of ActivitiesApi->update_activity_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->update_activity_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 
 **body** | [**UpdatableActivity**](UpdatableActivity.md)|  | [optional] 

### Return type

[**DetailedActivity**](DetailedActivity.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The activity&#39;s detailed representation. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# strava_python.ClubsApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_club_activities_by_id**](ClubsApi.md#get_club_activities_by_id) | **GET** /clubs/{id}/activities | List Club Activities
[**get_club_admins_by_id**](ClubsApi.md#get_club_admins_by_id) | **GET** /clubs/{id}/admins | List Club Administrators
[**get_club_by_id**](ClubsApi.md#get_club_by_id) | **GET** /clubs/{id} | Get Club
[**get_club_members_by_id**](ClubsApi.md#get_club_members_by_id) | **GET** /clubs/{id}/members | List Club Members
[**get_logged_in_athlete_clubs**](ClubsApi.md#get_logged_in_athlete_clubs) | **GET** /athlete/clubs | List Athlete Clubs


# **get_club_activities_by_id**
> List[ClubActivity] get_club_activities_by_id(id, page=page, per_page=per_page)

List Club Activities

Retrieve recent activities from members of a specific club. The authenticated athlete must belong to the requested club in order to hit this endpoint. Pagination is supported. Athlete profile visibility is respected for all activities.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.club_activity import ClubActivity
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
    api_instance = strava_python.ClubsApi(api_client)
    id = 56 # int | The identifier of the club.
    page = 56 # int | Page number. Defaults to 1. (optional)
    per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

    try:
        # List Club Activities
        api_response = api_instance.get_club_activities_by_id(id, page=page, per_page=per_page)
        print("The response of ClubsApi->get_club_activities_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubsApi->get_club_activities_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the club. | 
 **page** | **int**| Page number. Defaults to 1. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**List[ClubActivity]**](ClubActivity.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of activities. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_admins_by_id**
> List[SummaryAthlete] get_club_admins_by_id(id, page=page, per_page=per_page)

List Club Administrators

Returns a list of the administrators of a given club.

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
    api_instance = strava_python.ClubsApi(api_client)
    id = 56 # int | The identifier of the club.
    page = 56 # int | Page number. Defaults to 1. (optional)
    per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

    try:
        # List Club Administrators
        api_response = api_instance.get_club_admins_by_id(id, page=page, per_page=per_page)
        print("The response of ClubsApi->get_club_admins_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubsApi->get_club_admins_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the club. | 
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
**200** | A list of summary athlete representations. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_by_id**
> DetailedClub get_club_by_id(id)

Get Club

Returns a given club using its identifier.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.detailed_club import DetailedClub
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
    api_instance = strava_python.ClubsApi(api_client)
    id = 56 # int | The identifier of the club.

    try:
        # Get Club
        api_response = api_instance.get_club_by_id(id)
        print("The response of ClubsApi->get_club_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubsApi->get_club_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the club. | 

### Return type

[**DetailedClub**](DetailedClub.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The detailed representation of a club. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_members_by_id**
> List[ClubAthlete] get_club_members_by_id(id, page=page, per_page=per_page)

List Club Members

Returns a list of the athletes who are members of a given club.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.club_athlete import ClubAthlete
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
    api_instance = strava_python.ClubsApi(api_client)
    id = 56 # int | The identifier of the club.
    page = 56 # int | Page number. Defaults to 1. (optional)
    per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

    try:
        # List Club Members
        api_response = api_instance.get_club_members_by_id(id, page=page, per_page=per_page)
        print("The response of ClubsApi->get_club_members_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubsApi->get_club_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the club. | 
 **page** | **int**| Page number. Defaults to 1. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**List[ClubAthlete]**](ClubAthlete.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of club athlete representations. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_in_athlete_clubs**
> List[SummaryClub] get_logged_in_athlete_clubs(page=page, per_page=per_page)

List Athlete Clubs

Returns a list of the clubs whose membership includes the authenticated athlete.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.summary_club import SummaryClub
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
    api_instance = strava_python.ClubsApi(api_client)
    page = 56 # int | Page number. Defaults to 1. (optional)
    per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

    try:
        # List Athlete Clubs
        api_response = api_instance.get_logged_in_athlete_clubs(page=page, per_page=per_page)
        print("The response of ClubsApi->get_logged_in_athlete_clubs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubsApi->get_logged_in_athlete_clubs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. Defaults to 1. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**List[SummaryClub]**](SummaryClub.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of summary club representations. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


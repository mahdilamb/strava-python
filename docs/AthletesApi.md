# strava_python.AthletesApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logged_in_athlete**](AthletesApi.md#get_logged_in_athlete) | **GET** /athlete | Get Authenticated Athlete
[**get_logged_in_athlete_zones**](AthletesApi.md#get_logged_in_athlete_zones) | **GET** /athlete/zones | Get Zones
[**get_stats**](AthletesApi.md#get_stats) | **GET** /athletes/{id}/stats | Get Athlete Stats
[**update_logged_in_athlete**](AthletesApi.md#update_logged_in_athlete) | **PUT** /athlete | Update Athlete


# **get_logged_in_athlete**
> DetailedAthlete get_logged_in_athlete()

Get Authenticated Athlete

Returns the currently authenticated athlete. Tokens with profile:read_all scope will receive a detailed athlete representation; all others will receive a summary representation.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.detailed_athlete import DetailedAthlete
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
    api_instance = strava_python.AthletesApi(api_client)

    try:
        # Get Authenticated Athlete
        api_response = api_instance.get_logged_in_athlete()
        print("The response of AthletesApi->get_logged_in_athlete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->get_logged_in_athlete: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**DetailedAthlete**](DetailedAthlete.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profile information for the authenticated athlete. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_in_athlete_zones**
> Zones get_logged_in_athlete_zones()

Get Zones

Returns the the authenticated athlete's heart rate and power zones. Requires profile:read_all.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.zones import Zones
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
    api_instance = strava_python.AthletesApi(api_client)

    try:
        # Get Zones
        api_response = api_instance.get_logged_in_athlete_zones()
        print("The response of AthletesApi->get_logged_in_athlete_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->get_logged_in_athlete_zones: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Zones**](Zones.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Heart rate and power zones. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> ActivityStats get_stats(id)

Get Athlete Stats

Returns the activity stats of an athlete. Only includes data from activities set to Everyone visibilty.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.activity_stats import ActivityStats
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
    api_instance = strava_python.AthletesApi(api_client)
    id = 56 # int | The identifier of the athlete. Must match the authenticated athlete.

    try:
        # Get Athlete Stats
        api_response = api_instance.get_stats(id)
        print("The response of AthletesApi->get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->get_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the athlete. Must match the authenticated athlete. | 

### Return type

[**ActivityStats**](ActivityStats.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activity stats of the athlete. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_logged_in_athlete**
> DetailedAthlete update_logged_in_athlete(weight)

Update Athlete

Update the currently authenticated athlete. Requires profile:write scope.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.detailed_athlete import DetailedAthlete
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
    api_instance = strava_python.AthletesApi(api_client)
    weight = 3.4 # float | The weight of the athlete in kilograms.

    try:
        # Update Athlete
        api_response = api_instance.update_logged_in_athlete(weight)
        print("The response of AthletesApi->update_logged_in_athlete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->update_logged_in_athlete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weight** | **float**| The weight of the athlete in kilograms. | 

### Return type

[**DetailedAthlete**](DetailedAthlete.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profile information for the authenticated athlete. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


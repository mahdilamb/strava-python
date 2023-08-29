# strava_python.RoutesApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_route_as_gpx**](RoutesApi.md#get_route_as_gpx) | **GET** /routes/{id}/export_gpx | Export Route GPX
[**get_route_as_tcx**](RoutesApi.md#get_route_as_tcx) | **GET** /routes/{id}/export_tcx | Export Route TCX
[**get_route_by_id**](RoutesApi.md#get_route_by_id) | **GET** /routes/{id} | Get Route
[**get_routes_by_athlete_id**](RoutesApi.md#get_routes_by_athlete_id) | **GET** /athletes/{id}/routes | List Athlete Routes


# **get_route_as_gpx**
> get_route_as_gpx(id)

Export Route GPX

Returns a GPX file of the route. Requires read_all scope for private routes.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
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
    api_instance = strava_python.RoutesApi(api_client)
    id = 56 # int | The identifier of the route.

    try:
        # Export Route GPX
        api_instance.get_route_as_gpx(id)
    except Exception as e:
        print("Exception when calling RoutesApi->get_route_as_gpx: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the route. | 

### Return type

void (empty response body)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A GPX file with the route. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_as_tcx**
> get_route_as_tcx(id)

Export Route TCX

Returns a TCX file of the route. Requires read_all scope for private routes.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
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
    api_instance = strava_python.RoutesApi(api_client)
    id = 56 # int | The identifier of the route.

    try:
        # Export Route TCX
        api_instance.get_route_as_tcx(id)
    except Exception as e:
        print("Exception when calling RoutesApi->get_route_as_tcx: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the route. | 

### Return type

void (empty response body)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A TCX file with the route. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_by_id**
> Route get_route_by_id(id)

Get Route

Returns a route using its identifier. Requires read_all scope for private routes.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.route import Route
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
    api_instance = strava_python.RoutesApi(api_client)
    id = 56 # int | The identifier of the route.

    try:
        # Get Route
        api_response = api_instance.get_route_by_id(id)
        print("The response of RoutesApi->get_route_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->get_route_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the route. | 

### Return type

[**Route**](Route.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A representation of the route. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routes_by_athlete_id**
> List[Route] get_routes_by_athlete_id(page=page, per_page=per_page)

List Athlete Routes

Returns a list of the routes created by the authenticated athlete. Private routes are filtered out unless requested by a token with read_all scope.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.route import Route
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
    api_instance = strava_python.RoutesApi(api_client)
    page = 56 # int | Page number. Defaults to 1. (optional)
    per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

    try:
        # List Athlete Routes
        api_response = api_instance.get_routes_by_athlete_id(page=page, per_page=per_page)
        print("The response of RoutesApi->get_routes_by_athlete_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->get_routes_by_athlete_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. Defaults to 1. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**List[Route]**](Route.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A representation of the route. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


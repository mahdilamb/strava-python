# strava_python.StreamsApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activity_streams**](StreamsApi.md#get_activity_streams) | **GET** /activities/{id}/streams | Get Activity Streams
[**get_route_streams**](StreamsApi.md#get_route_streams) | **GET** /routes/{id}/streams | Get Route Streams
[**get_segment_effort_streams**](StreamsApi.md#get_segment_effort_streams) | **GET** /segment_efforts/{id}/streams | Get Segment Effort Streams
[**get_segment_streams**](StreamsApi.md#get_segment_streams) | **GET** /segments/{id}/streams | Get Segment Streams


# **get_activity_streams**
> StreamSet get_activity_streams(id, keys, key_by_type)

Get Activity Streams

Returns the given activity's streams. Requires activity:read scope. Requires activity:read_all scope for Only Me activities.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.stream_set import StreamSet
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
    api_instance = strava_python.StreamsApi(api_client)
    id = 56 # int | The identifier of the activity.
    keys = ['keys_example'] # List[str] | Desired stream types.
    key_by_type = True # bool | Must be true. (default to True)

    try:
        # Get Activity Streams
        api_response = api_instance.get_activity_streams(id, keys, key_by_type)
        print("The response of StreamsApi->get_activity_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->get_activity_streams: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 
 **keys** | [**List[str]**](str.md)| Desired stream types. | 
 **key_by_type** | **bool**| Must be true. | [default to True]

### Return type

[**StreamSet**](StreamSet.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The set of requested streams. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_streams**
> StreamSet get_route_streams(id)

Get Route Streams

Returns the given route's streams. Requires read_all scope for private routes.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.stream_set import StreamSet
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
    api_instance = strava_python.StreamsApi(api_client)
    id = 56 # int | The identifier of the route.

    try:
        # Get Route Streams
        api_response = api_instance.get_route_streams(id)
        print("The response of StreamsApi->get_route_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->get_route_streams: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the route. | 

### Return type

[**StreamSet**](StreamSet.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The set of requested streams. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment_effort_streams**
> StreamSet get_segment_effort_streams(id, keys, key_by_type)

Get Segment Effort Streams

Returns a set of streams for a segment effort completed by the authenticated athlete. Requires read_all scope.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.stream_set import StreamSet
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
    api_instance = strava_python.StreamsApi(api_client)
    id = 56 # int | The identifier of the segment effort.
    keys = ['keys_example'] # List[str] | The types of streams to return.
    key_by_type = True # bool | Must be true. (default to True)

    try:
        # Get Segment Effort Streams
        api_response = api_instance.get_segment_effort_streams(id, keys, key_by_type)
        print("The response of StreamsApi->get_segment_effort_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->get_segment_effort_streams: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the segment effort. | 
 **keys** | [**List[str]**](str.md)| The types of streams to return. | 
 **key_by_type** | **bool**| Must be true. | [default to True]

### Return type

[**StreamSet**](StreamSet.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The set of requested streams. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment_streams**
> StreamSet get_segment_streams(id, keys, key_by_type)

Get Segment Streams

Returns the given segment's streams. Requires read_all scope for private segments.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.stream_set import StreamSet
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
    api_instance = strava_python.StreamsApi(api_client)
    id = 56 # int | The identifier of the segment.
    keys = ['keys_example'] # List[str] | The types of streams to return.
    key_by_type = True # bool | Must be true. (default to True)

    try:
        # Get Segment Streams
        api_response = api_instance.get_segment_streams(id, keys, key_by_type)
        print("The response of StreamsApi->get_segment_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamsApi->get_segment_streams: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the segment. | 
 **keys** | [**List[str]**](str.md)| The types of streams to return. | 
 **key_by_type** | **bool**| Must be true. | [default to True]

### Return type

[**StreamSet**](StreamSet.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The set of requested streams. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


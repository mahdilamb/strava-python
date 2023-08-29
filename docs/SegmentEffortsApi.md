# strava_python.SegmentEffortsApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_efforts_by_segment_id**](SegmentEffortsApi.md#get_efforts_by_segment_id) | **GET** /segment_efforts | List Segment Efforts
[**get_segment_effort_by_id**](SegmentEffortsApi.md#get_segment_effort_by_id) | **GET** /segment_efforts/{id} | Get Segment Effort


# **get_efforts_by_segment_id**
> List[DetailedSegmentEffort] get_efforts_by_segment_id(segment_id, start_date_local=start_date_local, end_date_local=end_date_local, per_page=per_page)

List Segment Efforts

Returns a set of the authenticated athlete's segment efforts for a given segment.  Requires subscription.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.detailed_segment_effort import DetailedSegmentEffort
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
    api_instance = strava_python.SegmentEffortsApi(api_client)
    segment_id = 56 # int | The identifier of the segment.
    start_date_local = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 formatted date time. (optional)
    end_date_local = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 formatted date time. (optional)
    per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

    try:
        # List Segment Efforts
        api_response = api_instance.get_efforts_by_segment_id(segment_id, start_date_local=start_date_local, end_date_local=end_date_local, per_page=per_page)
        print("The response of SegmentEffortsApi->get_efforts_by_segment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentEffortsApi->get_efforts_by_segment_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **int**| The identifier of the segment. | 
 **start_date_local** | **datetime**| ISO 8601 formatted date time. | [optional] 
 **end_date_local** | **datetime**| ISO 8601 formatted date time. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**List[DetailedSegmentEffort]**](DetailedSegmentEffort.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of segment efforts. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment_effort_by_id**
> DetailedSegmentEffort get_segment_effort_by_id(id)

Get Segment Effort

Returns a segment effort from an activity that is owned by the authenticated athlete. Requires subscription.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.detailed_segment_effort import DetailedSegmentEffort
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
    api_instance = strava_python.SegmentEffortsApi(api_client)
    id = 56 # int | The identifier of the segment effort.

    try:
        # Get Segment Effort
        api_response = api_instance.get_segment_effort_by_id(id)
        print("The response of SegmentEffortsApi->get_segment_effort_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentEffortsApi->get_segment_effort_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the segment effort. | 

### Return type

[**DetailedSegmentEffort**](DetailedSegmentEffort.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Representation of a segment effort. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


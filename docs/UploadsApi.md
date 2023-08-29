# strava_python.UploadsApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_upload**](UploadsApi.md#create_upload) | **POST** /uploads | Upload Activity
[**get_upload_by_id**](UploadsApi.md#get_upload_by_id) | **GET** /uploads/{uploadId} | Get Upload


# **create_upload**
> Upload create_upload(file=file, name=name, description=description, trainer=trainer, commute=commute, data_type=data_type, external_id=external_id)

Upload Activity

Uploads a new data file to create an activity from. Requires activity:write scope.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.upload import Upload
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
    api_instance = strava_python.UploadsApi(api_client)
    file = None # bytearray | The uploaded file. (optional)
    name = 'name_example' # str | The desired name of the resulting activity. (optional)
    description = 'description_example' # str | The desired description of the resulting activity. (optional)
    trainer = 'trainer_example' # str | Whether the resulting activity should be marked as having been performed on a trainer. (optional)
    commute = 'commute_example' # str | Whether the resulting activity should be tagged as a commute. (optional)
    data_type = 'data_type_example' # str | The format of the uploaded file. (optional)
    external_id = 'external_id_example' # str | The desired external identifier of the resulting activity. (optional)

    try:
        # Upload Activity
        api_response = api_instance.create_upload(file=file, name=name, description=description, trainer=trainer, commute=commute, data_type=data_type, external_id=external_id)
        print("The response of UploadsApi->create_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->create_upload: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| The uploaded file. | [optional] 
 **name** | **str**| The desired name of the resulting activity. | [optional] 
 **description** | **str**| The desired description of the resulting activity. | [optional] 
 **trainer** | **str**| Whether the resulting activity should be marked as having been performed on a trainer. | [optional] 
 **commute** | **str**| Whether the resulting activity should be tagged as a commute. | [optional] 
 **data_type** | **str**| The format of the uploaded file. | [optional] 
 **external_id** | **str**| The desired external identifier of the resulting activity. | [optional] 

### Return type

[**Upload**](Upload.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A representation of the created upload. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_by_id**
> Upload get_upload_by_id(upload_id)

Get Upload

Returns an upload for a given identifier. Requires activity:write scope.

### Example

* OAuth Authentication (strava_oauth):
```python
import time
import os
import strava_python
from strava_python.models.upload import Upload
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
    api_instance = strava_python.UploadsApi(api_client)
    upload_id = 56 # int | The identifier of the upload.

    try:
        # Get Upload
        api_response = api_instance.get_upload_by_id(upload_id)
        print("The response of UploadsApi->get_upload_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->get_upload_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **int**| The identifier of the upload. | 

### Return type

[**Upload**](Upload.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Representation of the upload. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


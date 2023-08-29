# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr, conlist, validator

from strava_python.models.stream_set import StreamSet

from strava_python.api_client import ApiClient
from strava_python.api_response import ApiResponse
from strava_python.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class StreamsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_activity_streams(self, id : Annotated[StrictInt, Field(..., description="The identifier of the activity.")], keys : Annotated[conlist(StrictStr, min_length=1), Field(..., description="Desired stream types.")], key_by_type : Annotated[StrictBool, Field(..., description="Must be true.")], **kwargs) -> StreamSet:  # noqa: E501
        """Get Activity Streams  # noqa: E501

        Returns the given activity's streams. Requires activity:read scope. Requires activity:read_all scope for Only Me activities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_activity_streams(id, keys, key_by_type, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the activity. (required)
        :type id: int
        :param keys: Desired stream types. (required)
        :type keys: List[str]
        :param key_by_type: Must be true. (required)
        :type key_by_type: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StreamSet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_activity_streams_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_activity_streams_with_http_info(id, keys, key_by_type, **kwargs)  # noqa: E501

    @validate_arguments
    def get_activity_streams_with_http_info(self, id : Annotated[StrictInt, Field(..., description="The identifier of the activity.")], keys : Annotated[conlist(StrictStr, min_length=1), Field(..., description="Desired stream types.")], key_by_type : Annotated[StrictBool, Field(..., description="Must be true.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Activity Streams  # noqa: E501

        Returns the given activity's streams. Requires activity:read scope. Requires activity:read_all scope for Only Me activities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_activity_streams_with_http_info(id, keys, key_by_type, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the activity. (required)
        :type id: int
        :param keys: Desired stream types. (required)
        :type keys: List[str]
        :param key_by_type: Must be true. (required)
        :type key_by_type: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(StreamSet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'keys',
            'key_by_type'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_activity_streams" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('keys') is not None:  # noqa: E501
            _query_params.append(('keys', _params['keys']))
            _collection_formats['keys'] = 'csv'

        if _params.get('key_by_type') is not None:  # noqa: E501
            _query_params.append(('key_by_type', _params['key_by_type']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['strava_oauth']  # noqa: E501

        _response_types_map = {
            '200': "StreamSet",
        }

        return self.api_client.call_api(
            '/activities/{id}/streams', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_route_streams(self, id : Annotated[StrictInt, Field(..., description="The identifier of the route.")], **kwargs) -> StreamSet:  # noqa: E501
        """Get Route Streams  # noqa: E501

        Returns the given route's streams. Requires read_all scope for private routes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_route_streams(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the route. (required)
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StreamSet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_route_streams_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_route_streams_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_route_streams_with_http_info(self, id : Annotated[StrictInt, Field(..., description="The identifier of the route.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Route Streams  # noqa: E501

        Returns the given route's streams. Requires read_all scope for private routes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_route_streams_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the route. (required)
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(StreamSet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_route_streams" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['strava_oauth']  # noqa: E501

        _response_types_map = {
            '200': "StreamSet",
        }

        return self.api_client.call_api(
            '/routes/{id}/streams', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_segment_effort_streams(self, id : Annotated[StrictInt, Field(..., description="The identifier of the segment effort.")], keys : Annotated[conlist(StrictStr, min_length=1), Field(..., description="The types of streams to return.")], key_by_type : Annotated[StrictBool, Field(..., description="Must be true.")], **kwargs) -> StreamSet:  # noqa: E501
        """Get Segment Effort Streams  # noqa: E501

        Returns a set of streams for a segment effort completed by the authenticated athlete. Requires read_all scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_segment_effort_streams(id, keys, key_by_type, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the segment effort. (required)
        :type id: int
        :param keys: The types of streams to return. (required)
        :type keys: List[str]
        :param key_by_type: Must be true. (required)
        :type key_by_type: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StreamSet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_segment_effort_streams_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_segment_effort_streams_with_http_info(id, keys, key_by_type, **kwargs)  # noqa: E501

    @validate_arguments
    def get_segment_effort_streams_with_http_info(self, id : Annotated[StrictInt, Field(..., description="The identifier of the segment effort.")], keys : Annotated[conlist(StrictStr, min_length=1), Field(..., description="The types of streams to return.")], key_by_type : Annotated[StrictBool, Field(..., description="Must be true.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Segment Effort Streams  # noqa: E501

        Returns a set of streams for a segment effort completed by the authenticated athlete. Requires read_all scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_segment_effort_streams_with_http_info(id, keys, key_by_type, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the segment effort. (required)
        :type id: int
        :param keys: The types of streams to return. (required)
        :type keys: List[str]
        :param key_by_type: Must be true. (required)
        :type key_by_type: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(StreamSet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'keys',
            'key_by_type'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_segment_effort_streams" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('keys') is not None:  # noqa: E501
            _query_params.append(('keys', _params['keys']))
            _collection_formats['keys'] = 'csv'

        if _params.get('key_by_type') is not None:  # noqa: E501
            _query_params.append(('key_by_type', _params['key_by_type']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['strava_oauth']  # noqa: E501

        _response_types_map = {
            '200': "StreamSet",
        }

        return self.api_client.call_api(
            '/segment_efforts/{id}/streams', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_segment_streams(self, id : Annotated[StrictInt, Field(..., description="The identifier of the segment.")], keys : Annotated[conlist(StrictStr, min_length=1), Field(..., description="The types of streams to return.")], key_by_type : Annotated[StrictBool, Field(..., description="Must be true.")], **kwargs) -> StreamSet:  # noqa: E501
        """Get Segment Streams  # noqa: E501

        Returns the given segment's streams. Requires read_all scope for private segments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_segment_streams(id, keys, key_by_type, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the segment. (required)
        :type id: int
        :param keys: The types of streams to return. (required)
        :type keys: List[str]
        :param key_by_type: Must be true. (required)
        :type key_by_type: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StreamSet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_segment_streams_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_segment_streams_with_http_info(id, keys, key_by_type, **kwargs)  # noqa: E501

    @validate_arguments
    def get_segment_streams_with_http_info(self, id : Annotated[StrictInt, Field(..., description="The identifier of the segment.")], keys : Annotated[conlist(StrictStr, min_length=1), Field(..., description="The types of streams to return.")], key_by_type : Annotated[StrictBool, Field(..., description="Must be true.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Segment Streams  # noqa: E501

        Returns the given segment's streams. Requires read_all scope for private segments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_segment_streams_with_http_info(id, keys, key_by_type, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the segment. (required)
        :type id: int
        :param keys: The types of streams to return. (required)
        :type keys: List[str]
        :param key_by_type: Must be true. (required)
        :type key_by_type: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(StreamSet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'keys',
            'key_by_type'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_segment_streams" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('keys') is not None:  # noqa: E501
            _query_params.append(('keys', _params['keys']))
            _collection_formats['keys'] = 'csv'

        if _params.get('key_by_type') is not None:  # noqa: E501
            _query_params.append(('key_by_type', _params['key_by_type']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['strava_oauth']  # noqa: E501

        _response_types_map = {
            '200': "StreamSet",
        }

        return self.api_client.call_api(
            '/segments/{id}/streams', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

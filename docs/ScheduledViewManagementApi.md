# sumologic_client.ScheduledViewManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scheduled_view**](ScheduledViewManagementApi.md#create_scheduled_view) | **POST** /v1/scheduledViews | Create a new scheduled view.
[**disable_scheduled_view**](ScheduledViewManagementApi.md#disable_scheduled_view) | **DELETE** /v1/scheduledViews/{id}/disable | Disable a scheduled view.
[**get_scheduled_view**](ScheduledViewManagementApi.md#get_scheduled_view) | **GET** /v1/scheduledViews/{id} | Get a scheduled view.
[**list_scheduled_views**](ScheduledViewManagementApi.md#list_scheduled_views) | **GET** /v1/scheduledViews | Get a list of scheduled views.
[**pause_scheduled_view**](ScheduledViewManagementApi.md#pause_scheduled_view) | **POST** /v1/scheduledViews/{id}/pause | Pause a scheduled view.
[**start_scheduled_view**](ScheduledViewManagementApi.md#start_scheduled_view) | **POST** /v1/scheduledViews/{id}/start | Start a scheduled view.
[**update_scheduled_view**](ScheduledViewManagementApi.md#update_scheduled_view) | **PUT** /v1/scheduledViews/{id} | Update a scheduled view.


# **create_scheduled_view**
> ScheduledView create_scheduled_view(create_scheduled_view_definition)

Create a new scheduled view.

Creates a new scheduled view in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import scheduled_view_management_api
from sumologic_client.model.scheduled_view import ScheduledView
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.create_scheduled_view_definition import CreateScheduledViewDefinition
from pprint import pprint
# Defining the host is optional and defaults to https://api.au.sumologic.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sumologic_client.Configuration(
    host = "https://api.au.sumologic.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = sumologic_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sumologic_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scheduled_view_management_api.ScheduledViewManagementApi(api_client)
    create_scheduled_view_definition = CreateScheduledViewDefinition(
        query="_sourcecategory=*/Apache",
        index_name="TestScheduledView",
        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        retention_period=365,
        data_forwarding_id="data_forwarding_id_example",
        parsing_mode="AutoParse",
    ) # CreateScheduledViewDefinition | Information about the new scheduled view.

    # example passing only required values which don't have defaults set
    try:
        # Create a new scheduled view.
        api_response = api_instance.create_scheduled_view(create_scheduled_view_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ScheduledViewManagementApi->create_scheduled_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_scheduled_view_definition** | [**CreateScheduledViewDefinition**](CreateScheduledViewDefinition.md)| Information about the new scheduled view. |

### Return type

[**ScheduledView**](ScheduledView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scheduled view has been created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_scheduled_view**
> disable_scheduled_view(id)

Disable a scheduled view.

Disable a scheduled view with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import scheduled_view_management_api
from sumologic_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.au.sumologic.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sumologic_client.Configuration(
    host = "https://api.au.sumologic.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = sumologic_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sumologic_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scheduled_view_management_api.ScheduledViewManagementApi(api_client)
    id = "id_example" # str | Identifier of the scheduled view to disable.

    # example passing only required values which don't have defaults set
    try:
        # Disable a scheduled view.
        api_instance.disable_scheduled_view(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling ScheduledViewManagementApi->disable_scheduled_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the scheduled view to disable. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The scheduled view was disabled successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_view**
> ScheduledView get_scheduled_view(id)

Get a scheduled view.

Get a scheduled view with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import scheduled_view_management_api
from sumologic_client.model.scheduled_view import ScheduledView
from sumologic_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.au.sumologic.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sumologic_client.Configuration(
    host = "https://api.au.sumologic.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = sumologic_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sumologic_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scheduled_view_management_api.ScheduledViewManagementApi(api_client)
    id = "id_example" # str | Identifier of the scheduled view to fetch.

    # example passing only required values which don't have defaults set
    try:
        # Get a scheduled view.
        api_response = api_instance.get_scheduled_view(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ScheduledViewManagementApi->get_scheduled_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the scheduled view to fetch. |

### Return type

[**ScheduledView**](ScheduledView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled view object that was requested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scheduled_views**
> ListScheduledViewsResponse list_scheduled_views()

Get a list of scheduled views.

Get a list of all scheduled views in the organization. The response is paginated with a default limit of 100 scheduled views per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import scheduled_view_management_api
from sumologic_client.model.list_scheduled_views_response import ListScheduledViewsResponse
from sumologic_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.au.sumologic.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sumologic_client.Configuration(
    host = "https://api.au.sumologic.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = sumologic_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sumologic_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scheduled_view_management_api.ScheduledViewManagementApi(api_client)
    limit = 100 # int | Limit the number of scheduled views returned in the response. The number of scheduled views returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. `token` is set to null when no more pages are left. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of scheduled views.
        api_response = api_instance.list_scheduled_views(limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ScheduledViewManagementApi->list_scheduled_views: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of scheduled views returned in the response. The number of scheduled views returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. &#x60;token&#x60; is set to null when no more pages are left. | [optional]

### Return type

[**ListScheduledViewsResponse**](ListScheduledViewsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of scheduled views in the organization. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_scheduled_view**
> ScheduledView pause_scheduled_view(id)

Pause a scheduled view.

Pause a scheduled view with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import scheduled_view_management_api
from sumologic_client.model.scheduled_view import ScheduledView
from sumologic_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.au.sumologic.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sumologic_client.Configuration(
    host = "https://api.au.sumologic.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = sumologic_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sumologic_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scheduled_view_management_api.ScheduledViewManagementApi(api_client)
    id = "id_example" # str | Identifier of the scheduled view to pause.

    # example passing only required values which don't have defaults set
    try:
        # Pause a scheduled view.
        api_response = api_instance.pause_scheduled_view(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ScheduledViewManagementApi->pause_scheduled_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the scheduled view to pause. |

### Return type

[**ScheduledView**](ScheduledView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scheduled view was paused successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_scheduled_view**
> ScheduledView start_scheduled_view(id)

Start a scheduled view.

Start a scheduled view with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import scheduled_view_management_api
from sumologic_client.model.scheduled_view import ScheduledView
from sumologic_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.au.sumologic.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sumologic_client.Configuration(
    host = "https://api.au.sumologic.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = sumologic_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sumologic_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scheduled_view_management_api.ScheduledViewManagementApi(api_client)
    id = "id_example" # str | Identifier of the scheduled view to start.

    # example passing only required values which don't have defaults set
    try:
        # Start a scheduled view.
        api_response = api_instance.start_scheduled_view(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ScheduledViewManagementApi->start_scheduled_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the scheduled view to start. |

### Return type

[**ScheduledView**](ScheduledView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scheduled view was started successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scheduled_view**
> ScheduledView update_scheduled_view(id, update_scheduled_view_definition)

Update a scheduled view.

Update an existing scheduled view.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import scheduled_view_management_api
from sumologic_client.model.scheduled_view import ScheduledView
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.update_scheduled_view_definition import UpdateScheduledViewDefinition
from pprint import pprint
# Defining the host is optional and defaults to https://api.au.sumologic.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sumologic_client.Configuration(
    host = "https://api.au.sumologic.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = sumologic_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sumologic_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scheduled_view_management_api.ScheduledViewManagementApi(api_client)
    id = "id_example" # str | Identifier of the scheduled view to update.
    update_scheduled_view_definition = UpdateScheduledViewDefinition(
        data_forwarding_id="data_forwarding_id_example",
        retention_period=365,
        reduce_retention_period_immediately=False,
    ) # UpdateScheduledViewDefinition | Information to update about the scheduled view.

    # example passing only required values which don't have defaults set
    try:
        # Update a scheduled view.
        api_response = api_instance.update_scheduled_view(id, update_scheduled_view_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ScheduledViewManagementApi->update_scheduled_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the scheduled view to update. |
 **update_scheduled_view_definition** | [**UpdateScheduledViewDefinition**](UpdateScheduledViewDefinition.md)| Information to update about the scheduled view. |

### Return type

[**ScheduledView**](ScheduledView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scheduled view was successfully modified. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


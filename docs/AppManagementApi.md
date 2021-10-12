# sumologic_client.AppManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app**](AppManagementApi.md#get_app) | **GET** /v1/apps/{uuid} | Get an app by UUID.
[**get_async_install_status**](AppManagementApi.md#get_async_install_status) | **GET** /v1/apps/install/{jobId}/status | App install job status.
[**install_app**](AppManagementApi.md#install_app) | **POST** /v1/apps/{uuid}/install | Install an app by UUID.
[**list_apps**](AppManagementApi.md#list_apps) | **GET** /v1/apps | List available apps.


# **get_app**
> App get_app(uuid)

Get an app by UUID.

Gets the app with the given universally unique identifier (UUID).

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import app_management_api
from sumologic_client.model.app import App
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
    api_instance = app_management_api.AppManagementApi(api_client)
    uuid = "uuid_example" # str | The identifier of the app to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Get an app by UUID.
        api_response = api_instance.get_app(uuid)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AppManagementApi->get_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The identifier of the app to retrieve. |

### Return type

[**App**](App.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The retrieved app. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_install_status**
> AsyncJobStatus get_async_install_status(job_id)

App install job status.

Get the status of an asynchronous app install request for the given job identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import app_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.async_job_status import AsyncJobStatus
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
    api_instance = app_management_api.AppManagementApi(api_client)
    job_id = "jobId_example" # str | The identifier of the asynchronous install job.

    # example passing only required values which don't have defaults set
    try:
        # App install job status.
        api_response = api_instance.get_async_install_status(job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AppManagementApi->get_async_install_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The identifier of the asynchronous install job. |

### Return type

[**AsyncJobStatus**](AsyncJobStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of the app install job. |  -  |
**0** | App installation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_app**
> BeginAsyncJobResponse install_app(uuid, app_install_request)

Install an app by UUID.

Installs the app with given UUID in the folder specified using destinationFolderId.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import app_management_api
from sumologic_client.model.app_install_request import AppInstallRequest
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.begin_async_job_response import BeginAsyncJobResponse
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
    api_instance = app_management_api.AppManagementApi(api_client)
    uuid = "uuid_example" # str | UUID of the app to install.
    app_install_request = AppInstallRequest(
        name="Sumo Logic Configuration App",
        description="Sumo Logic Configuration App to configure collectors and data sources",
        destination_folder_id="00000000000001C8",
        data_source_values={
            "key": "key_example",
        },
    ) # AppInstallRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Install an app by UUID.
        api_response = api_instance.install_app(uuid, app_install_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AppManagementApi->install_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the app to install. |
 **app_install_request** | [**AppInstallRequest**](AppInstallRequest.md)|  |

### Return type

[**BeginAsyncJobResponse**](BeginAsyncJobResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App install job has been scheduled. |  -  |
**0** | App installation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps**
> ListAppsResult list_apps()

List available apps.

Lists all available apps from the App Catalog.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import app_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_apps_result import ListAppsResult
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
    api_instance = app_management_api.AppManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List available apps.
        api_response = api_instance.list_apps()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AppManagementApi->list_apps: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAppsResult**](ListAppsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all available apps. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


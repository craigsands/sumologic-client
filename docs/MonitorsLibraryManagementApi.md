# sumologic_client.MonitorsLibraryManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_monitor_by_ids**](MonitorsLibraryManagementApi.md#disable_monitor_by_ids) | **PUT** /v1/monitors/disable | Disable monitors.
[**get_monitor_usage_info**](MonitorsLibraryManagementApi.md#get_monitor_usage_info) | **GET** /v1/monitors/usageInfo | Usage info of monitors.
[**get_monitors_full_path**](MonitorsLibraryManagementApi.md#get_monitors_full_path) | **GET** /v1/monitors/{id}/path | Get the path of a monitor or folder.
[**get_monitors_library_root**](MonitorsLibraryManagementApi.md#get_monitors_library_root) | **GET** /v1/monitors/root | Get the root monitors folder.
[**monitors_copy**](MonitorsLibraryManagementApi.md#monitors_copy) | **POST** /v1/monitors/{id}/copy | Copy a monitor or folder.
[**monitors_create**](MonitorsLibraryManagementApi.md#monitors_create) | **POST** /v1/monitors | Create a monitor or folder. 
[**monitors_delete_by_id**](MonitorsLibraryManagementApi.md#monitors_delete_by_id) | **DELETE** /v1/monitors/{id} | Delete a monitor or folder. 
[**monitors_delete_by_ids**](MonitorsLibraryManagementApi.md#monitors_delete_by_ids) | **DELETE** /v1/monitors | Bulk delete a monitor or folder. 
[**monitors_export_item**](MonitorsLibraryManagementApi.md#monitors_export_item) | **GET** /v1/monitors/{id}/export | Export a monitor or folder.
[**monitors_get_by_path**](MonitorsLibraryManagementApi.md#monitors_get_by_path) | **GET** /v1/monitors/path | Read a monitor or folder by its path.
[**monitors_import_item**](MonitorsLibraryManagementApi.md#monitors_import_item) | **POST** /v1/monitors/{parentId}/import | Import a monitor or folder.
[**monitors_move**](MonitorsLibraryManagementApi.md#monitors_move) | **POST** /v1/monitors/{id}/move | Move a monitor or folder.
[**monitors_read_by_id**](MonitorsLibraryManagementApi.md#monitors_read_by_id) | **GET** /v1/monitors/{id} | Get a monitor or folder.
[**monitors_read_by_ids**](MonitorsLibraryManagementApi.md#monitors_read_by_ids) | **GET** /v1/monitors | Bulk read a monitor or folder.
[**monitors_search**](MonitorsLibraryManagementApi.md#monitors_search) | **GET** /v1/monitors/search | Search for a monitor or folder.
[**monitors_update_by_id**](MonitorsLibraryManagementApi.md#monitors_update_by_id) | **PUT** /v1/monitors/{id} | Update a monitor or folder. 


# **disable_monitor_by_ids**
> DisableMonitorResponse disable_monitor_by_ids(ids)

Disable monitors.

Bulk disable monitors by the given identifiers.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.disable_monitor_response import DisableMonitorResponse
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    ids = [
        "0000000000000001,0000000000000002,0000000000000003",
    ] # [str] | A comma-separated list of identifiers.

    # example passing only required values which don't have defaults set
    try:
        # Disable monitors.
        api_response = api_instance.disable_monitor_by_ids(ids)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->disable_monitor_by_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| A comma-separated list of identifiers. |

### Return type

[**DisableMonitorResponse**](DisableMonitorResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Disabled monitors |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitor_usage_info**
> MonitorUsageInfo get_monitor_usage_info()

Usage info of monitors.

Get the current number and the allowed number of log and metrics monitors.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.monitor_usage_info import MonitorUsageInfo
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Usage info of monitors.
        api_response = api_instance.get_monitor_usage_info()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->get_monitor_usage_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MonitorUsageInfo**](MonitorUsageInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MonitorUsageInfo has been retrieved successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitors_full_path**
> Path get_monitors_full_path(id)

Get the path of a monitor or folder.

Get the full path of the monitor or folder in the monitors library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.path import Path
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    id = "id_example" # str | Identifier of the monitor or folder.

    # example passing only required values which don't have defaults set
    try:
        # Get the path of a monitor or folder.
        api_response = api_instance.get_monitors_full_path(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->get_monitors_full_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the monitor or folder. |

### Return type

[**Path**](Path.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Full path of the monitor or folder. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitors_library_root**
> MonitorsLibraryFolderResponse get_monitors_library_root()

Get the root monitors folder.

Get the root folder in the monitors library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.monitors_library_folder_response import MonitorsLibraryFolderResponse
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the root monitors folder.
        api_response = api_instance.get_monitors_library_root()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->get_monitors_library_root: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MonitorsLibraryFolderResponse**](MonitorsLibraryFolderResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Root folder of the monitors library. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_copy**
> MonitorsLibraryBaseResponse monitors_copy(id, content_copy_params)

Copy a monitor or folder.

Copy a monitor or folder in the monitors library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.monitors_library_base_response import MonitorsLibraryBaseResponse
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.content_copy_params import ContentCopyParams
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    id = "id_example" # str | Identifier of the monitor or folder to copy.
    content_copy_params = ContentCopyParams(
        parent_id="parent_id_example",
        name="name_example",
        description="description_example",
    ) # ContentCopyParams | Fields include:   1) Identifier of the parent folder to copy to.   2) Optionally provide a new name.   3) Optionally provide a new description.   4) Optionally set to true if you want to copy and preserve the locked status. Requires `LockMonitors` capability.

    # example passing only required values which don't have defaults set
    try:
        # Copy a monitor or folder.
        api_response = api_instance.monitors_copy(id, content_copy_params)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_copy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the monitor or folder to copy. |
 **content_copy_params** | [**ContentCopyParams**](ContentCopyParams.md)| Fields include:   1) Identifier of the parent folder to copy to.   2) Optionally provide a new name.   3) Optionally provide a new description.   4) Optionally set to true if you want to copy and preserve the locked status. Requires &#x60;LockMonitors&#x60; capability. |

### Return type

[**MonitorsLibraryBaseResponse**](MonitorsLibraryBaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The monitor or folder was copied. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_create**
> MonitorsLibraryBaseResponse monitors_create(parent_id, monitors_library_base)

Create a monitor or folder. 

Create a monitor or folder in the monitors library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.monitors_library_base_response import MonitorsLibraryBaseResponse
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.monitors_library_base import MonitorsLibraryBase
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    parent_id = "parentId_example" # str | Identifier of the parent folder in which to create the monitor or folder.
    monitors_library_base = MonitorsLibraryBase() # MonitorsLibraryBase | The monitor or folder to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a monitor or folder. 
        api_response = api_instance.monitors_create(parent_id, monitors_library_base)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **str**| Identifier of the parent folder in which to create the monitor or folder. |
 **monitors_library_base** | [**MonitorsLibraryBase**](MonitorsLibraryBase.md)| The monitor or folder to create. |

### Return type

[**MonitorsLibraryBaseResponse**](MonitorsLibraryBaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The monitor or folder was created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_delete_by_id**
> monitors_delete_by_id(id)

Delete a monitor or folder. 

Delete a monitor or folder from the monitors library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    id = "id_example" # str | Identifier of the monitor or folder to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a monitor or folder. 
        api_instance.monitors_delete_by_id(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_delete_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the monitor or folder to delete. |

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
**204** | The monitor or folder was successfully deleted. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_delete_by_ids**
> IdToMonitorsLibraryBaseResponseMap monitors_delete_by_ids(ids)

Bulk delete a monitor or folder. 

Bulk delete a monitor or folder by the given identifiers in the monitors library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.id_to_monitors_library_base_response_map import IdToMonitorsLibraryBaseResponseMap
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    ids = [
        "0000000000000001,0000000000000002,0000000000000003",
    ] # [str] | A comma-separated list of identifiers.

    # example passing only required values which don't have defaults set
    try:
        # Bulk delete a monitor or folder. 
        api_response = api_instance.monitors_delete_by_ids(ids)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_delete_by_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| A comma-separated list of identifiers. |

### Return type

[**IdToMonitorsLibraryBaseResponseMap**](IdToMonitorsLibraryBaseResponseMap.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A map between the deleted identifier and its metadata. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_export_item**
> MonitorsLibraryBaseExport monitors_export_item(id)

Export a monitor or folder.

Export a monitor or folder. If the given identifier is a folder, everything under the folder is exported recursively with folder as the root.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.monitors_library_base_export import MonitorsLibraryBaseExport
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    id = "id_example" # str | Identifier of the monitor or folder to export.

    # example passing only required values which don't have defaults set
    try:
        # Export a monitor or folder.
        api_response = api_instance.monitors_export_item(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_export_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the monitor or folder to export. |

### Return type

[**MonitorsLibraryBaseExport**](MonitorsLibraryBaseExport.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exported monitor or folder. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_get_by_path**
> MonitorsLibraryBaseResponse monitors_get_by_path(path)

Read a monitor or folder by its path.

Read a monitor or folder by its path in the monitors library structure.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.monitors_library_base_response import MonitorsLibraryBaseResponse
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    path = "path_example" # str | The path of the monitor or folder.

    # example passing only required values which don't have defaults set
    try:
        # Read a monitor or folder by its path.
        api_response = api_instance.monitors_get_by_path(path)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_get_by_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path of the monitor or folder. |

### Return type

[**MonitorsLibraryBaseResponse**](MonitorsLibraryBaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested monitor or folder. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_import_item**
> MonitorsLibraryBaseResponse monitors_import_item(parent_id, monitors_library_base_export)

Import a monitor or folder.

Import a monitor or folder.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.monitors_library_base_response import MonitorsLibraryBaseResponse
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.monitors_library_base_export import MonitorsLibraryBaseExport
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    parent_id = "parentId_example" # str | Identifier of the parent folder in which to import the monitor or folder.
    monitors_library_base_export = MonitorsLibraryBaseExport() # MonitorsLibraryBaseExport | The monitor or folder to be imported.

    # example passing only required values which don't have defaults set
    try:
        # Import a monitor or folder.
        api_response = api_instance.monitors_import_item(parent_id, monitors_library_base_export)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_import_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **str**| Identifier of the parent folder in which to import the monitor or folder. |
 **monitors_library_base_export** | [**MonitorsLibraryBaseExport**](MonitorsLibraryBaseExport.md)| The monitor or folder to be imported. |

### Return type

[**MonitorsLibraryBaseResponse**](MonitorsLibraryBaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly imported monitor or folder. NOTE: Permissions field will not be filled (empty list). |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_move**
> MonitorsLibraryBaseResponse monitors_move(id, parent_id)

Move a monitor or folder.

Move a monitor or folder to a different location in the monitors library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.monitors_library_base_response import MonitorsLibraryBaseResponse
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    id = "id_example" # str | Identifier of the monitor or folder to move.
    parent_id = "parentId_example" # str | Identifier of the parent folder to move the monitor or folder to.

    # example passing only required values which don't have defaults set
    try:
        # Move a monitor or folder.
        api_response = api_instance.monitors_move(id, parent_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the monitor or folder to move. |
 **parent_id** | **str**| Identifier of the parent folder to move the monitor or folder to. |

### Return type

[**MonitorsLibraryBaseResponse**](MonitorsLibraryBaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Moved monitor or folder. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_read_by_id**
> MonitorsLibraryBaseResponse monitors_read_by_id(id)

Get a monitor or folder.

Get a monitor or folder from the monitors library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.monitors_library_base_response import MonitorsLibraryBaseResponse
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    id = "id_example" # str | Identifier of the monitor or folder to read.

    # example passing only required values which don't have defaults set
    try:
        # Get a monitor or folder.
        api_response = api_instance.monitors_read_by_id(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_read_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the monitor or folder to read. |

### Return type

[**MonitorsLibraryBaseResponse**](MonitorsLibraryBaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested monitor or folder. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_read_by_ids**
> IdToMonitorsLibraryBaseResponseMap monitors_read_by_ids(ids)

Bulk read a monitor or folder.

Bulk read a monitor or folder by the given identifiers from the monitors library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.id_to_monitors_library_base_response_map import IdToMonitorsLibraryBaseResponseMap
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    ids = [
        "0000000000000001,0000000000000002,0000000000000003",
    ] # [str] | A comma-separated list of identifiers.

    # example passing only required values which don't have defaults set
    try:
        # Bulk read a monitor or folder.
        api_response = api_instance.monitors_read_by_ids(ids)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_read_by_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| A comma-separated list of identifiers. |

### Return type

[**IdToMonitorsLibraryBaseResponseMap**](IdToMonitorsLibraryBaseResponseMap.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A map between an identifier and its definition (monitor or folder). |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_search**
> ListMonitorsLibraryItemWithPath monitors_search(query)

Search for a monitor or folder.

Search for a monitor or folder in the monitors library structure.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_monitors_library_item_with_path import ListMonitorsLibraryItemWithPath
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    query = "createdBy:000000000000968B Test" # str | The search query to find monitor or folder. Below is the list of different filters with examples:   - **createdBy** : Filter by the user's identifier who created the content. Example: `createdBy:000000000000968B`.   - **createdBefore** : Filter by the content objects created before the given timestamp(in milliseconds). Example: `createdBefore:1457997222`.   - **createdAfter** : Filter by the content objects created after the given timestamp(in milliseconds). Example: `createdAfter:1457997111`.   - **modifiedBefore** : Filter by the content objects modified before the given timestamp(in milliseconds). Example: `modifiedBefore:1457997222`.   - **modifiedAfter** : Filter by the content objects modified after the given timestamp(in milliseconds). Example: `modifiedAfter:1457997111`.   - **type** : Filter by the type of the content object. Example: `type:folder`.   - **monitorStatus** : Filter by the status of the monitor: Normal, Critical, Warning, MissingData, Disabled, AllTriggered. Example: `monitorStatus:Normal`.  You can also use multiple filters in one query. For example to search for all content objects created by user with identifier 000000000000968B with creation timestamp after 1457997222 containing the text Test, the query would look like:    `createdBy:000000000000968B createdAfter:1457997222 Test`
    limit = 10 # int | Maximum number of items you want in the response. (optional) if omitted the server will use the default value of 100
    offset = 5 # int | The position or row from where to start the search operation. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Search for a monitor or folder.
        api_response = api_instance.monitors_search(query)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_search: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for a monitor or folder.
        api_response = api_instance.monitors_search(query, limit=limit, offset=offset)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query to find monitor or folder. Below is the list of different filters with examples:   - **createdBy** : Filter by the user&#39;s identifier who created the content. Example: &#x60;createdBy:000000000000968B&#x60;.   - **createdBefore** : Filter by the content objects created before the given timestamp(in milliseconds). Example: &#x60;createdBefore:1457997222&#x60;.   - **createdAfter** : Filter by the content objects created after the given timestamp(in milliseconds). Example: &#x60;createdAfter:1457997111&#x60;.   - **modifiedBefore** : Filter by the content objects modified before the given timestamp(in milliseconds). Example: &#x60;modifiedBefore:1457997222&#x60;.   - **modifiedAfter** : Filter by the content objects modified after the given timestamp(in milliseconds). Example: &#x60;modifiedAfter:1457997111&#x60;.   - **type** : Filter by the type of the content object. Example: &#x60;type:folder&#x60;.   - **monitorStatus** : Filter by the status of the monitor: Normal, Critical, Warning, MissingData, Disabled, AllTriggered. Example: &#x60;monitorStatus:Normal&#x60;.  You can also use multiple filters in one query. For example to search for all content objects created by user with identifier 000000000000968B with creation timestamp after 1457997222 containing the text Test, the query would look like:    &#x60;createdBy:000000000000968B createdAfter:1457997222 Test&#x60; |
 **limit** | **int**| Maximum number of items you want in the response. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The position or row from where to start the search operation. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListMonitorsLibraryItemWithPath**](ListMonitorsLibraryItemWithPath.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of folders and monitors matching the search query. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitors_update_by_id**
> MonitorsLibraryBaseResponse monitors_update_by_id(id, monitors_library_base_update)

Update a monitor or folder. 

Update a monitor or folder in the monitors library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import monitors_library_management_api
from sumologic_client.model.monitors_library_base_update import MonitorsLibraryBaseUpdate
from sumologic_client.model.monitors_library_base_response import MonitorsLibraryBaseResponse
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
    api_instance = monitors_library_management_api.MonitorsLibraryManagementApi(api_client)
    id = "id_example" # str | Identifier of the monitor or folder to update.
    monitors_library_base_update = MonitorsLibraryBaseUpdate() # MonitorsLibraryBaseUpdate | The monitor or folder to update. The content version must match its latest version number in the monitors library. If the version does not match it will not be updated.

    # example passing only required values which don't have defaults set
    try:
        # Update a monitor or folder. 
        api_response = api_instance.monitors_update_by_id(id, monitors_library_base_update)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MonitorsLibraryManagementApi->monitors_update_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the monitor or folder to update. |
 **monitors_library_base_update** | [**MonitorsLibraryBaseUpdate**](MonitorsLibraryBaseUpdate.md)| The monitor or folder to update. The content version must match its latest version number in the monitors library. If the version does not match it will not be updated. |

### Return type

[**MonitorsLibraryBaseResponse**](MonitorsLibraryBaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The monitor or folder was updated. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


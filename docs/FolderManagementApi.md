# sumologic_client.FolderManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folder**](FolderManagementApi.md#create_folder) | **POST** /v2/content/folders | Create a new folder.
[**get_admin_recommended_folder_async**](FolderManagementApi.md#get_admin_recommended_folder_async) | **GET** /v2/content/folders/adminRecommended | Schedule Admin Recommended folder job
[**get_admin_recommended_folder_async_result**](FolderManagementApi.md#get_admin_recommended_folder_async_result) | **GET** /v2/content/folders/adminRecommended/{jobId}/result | Get Admin Recommended folder job result
[**get_admin_recommended_folder_async_status**](FolderManagementApi.md#get_admin_recommended_folder_async_status) | **GET** /v2/content/folders/adminRecommended/{jobId}/status | Get Admin Recommended folder job status
[**get_folder**](FolderManagementApi.md#get_folder) | **GET** /v2/content/folders/{id} | Get a folder.
[**get_global_folder_async**](FolderManagementApi.md#get_global_folder_async) | **GET** /v2/content/folders/global | Schedule Global View job
[**get_global_folder_async_result**](FolderManagementApi.md#get_global_folder_async_result) | **GET** /v2/content/folders/global/{jobId}/result | Get Global View job result
[**get_global_folder_async_status**](FolderManagementApi.md#get_global_folder_async_status) | **GET** /v2/content/folders/global/{jobId}/status | Get Global View job status
[**get_personal_folder**](FolderManagementApi.md#get_personal_folder) | **GET** /v2/content/folders/personal | Get personal folder.
[**update_folder**](FolderManagementApi.md#update_folder) | **PUT** /v2/content/folders/{id} | Update a folder.


# **create_folder**
> Folder create_folder(folder_definition)

Create a new folder.

Creates a new folder under the given parent folder. Set the header parameter `isAdminMode` to `\"true\"` to create a folder inside \"Admin Recommended\" folder.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import folder_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.folder import Folder
from sumologic_client.model.folder_definition import FolderDefinition
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
    api_instance = folder_management_api.FolderManagementApi(api_client)
    folder_definition = FolderDefinition(
        name="SampleFolder",
        description="This is a sample folder.",
        parent_id="parent_id_example",
    ) # FolderDefinition | Information about the new folder.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new folder.
        api_response = api_instance.create_folder(folder_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->create_folder: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new folder.
        api_response = api_instance.create_folder(folder_definition, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->create_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_definition** | [**FolderDefinition**](FolderDefinition.md)| Information about the new folder. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

### Return type

[**Folder**](Folder.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The folder has been created. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_recommended_folder_async**
> BeginAsyncJobResponse get_admin_recommended_folder_async()

Schedule Admin Recommended folder job

Schedule an asynchronous job to get the top-level Admin Recommended content items. You can read more about Admin Recommended folder [here](https://help.sumologic.com/Manage/Content_Sharing/Admin_Mode#move-important-content-to-admin-recommended).  _You get back a identifier of asynchronous job in response to this endpoint. See [Asynchronous-Request](#section/Getting-Started/Asynchronous-Request) section for more details on how to work with asynchronous request._

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import folder_management_api
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
    api_instance = folder_management_api.FolderManagementApi(api_client)
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Schedule Admin Recommended folder job
        api_response = api_instance.get_admin_recommended_folder_async(is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->get_admin_recommended_folder_async: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

### Return type

[**BeginAsyncJobResponse**](BeginAsyncJobResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An asynchronous job to get the Admin Recommended folder has been scheduled. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_recommended_folder_async_result**
> Folder get_admin_recommended_folder_async_result(job_id)

Get Admin Recommended folder job result

Get result of an Admin Recommended job for the given job identifier. The result will be \"Admin Recommended\" folder with a list of top-level Admin Recommended content items in `children` field.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import folder_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.folder import Folder
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
    api_instance = folder_management_api.FolderManagementApi(api_client)
    job_id = "jobId_example" # str | The identifier of the asynchronous Admin Recommended folder job.

    # example passing only required values which don't have defaults set
    try:
        # Get Admin Recommended folder job result
        api_response = api_instance.get_admin_recommended_folder_async_result(job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->get_admin_recommended_folder_async_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The identifier of the asynchronous Admin Recommended folder job. |

### Return type

[**Folder**](Folder.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Admin Recommended folder. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_recommended_folder_async_status**
> AsyncJobStatus get_admin_recommended_folder_async_status(job_id)

Get Admin Recommended folder job status

Get the status of an asynchronous Admin Recommended folder job for the given job identifier. If job succeeds, use [Admin Recommended Job Result](#operation/getAdminRecommendedFolderAsyncResult) endpoint to fetch top-level content items in Admin Recommended folder.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import folder_management_api
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
    api_instance = folder_management_api.FolderManagementApi(api_client)
    job_id = "jobId_example" # str | The identifier of the asynchronous Admin Recommended folder job.

    # example passing only required values which don't have defaults set
    try:
        # Get Admin Recommended folder job status
        api_response = api_instance.get_admin_recommended_folder_async_status(job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->get_admin_recommended_folder_async_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The identifier of the asynchronous Admin Recommended folder job. |

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
**200** | Asynchronous Admin Recommended folder job status. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> Folder get_folder(id)

Get a folder.

Get a folder with the given identifier. Set the header parameter `isAdminMode` to `\"true\"` if fetching a folder inside \"Admin Recommended\" folder.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import folder_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.folder import Folder
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
    api_instance = folder_management_api.FolderManagementApi(api_client)
    id = "id_example" # str | Identifier of the folder to fetch.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a folder.
        api_response = api_instance.get_folder(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->get_folder: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a folder.
        api_response = api_instance.get_folder(id, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->get_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the folder to fetch. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

### Return type

[**Folder**](Folder.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder that was requested. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_folder_async**
> BeginAsyncJobResponse get_global_folder_async()

Schedule Global View job

Schedule an asynchronous job to get Global View. Global View contains all top-level content items that a user has permissions to view in the organization. User can traverse the top-level folders using [GetFolder API](#operation/getFolder) to get rest of the content items. Make sure you set `isAdminMode` header parameter to `true` when traversing top-level items.  _Global View is not a real folder, therefore there is no folder identifier associated with it_.  _You get back a identifier of asynchronous job in response to this endpoint. See [Asynchronous-Request](#section/Getting-Started/Asynchronous-Request) section for more details on how to work with asynchronous request._

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import folder_management_api
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
    api_instance = folder_management_api.FolderManagementApi(api_client)
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Schedule Global View job
        api_response = api_instance.get_global_folder_async(is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->get_global_folder_async: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

### Return type

[**BeginAsyncJobResponse**](BeginAsyncJobResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An asynchronous job to get a list of all content items been scheduled. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_folder_async_result**
> ContentList get_global_folder_async_result(job_id)

Get Global View job result

Get result of a Global View job for the given job identifier. The result will be a list of all content items that a user has permissions to view in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import folder_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.content_list import ContentList
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
    api_instance = folder_management_api.FolderManagementApi(api_client)
    job_id = "jobId_example" # str | The identifier of the asynchronous Global View job.

    # example passing only required values which don't have defaults set
    try:
        # Get Global View job result
        api_response = api_instance.get_global_folder_async_result(job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->get_global_folder_async_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The identifier of the asynchronous Global View job. |

### Return type

[**ContentList**](ContentList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all content items with view permission. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_folder_async_status**
> AsyncJobStatus get_global_folder_async_status(job_id)

Get Global View job status

Get the status of an asynchronous Global View job for the given job identifier. If job succeeds, use [Global View Result](#operation/getGlobalFolderAsyncResult) endpoint to fetch all content items that you have permissions to view.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import folder_management_api
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
    api_instance = folder_management_api.FolderManagementApi(api_client)
    job_id = "jobId_example" # str | The identifier of the asynchronous Global View job.

    # example passing only required values which don't have defaults set
    try:
        # Get Global View job status
        api_response = api_instance.get_global_folder_async_status(job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->get_global_folder_async_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The identifier of the asynchronous Global View job. |

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
**200** | Asynchronous Global View job status. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_folder**
> Folder get_personal_folder()

Get personal folder.

Get the personal folder of the current user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import folder_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.folder import Folder
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
    api_instance = folder_management_api.FolderManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get personal folder.
        api_response = api_instance.get_personal_folder()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->get_personal_folder: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Folder**](Folder.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The personal folder of the current user.  |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder**
> Folder update_folder(id, update_folder_request)

Update a folder.

Update an existing folder with the given identifier. Set the header parameter `isAdminMode` to `\"true\"` if updating a folder inside \"Admin Recommended\" folder.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import folder_management_api
from sumologic_client.model.update_folder_request import UpdateFolderRequest
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.folder import Folder
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
    api_instance = folder_management_api.FolderManagementApi(api_client)
    id = "id_example" # str | Identifier of the folder to update.
    update_folder_request = UpdateFolderRequest(
        name="SampleFolder",
        description="This is a sample folder.",
    ) # UpdateFolderRequest | Information to update about the folder.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a folder.
        api_response = api_instance.update_folder(id, update_folder_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->update_folder: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a folder.
        api_response = api_instance.update_folder(id, update_folder_request, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FolderManagementApi->update_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the folder to update. |
 **update_folder_request** | [**UpdateFolderRequest**](UpdateFolderRequest.md)| Information to update about the folder. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

### Return type

[**Folder**](Folder.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The folder was successfully updated. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


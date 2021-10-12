# sumologic_client.ContentManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**async_copy_status**](ContentManagementApi.md#async_copy_status) | **GET** /v2/content/{id}/copy/{jobId}/status | Content copy job status.
[**begin_async_copy**](ContentManagementApi.md#begin_async_copy) | **POST** /v2/content/{id}/copy | Start a content copy job.
[**begin_async_delete**](ContentManagementApi.md#begin_async_delete) | **DELETE** /v2/content/{id}/delete | Start a content deletion job.
[**begin_async_export**](ContentManagementApi.md#begin_async_export) | **POST** /v2/content/{id}/export | Start a content export job.
[**begin_async_import**](ContentManagementApi.md#begin_async_import) | **POST** /v2/content/folders/{folderId}/import | Start a content import job.
[**get_async_delete_status**](ContentManagementApi.md#get_async_delete_status) | **GET** /v2/content/{id}/delete/{jobId}/status | Content deletion job status.
[**get_async_export_result**](ContentManagementApi.md#get_async_export_result) | **GET** /v2/content/{contentId}/export/{jobId}/result | Content export job result.
[**get_async_export_status**](ContentManagementApi.md#get_async_export_status) | **GET** /v2/content/{contentId}/export/{jobId}/status | Content export job status.
[**get_async_import_status**](ContentManagementApi.md#get_async_import_status) | **GET** /v2/content/folders/{folderId}/import/{jobId}/status | Content import job status.
[**get_item_by_path**](ContentManagementApi.md#get_item_by_path) | **GET** /v2/content/path | Get content item by path.
[**get_path_by_id**](ContentManagementApi.md#get_path_by_id) | **GET** /v2/content/{contentId}/path | Get path of an item.
[**move_item**](ContentManagementApi.md#move_item) | **POST** /v2/content/{id}/move | Move an item.


# **async_copy_status**
> AsyncJobStatus async_copy_status(id, job_id)

Content copy job status.

Get the status of the copy request with the given job identifier. On success, field `statusMessage` will contain identifier of the newly copied content in format: `id: {hexIdentifier}`. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    id = "id_example" # str | The identifier of the content which was copied.
    job_id = "jobId_example" # str | The identifier of the asynchronous copy request job.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Content copy job status.
        api_response = api_instance.async_copy_status(id, job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->async_copy_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Content copy job status.
        api_response = api_instance.async_copy_status(id, job_id, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->async_copy_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the content which was copied. |
 **job_id** | **str**| The identifier of the asynchronous copy request job. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

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
**200** | The status of the content copy job. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_async_copy**
> BeginAsyncJobResponse begin_async_copy(id, destination_folder)

Start a content copy job.

Start an asynchronous content copy job with the given identifier to the destination folder. If the content item is a folder, everything under the folder is copied recursively.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    id = "id_example" # str | The identifier of the content item to copy. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format.
    destination_folder = "destinationFolder_example" # str | The identifier of the destination folder.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start a content copy job.
        api_response = api_instance.begin_async_copy(id, destination_folder)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->begin_async_copy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start a content copy job.
        api_response = api_instance.begin_async_copy(id, destination_folder, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->begin_async_copy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the content item to copy. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. |
 **destination_folder** | **str**| The identifier of the destination folder. |
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
**200** | Content copy job has been scheduled. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_async_delete**
> BeginAsyncJobResponse begin_async_delete(id)

Start a content deletion job.

Start an asynchronous content deletion job with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    id = "id_example" # str | Identifier of the content to delete. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start a content deletion job.
        api_response = api_instance.begin_async_delete(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->begin_async_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start a content deletion job.
        api_response = api_instance.begin_async_delete(id, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->begin_async_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the content to delete. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. |
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
**200** | Deletion job has been scheduled. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_async_export**
> BeginAsyncJobResponse begin_async_export(id)

Start a content export job.

Schedule an _asynchronous_ export of content with the given identifier. You will get back an asynchronous job identifier on success. Use the [getAsyncExportStatus](#operation/getAsyncExportStatus) endpoint and the job identifier you got back in the response to track the status of an asynchronous export job. If the content item is a folder, everything under the folder is exported recursively. Keep in mind when exporting large folders that there is a limit of 1000 content objects that can be exported at once. If you want to import more than 1000 content objects, then be sure to split the import into batches of 1000 objects or less. The results from the export are compatible with the Library import feature in the Sumo Logic user interface as well as the API content import job.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    id = "id_example" # str | The identifier of the content item to export. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start a content export job.
        api_response = api_instance.begin_async_export(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->begin_async_export: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start a content export job.
        api_response = api_instance.begin_async_export(id, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->begin_async_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the content item to export. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. |
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
**200** | Export job has been scheduled. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_async_import**
> BeginAsyncJobResponse begin_async_import(folder_id, content_sync_definition)

Start a content import job.

Schedule an asynchronous import of content inside an existing folder with the given identifier. Import requests can be used to create or update content within a folder. Content items need to have a unique name within their folder. If there is already a content item with the same name in the folder, you can set the `overwrite` parameter to `true` to overwrite existing content items. By default, the `overwrite` parameter is set to `false`, where the import will fail if a content item with the same name already exist. Keep in mind when importing large folders that there is a limit of 1000 content objects that can be imported at once. If you want to import more than 1000 content objects, then be sure to split the import into batches of 1000 objects or less.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.content_sync_definition import ContentSyncDefinition
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    folder_id = "folderId_example" # str | The identifier of the folder to import into. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format.
    content_sync_definition = ContentSyncDefinition() # ContentSyncDefinition | The content to import.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)
    overwrite = False # bool | Set this to \"true\" to overwrite a content item if the name already exists. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Start a content import job.
        api_response = api_instance.begin_async_import(folder_id, content_sync_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->begin_async_import: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start a content import job.
        api_response = api_instance.begin_async_import(folder_id, content_sync_definition, is_admin_mode=is_admin_mode, overwrite=overwrite)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->begin_async_import: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| The identifier of the folder to import into. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. |
 **content_sync_definition** | [**ContentSyncDefinition**](ContentSyncDefinition.md)| The content to import. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]
 **overwrite** | **bool**| Set this to \&quot;true\&quot; to overwrite a content item if the name already exists. | [optional] if omitted the server will use the default value of False

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
**200** | Import job has been scheduled. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_delete_status**
> AsyncJobStatus get_async_delete_status(id, job_id)

Content deletion job status.

Get the status of an asynchronous content deletion job request for the given job identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    id = "id_example" # str | Identifier of the content to delete.
    job_id = "jobId_example" # str | The identifier of the asynchronous job.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Content deletion job status.
        api_response = api_instance.get_async_delete_status(id, job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->get_async_delete_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Content deletion job status.
        api_response = api_instance.get_async_delete_status(id, job_id, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->get_async_delete_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the content to delete. |
 **job_id** | **str**| The identifier of the asynchronous job. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

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
**200** | The status of the content deletion job. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_export_result**
> ContentSyncDefinition get_async_export_result(content_id, job_id)

Content export job result.

Get results from content export job for the given job identifier. The results from this export are incompatible with the Library import feature in the Sumo user interface.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.content_sync_definition import ContentSyncDefinition
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    content_id = "contentId_example" # str | The identifier of the exported content item.
    job_id = "jobId_example" # str | The identifier of the asynchronous job.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Content export job result.
        api_response = api_instance.get_async_export_result(content_id, job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->get_async_export_result: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Content export job result.
        api_response = api_instance.get_async_export_result(content_id, job_id, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->get_async_export_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **str**| The identifier of the exported content item. |
 **job_id** | **str**| The identifier of the asynchronous job. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

### Return type

[**ContentSyncDefinition**](ContentSyncDefinition.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of export job. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_export_status**
> AsyncJobStatus get_async_export_status(content_id, job_id)

Content export job status.

Get the status of an asynchronous content export request for the given job identifier. On success, use the [getExportResult](#operation/getAsyncExportResult) endpoint to get the result of the export job.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    content_id = "contentId_example" # str | The identifier of the exported content item.
    job_id = "jobId_example" # str | The identifier of the asynchronous export job.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Content export job status.
        api_response = api_instance.get_async_export_status(content_id, job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->get_async_export_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Content export job status.
        api_response = api_instance.get_async_export_status(content_id, job_id, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->get_async_export_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **str**| The identifier of the exported content item. |
 **job_id** | **str**| The identifier of the asynchronous export job. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

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
**200** | The status of the export job. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_import_status**
> AsyncJobStatus get_async_import_status(folder_id, job_id)

Content import job status.

Get the status of a content import job for the given job identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    folder_id = "folderId_example" # str | The identifier of the folder to import into.
    job_id = "jobId_example" # str | The identifier of the import request.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Content import job status.
        api_response = api_instance.get_async_import_status(folder_id, job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->get_async_import_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Content import job status.
        api_response = api_instance.get_async_import_status(folder_id, job_id, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->get_async_import_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| The identifier of the folder to import into. |
 **job_id** | **str**| The identifier of the import request. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

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
**200** | The status of the import job. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_by_path**
> Content get_item_by_path(path)

Get content item by path.

Get a content item corresponding to the given path.  _Path is specified in the required query parameter `path`. The path should be URL encoded._ For example, to get \"Acme Corp\" folder of a user \"user@sumo.com\" you can use the following curl command:   ```bash   curl https://api.sumologic.com/api/v2/content/path?path=/Library/Users/user%40sumo.com/Acme%20Corp   ```   The absolute path to a content item should be specified to get the item. The content library has \"Library\" folder at the root level. For items in \"Personal\" folder, the base path is \"/Library/Users/user@sumo.com\" where \"user@sumo.com\" is the email address of the user. For example if a user with email address `wile@acme.com` has `Rockets` folder inside Personal folder, the path of Rockets folder will be `/Library/Users/wile@acme.com/Rockets`.  For items in \"Admin Recommended\" folder, the base path is \"/Library/Admin Recommended\". For example, given a folder `Acme` in Admin Recommended folder, the path will be `/Library/Admin Recommended/Acme`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
from sumologic_client.model.content import Content
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    path = "/Library/Users/user@sumo.com/SampleFolder" # str | Path of the content item to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Get content item by path.
        api_response = api_instance.get_item_by_path(path)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->get_item_by_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path of the content item to retrieve. |

### Return type

[**Content**](Content.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content item corresponding to the given path. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_path_by_id**
> ContentPath get_path_by_id(content_id)

Get path of an item.

Get full path of a content item with the given identifier. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.content_path import ContentPath
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    content_id = "contentId_example" # str | Identifier of the content item to get the path.

    # example passing only required values which don't have defaults set
    try:
        # Get path of an item.
        api_response = api_instance.get_path_by_id(content_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->get_path_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **str**| Identifier of the content item to get the path. |

### Return type

[**ContentPath**](ContentPath.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Full path of the content item. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_item**
> move_item(destination_folder_id, id)

Move an item.

Moves an item from its current location to another folder. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_management_api
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
    api_instance = content_management_api.ContentManagementApi(api_client)
    destination_folder_id = "destinationFolderId_example" # str | Identifier of the destination folder.
    id = "id_example" # str | Identifier of the item the user wants to move.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Move an item.
        api_instance.move_item(destination_folder_id, id)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->move_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Move an item.
        api_instance.move_item(destination_folder_id, id, is_admin_mode=is_admin_mode)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentManagementApi->move_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_folder_id** | **str**| Identifier of the destination folder. |
 **id** | **str**| Identifier of the item the user wants to move. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

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
**200** | Content was moved successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


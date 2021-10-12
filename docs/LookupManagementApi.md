# sumologic_client.LookupManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_table**](LookupManagementApi.md#create_table) | **POST** /v1/lookupTables | Create a lookup table.
[**delete_table**](LookupManagementApi.md#delete_table) | **DELETE** /v1/lookupTables/{id} | Delete a lookup table.
[**delete_table_row**](LookupManagementApi.md#delete_table_row) | **PUT** /v1/lookupTables/{id}/deleteTableRow | Delete a lookup table row.
[**lookup_table_by_id**](LookupManagementApi.md#lookup_table_by_id) | **GET** /v1/lookupTables/{id} | Get a lookup table.
[**request_job_status**](LookupManagementApi.md#request_job_status) | **GET** /v1/lookupTables/jobs/{jobId}/status | Get the status of an async job.
[**truncate_table**](LookupManagementApi.md#truncate_table) | **POST** /v1/lookupTables/{id}/truncate | Empty a lookup table.
[**update_table**](LookupManagementApi.md#update_table) | **PUT** /v1/lookupTables/{id} | Edit a lookup table.
[**update_table_row**](LookupManagementApi.md#update_table_row) | **PUT** /v1/lookupTables/{id}/row | Insert or Update a lookup table row.
[**upload_file**](LookupManagementApi.md#upload_file) | **POST** /v1/lookupTables/{id}/upload | Upload a CSV file.


# **create_table**
> LookupTable create_table(lookup_table_definition)

Create a lookup table.

Create a new lookup table by providing a schema and specifying its configuration. Providing parentFolderId  is mandatory. Use the [getItemByPath](#operation/getItemByPath) endpoint to get content id of a path. Please check [Content management API](#tag/contentManagement) and [Folder management API](#tag/folderManagement) for all available options.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import lookup_management_api
from sumologic_client.model.lookup_table_definition import LookupTableDefinition
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.lookup_table import LookupTable
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
    api_instance = lookup_management_api.LookupManagementApi(api_client)
    lookup_table_definition = LookupTableDefinition() # LookupTableDefinition | The schema and configuration for the lookup table.

    # example passing only required values which don't have defaults set
    try:
        # Create a lookup table.
        api_response = api_instance.create_table(lookup_table_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling LookupManagementApi->create_table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_table_definition** | [**LookupTableDefinition**](LookupTableDefinition.md)| The schema and configuration for the lookup table. |

### Return type

[**LookupTable**](LookupTable.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lookup table created successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table**
> delete_table(id)

Delete a lookup table.

Delete a lookup table completely.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import lookup_management_api
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
    api_instance = lookup_management_api.LookupManagementApi(api_client)
    id = "0000000001C41EE4" # str | Identifier of the lookup table.

    # example passing only required values which don't have defaults set
    try:
        # Delete a lookup table.
        api_instance.delete_table(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling LookupManagementApi->delete_table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the lookup table. |

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
**204** | Deletion successful. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table_row**
> delete_table_row(id, row_delete_definition)

Delete a lookup table row.

Delete a row from lookup table by giving primary key. The complete set of primary key fields of the lookup table should be provided.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import lookup_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.row_delete_definition import RowDeleteDefinition
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
    api_instance = lookup_management_api.LookupManagementApi(api_client)
    id = "0000000001C41EE4" # str | Identifier of the lookup table.
    row_delete_definition = RowDeleteDefinition(
        primary_key=[
            TableRow(
                column_name="user_id",
                column_value="user1",
            ),
        ],
    ) # RowDeleteDefinition | Lookup table row delete definition.

    # example passing only required values which don't have defaults set
    try:
        # Delete a lookup table row.
        api_instance.delete_table_row(id, row_delete_definition)
    except sumologic_client.ApiException as e:
        print("Exception when calling LookupManagementApi->delete_table_row: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the lookup table. |
 **row_delete_definition** | [**RowDeleteDefinition**](RowDeleteDefinition.md)| Lookup table row delete definition. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Row deleted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_table_by_id**
> LookupTable lookup_table_by_id(id)

Get a lookup table.

Get a lookup table for the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import lookup_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.lookup_table import LookupTable
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
    api_instance = lookup_management_api.LookupManagementApi(api_client)
    id = "0000000001C41EE4" # str | Identifier of the lookup table.

    # example passing only required values which don't have defaults set
    try:
        # Get a lookup table.
        api_response = api_instance.lookup_table_by_id(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling LookupManagementApi->lookup_table_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the lookup table. |

### Return type

[**LookupTable**](LookupTable.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Definition of the lookup table. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_job_status**
> LookupAsyncJobStatus request_job_status(job_id)

Get the status of an async job.

Retrieve the status of a previously made request. If the request was successful, the status of the response object will be `Success`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import lookup_management_api
from sumologic_client.model.lookup_async_job_status import LookupAsyncJobStatus
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
    api_instance = lookup_management_api.LookupManagementApi(api_client)
    job_id = "0000000001C41AA3" # str | An identifier returned in response to an asynchronous request.

    # example passing only required values which don't have defaults set
    try:
        # Get the status of an async job.
        api_response = api_instance.request_job_status(job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling LookupManagementApi->request_job_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| An identifier returned in response to an asynchronous request. |

### Return type

[**LookupAsyncJobStatus**](LookupAsyncJobStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of async job with given identifier. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **truncate_table**
> LookupRequestToken truncate_table(id)

Empty a lookup table.

Delete all data from a lookup table.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import lookup_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.lookup_request_token import LookupRequestToken
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
    api_instance = lookup_management_api.LookupManagementApi(api_client)
    id = "0000000001C41EE4" # str | Identifier of the table to clear.

    # example passing only required values which don't have defaults set
    try:
        # Empty a lookup table.
        api_response = api_instance.truncate_table(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling LookupManagementApi->truncate_table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the table to clear. |

### Return type

[**LookupRequestToken**](LookupRequestToken.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The delete data request was accepted. Use the provided token in a status request to track the status of the delete. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table**
> LookupTable update_table(id, lookup_update_definition)

Edit a lookup table.

Edit the lookup table data. All the fields are mandatory in the request.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import lookup_management_api
from sumologic_client.model.lookup_update_definition import LookupUpdateDefinition
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.lookup_table import LookupTable
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
    api_instance = lookup_management_api.LookupManagementApi(api_client)
    id = "0000000001C41EE4" # str | Identifier of the lookup table.
    lookup_update_definition = LookupUpdateDefinition(
        ttl=100,
        description="This is a sample lookup table description.",
        size_limit_action="DeleteOldData",
    ) # LookupUpdateDefinition | The configuration changes for the lookup table.

    # example passing only required values which don't have defaults set
    try:
        # Edit a lookup table.
        api_response = api_instance.update_table(id, lookup_update_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling LookupManagementApi->update_table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the lookup table. |
 **lookup_update_definition** | [**LookupUpdateDefinition**](LookupUpdateDefinition.md)| The configuration changes for the lookup table. |

### Return type

[**LookupTable**](LookupTable.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration updated successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_row**
> update_table_row(id, row_update_definition)

Insert or Update a lookup table row.

Insert or update a row of a lookup table with the given identifier. A new row is inserted if the primary key does not exist already, otherwise the existing row with the specified primary key is updated. All the fields of the lookup table are required and will be updated to the given values. In case a field is not specified then it will be assumed to be set to null. If the table size exceeds the maximum limit of 100MB then based on the size limit action of the table the update will be processed or discarded.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import lookup_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.row_update_definition import RowUpdateDefinition
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
    api_instance = lookup_management_api.LookupManagementApi(api_client)
    id = "0000000001C41EE4" # str | Identifier of the lookup table.
    row_update_definition = RowUpdateDefinition(
        row=[
            TableRow(
                column_name="user_id",
                column_value="user1",
            ),
        ],
    ) # RowUpdateDefinition | Lookup table row update definition.

    # example passing only required values which don't have defaults set
    try:
        # Insert or Update a lookup table row.
        api_instance.update_table_row(id, row_update_definition)
    except sumologic_client.ApiException as e:
        print("Exception when calling LookupManagementApi->update_table_row: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the lookup table. |
 **row_update_definition** | [**RowUpdateDefinition**](RowUpdateDefinition.md)| Lookup table row update definition. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Row updated successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> LookupRequestToken upload_file(id, file)

Upload a CSV file.

Create a request to populate a lookup table with a CSV file.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import lookup_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.lookup_request_token import LookupRequestToken
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
    api_instance = lookup_management_api.LookupManagementApi(api_client)
    id = "0000000001C41EE4" # str | Identifier of the lookup table to populate.
    file = open('/path/to/file', 'rb') # file_type | The CSV file to upload.   - The size limit for the CSV file is 100MB.   - Use Unix format, with newlines (\\\"\\\\n\\\") separating rows.   - The first row should contain headers that match the lookup table schema. Matching is     case-insensitive.
    merge = True # bool | This indicates whether the file contents will be merged with existing data in the lookup table or not. If this is true then data with the same primary keys will be updated while the rest of the rows will be appended. By default, merge is false. The response includes a request identifier that you need to use in the [Request Status API](#operation/requestStatus) to track the status of the upload request. (optional) if omitted the server will use the default value of False
    file_encoding = "UTF-16" # str | File encoding of file being uploaded. (optional) if omitted the server will use the default value of "UTF-8"

    # example passing only required values which don't have defaults set
    try:
        # Upload a CSV file.
        api_response = api_instance.upload_file(id, file)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling LookupManagementApi->upload_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a CSV file.
        api_response = api_instance.upload_file(id, file, merge=merge, file_encoding=file_encoding)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling LookupManagementApi->upload_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the lookup table to populate. |
 **file** | **file_type**| The CSV file to upload.   - The size limit for the CSV file is 100MB.   - Use Unix format, with newlines (\\\&quot;\\\\n\\\&quot;) separating rows.   - The first row should contain headers that match the lookup table schema. Matching is     case-insensitive. |
 **merge** | **bool**| This indicates whether the file contents will be merged with existing data in the lookup table or not. If this is true then data with the same primary keys will be updated while the rest of the rows will be appended. By default, merge is false. The response includes a request identifier that you need to use in the [Request Status API](#operation/requestStatus) to track the status of the upload request. | [optional] if omitted the server will use the default value of False
 **file_encoding** | **str**| File encoding of file being uploaded. | [optional] if omitted the server will use the default value of "UTF-8"

### Return type

[**LookupRequestToken**](LookupRequestToken.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upload request was accepted. Use the provided token in a status request to track the status of the upload. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


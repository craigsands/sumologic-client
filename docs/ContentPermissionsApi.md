# sumologic_client.ContentPermissionsApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_content_permissions**](ContentPermissionsApi.md#add_content_permissions) | **PUT** /v2/content/{id}/permissions/add | Add permissions to a content item.
[**get_content_permissions**](ContentPermissionsApi.md#get_content_permissions) | **GET** /v2/content/{id}/permissions | Get permissions of a content item
[**remove_content_permissions**](ContentPermissionsApi.md#remove_content_permissions) | **PUT** /v2/content/{id}/permissions/remove | Remove permissions from a content item.


# **add_content_permissions**
> ContentPermissionResult add_content_permissions(id, content_permission_update_request)

Add permissions to a content item.

Add permissions to a content item with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_permissions_api
from sumologic_client.model.content_permission_result import ContentPermissionResult
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.content_permission_update_request import ContentPermissionUpdateRequest
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
    api_instance = content_permissions_api.ContentPermissionsApi(api_client)
    id = "id_example" # str | The identifier of the content item.
    content_permission_update_request = ContentPermissionUpdateRequest(
        content_permission_assignments=[
            ContentPermissionAssignment(
                permission_name="Edit",
                source_type="role",
                source_id="source_id_example",
                content_id="content_id_example",
            ),
        ],
        notify_recipients=True,
        notification_message="notification_message_example",
    ) # ContentPermissionUpdateRequest | New permissions to add to the content item with the given identifier.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add permissions to a content item.
        api_response = api_instance.add_content_permissions(id, content_permission_update_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentPermissionsApi->add_content_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add permissions to a content item.
        api_response = api_instance.add_content_permissions(id, content_permission_update_request, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentPermissionsApi->add_content_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the content item. |
 **content_permission_update_request** | [**ContentPermissionUpdateRequest**](ContentPermissionUpdateRequest.md)| New permissions to add to the content item with the given identifier. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

### Return type

[**ContentPermissionResult**](ContentPermissionResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated permission object for the requested content item. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_permissions**
> ContentPermissionResult get_content_permissions(id)

Get permissions of a content item

Returns content permissions of a content item with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_permissions_api
from sumologic_client.model.content_permission_result import ContentPermissionResult
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
    api_instance = content_permissions_api.ContentPermissionsApi(api_client)
    id = "id_example" # str | The identifier of the content item.
    explicit_only = False # bool | There are two permission types: explicit and implicit. Permissions specifically assigned to the content item are explicit. Permissions derived from a parent content item, like a folder are implicit. To return only explicit permissions set this to true. (optional) if omitted the server will use the default value of False
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get permissions of a content item
        api_response = api_instance.get_content_permissions(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentPermissionsApi->get_content_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get permissions of a content item
        api_response = api_instance.get_content_permissions(id, explicit_only=explicit_only, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentPermissionsApi->get_content_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the content item. |
 **explicit_only** | **bool**| There are two permission types: explicit and implicit. Permissions specifically assigned to the content item are explicit. Permissions derived from a parent content item, like a folder are implicit. To return only explicit permissions set this to true. | [optional] if omitted the server will use the default value of False
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

### Return type

[**ContentPermissionResult**](ContentPermissionResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of permissions for the requested content item. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_content_permissions**
> ContentPermissionResult remove_content_permissions(id, content_permission_update_request)

Remove permissions from a content item.

Remove permissions from a content item with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import content_permissions_api
from sumologic_client.model.content_permission_result import ContentPermissionResult
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.content_permission_update_request import ContentPermissionUpdateRequest
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
    api_instance = content_permissions_api.ContentPermissionsApi(api_client)
    id = "id_example" # str | The identifier of the content item.
    content_permission_update_request = ContentPermissionUpdateRequest(
        content_permission_assignments=[
            ContentPermissionAssignment(
                permission_name="Edit",
                source_type="role",
                source_id="source_id_example",
                content_id="content_id_example",
            ),
        ],
        notify_recipients=True,
        notification_message="notification_message_example",
    ) # ContentPermissionUpdateRequest | Permissions to remove from a content item with the given identifier.
    is_admin_mode = "isAdminMode_example" # str | Set this to \"true\" if you want to perform the request as a Content Administrator. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove permissions from a content item.
        api_response = api_instance.remove_content_permissions(id, content_permission_update_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentPermissionsApi->remove_content_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove permissions from a content item.
        api_response = api_instance.remove_content_permissions(id, content_permission_update_request, is_admin_mode=is_admin_mode)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ContentPermissionsApi->remove_content_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the content item. |
 **content_permission_update_request** | [**ContentPermissionUpdateRequest**](ContentPermissionUpdateRequest.md)| Permissions to remove from a content item with the given identifier. |
 **is_admin_mode** | **str**| Set this to \&quot;true\&quot; if you want to perform the request as a Content Administrator. | [optional]

### Return type

[**ContentPermissionResult**](ContentPermissionResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated permissions for the requested content item. |  -  |
**0** | Operation failed with an error. Check that your request is valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# sumologic_client.AccessKeyManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_key**](AccessKeyManagementApi.md#create_access_key) | **POST** /v1/accessKeys | Create an access key.
[**delete_access_key**](AccessKeyManagementApi.md#delete_access_key) | **DELETE** /v1/accessKeys/{id} | Delete an access key.
[**list_access_keys**](AccessKeyManagementApi.md#list_access_keys) | **GET** /v1/accessKeys | List all access keys.
[**list_personal_access_keys**](AccessKeyManagementApi.md#list_personal_access_keys) | **GET** /v1/accessKeys/personal | List personal keys.
[**update_access_key**](AccessKeyManagementApi.md#update_access_key) | **PUT** /v1/accessKeys/{id} | Update an access key.


# **create_access_key**
> AccessKey create_access_key(access_key_create_request)

Create an access key.

Creates a new access ID and key pair. The new access key can be used from the domains specified in corsHeaders field. Whether Sumo Logic accepts or rejects an API request depends on whether it contains an ORIGIN header and the entries in the allowlist. Sumo Logic will reject:   1. Requests with an ORIGIN header but the allowlist is empty.   2. Requests with an ORIGIN header that don't match any entry in the allowlist.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import access_key_management_api
from sumologic_client.model.access_key import AccessKey
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.access_key_create_request import AccessKeyCreateRequest
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
    api_instance = access_key_management_api.AccessKeyManagementApi(api_client)
    access_key_create_request = AccessKeyCreateRequest(
        label="automation access key",
        cors_headers=["https://my-app.com","https://mail.my-app.com"],
    ) # AccessKeyCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an access key.
        api_response = api_instance.create_access_key(access_key_create_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AccessKeyManagementApi->create_access_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key_create_request** | [**AccessKeyCreateRequest**](AccessKeyCreateRequest.md)|  |

### Return type

[**AccessKey**](AccessKey.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access key created successfully. |  -  |
**0** | Access key creation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_key**
> delete_access_key(id)

Delete an access key.

Deletes the access key with the given accessId.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import access_key_management_api
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
    api_instance = access_key_management_api.AccessKeyManagementApi(api_client)
    id = "id_example" # str | The accessId of the access key to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete an access key.
        api_instance.delete_access_key(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling AccessKeyManagementApi->delete_access_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The accessId of the access key to delete. |

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
**204** | Access key deletion completed successfully. |  -  |
**0** | Access key deletion failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_keys**
> PaginatedListAccessKeysResult list_access_keys()

List all access keys.

List all access keys in your account.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import access_key_management_api
from sumologic_client.model.paginated_list_access_keys_result import PaginatedListAccessKeysResult
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
    api_instance = access_key_management_api.AccessKeyManagementApi(api_client)
    limit = 100 # int | Limit the number of access keys returned in the response. The number of access keys returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. `token` is set to null when no more pages are left. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all access keys.
        api_response = api_instance.list_access_keys(limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AccessKeyManagementApi->list_access_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of access keys returned in the response. The number of access keys returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. &#x60;token&#x60; is set to null when no more pages are left. | [optional]

### Return type

[**PaginatedListAccessKeysResult**](PaginatedListAccessKeysResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all access keys in your account. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_personal_access_keys**
> ListAccessKeysResult list_personal_access_keys()

List personal keys.

List all access keys that belong to your user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import access_key_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_access_keys_result import ListAccessKeysResult
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
    api_instance = access_key_management_api.AccessKeyManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List personal keys.
        api_response = api_instance.list_personal_access_keys()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AccessKeyManagementApi->list_personal_access_keys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAccessKeysResult**](ListAccessKeysResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all access keys that belong to the user making the request. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_key**
> AccessKeyPublic update_access_key(id, access_key_update_request)

Update an access key.

Updates the properties of existing accessKey by accessId. It can be used to enable or disable the access key and to update the corsHeaders list.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import access_key_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.access_key_public import AccessKeyPublic
from sumologic_client.model.access_key_update_request import AccessKeyUpdateRequest
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
    api_instance = access_key_management_api.AccessKeyManagementApi(api_client)
    id = "id_example" # str | The accessId of the access key to update.
    access_key_update_request = AccessKeyUpdateRequest(
        disabled=True,
        cors_headers=["https://my-app.com","https://mail.my-app.com"],
    ) # AccessKeyUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update an access key.
        api_response = api_instance.update_access_key(id, access_key_update_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AccessKeyManagementApi->update_access_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The accessId of the access key to update. |
 **access_key_update_request** | [**AccessKeyUpdateRequest**](AccessKeyUpdateRequest.md)|  |

### Return type

[**AccessKeyPublic**](AccessKeyPublic.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access key updated successfully. |  -  |
**0** | Access key update failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


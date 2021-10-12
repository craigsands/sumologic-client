# sumologic_client.TokensLibraryManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](TokensLibraryManagementApi.md#create_token) | **POST** /v1/tokens | Create a token.
[**delete_token**](TokensLibraryManagementApi.md#delete_token) | **DELETE** /v1/tokens/{id} | Delete a token.
[**get_token**](TokensLibraryManagementApi.md#get_token) | **GET** /v1/tokens/{id} | Get a token.
[**list_tokens**](TokensLibraryManagementApi.md#list_tokens) | **GET** /v1/tokens | Get a list of tokens.
[**update_token**](TokensLibraryManagementApi.md#update_token) | **PUT** /v1/tokens/{id} | Update a token.


# **create_token**
> TokenBaseResponse create_token(token_base_definition)

Create a token.

Create a token in the token library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import tokens_library_management_api
from sumologic_client.model.token_base_response import TokenBaseResponse
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.token_base_definition import TokenBaseDefinition
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
    api_instance = tokens_library_management_api.TokensLibraryManagementApi(api_client)
    token_base_definition = TokenBaseDefinition(
        name="token-name",
        description="token description: for test.",
        status="Active",
        type="CollectorRegistration",
    ) # TokenBaseDefinition | Information about the token to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a token.
        api_response = api_instance.create_token(token_base_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling TokensLibraryManagementApi->create_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_base_definition** | [**TokenBaseDefinition**](TokenBaseDefinition.md)| Information about the token to create. |

### Return type

[**TokenBaseResponse**](TokenBaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token has been created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> delete_token(id)

Delete a token.

Delete a token with the given identifier in the token library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import tokens_library_management_api
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
    api_instance = tokens_library_management_api.TokensLibraryManagementApi(api_client)
    id = "id_example" # str | Identifier of the token to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a token.
        api_instance.delete_token(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling TokensLibraryManagementApi->delete_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the token to delete. |

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
**204** | The token was deleted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> TokenBaseResponse get_token(id)

Get a token.

Get a token with the given identifier in the token library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import tokens_library_management_api
from sumologic_client.model.token_base_response import TokenBaseResponse
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
    api_instance = tokens_library_management_api.TokensLibraryManagementApi(api_client)
    id = "id_example" # str | Identifier of the token to return.

    # example passing only required values which don't have defaults set
    try:
        # Get a token.
        api_response = api_instance.get_token(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling TokensLibraryManagementApi->get_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the token to return. |

### Return type

[**TokenBaseResponse**](TokenBaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token object that was requested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tokens**
> ListTokensBaseResponse list_tokens()

Get a list of tokens.

Get a list of all tokens in the token library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import tokens_library_management_api
from sumologic_client.model.list_tokens_base_response import ListTokensBaseResponse
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
    api_instance = tokens_library_management_api.TokensLibraryManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of tokens.
        api_response = api_instance.list_tokens()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling TokensLibraryManagementApi->list_tokens: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListTokensBaseResponse**](ListTokensBaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of tokens. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token**
> TokenBaseResponse update_token(id, token_base_definition_update)

Update a token.

Update a token with the given identifier in the token library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import tokens_library_management_api
from sumologic_client.model.token_base_response import TokenBaseResponse
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.token_base_definition_update import TokenBaseDefinitionUpdate
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
    api_instance = tokens_library_management_api.TokensLibraryManagementApi(api_client)
    id = "id_example" # str | Identifier of the token to update.
    token_base_definition_update = TokenBaseDefinitionUpdate(
        name="token-name",
        description="token description: for test.",
        status="Active",
        type="CollectorRegistration",
        version=1,
    ) # TokenBaseDefinitionUpdate | The token to update.

    # example passing only required values which don't have defaults set
    try:
        # Update a token.
        api_response = api_instance.update_token(id, token_base_definition_update)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling TokensLibraryManagementApi->update_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the token to update. |
 **token_base_definition_update** | [**TokenBaseDefinitionUpdate**](TokenBaseDefinitionUpdate.md)| The token to update. |

### Return type

[**TokenBaseResponse**](TokenBaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token was successfully modified. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


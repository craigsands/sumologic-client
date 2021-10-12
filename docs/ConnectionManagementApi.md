# sumologic_client.ConnectionManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection**](ConnectionManagementApi.md#create_connection) | **POST** /v1/connections | Create a new connection.
[**delete_connection**](ConnectionManagementApi.md#delete_connection) | **DELETE** /v1/connections/{id} | Delete a connection.
[**get_connection**](ConnectionManagementApi.md#get_connection) | **GET** /v1/connections/{id} | Get a connection.
[**list_connections**](ConnectionManagementApi.md#list_connections) | **GET** /v1/connections | Get a list of connections.
[**test_connection**](ConnectionManagementApi.md#test_connection) | **POST** /v1/connections/test | Test a new connection url.
[**update_connection**](ConnectionManagementApi.md#update_connection) | **PUT** /v1/connections/{id} | Update a connection.


# **create_connection**
> Connection create_connection(connection_definition)

Create a new connection.

Create a new connection in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import connection_management_api
from sumologic_client.model.connection import Connection
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.connection_definition import ConnectionDefinition
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
    api_instance = connection_management_api.ConnectionManagementApi(api_client)
    connection_definition = ConnectionDefinition() # ConnectionDefinition | Information about the new connection.

    # example passing only required values which don't have defaults set
    try:
        # Create a new connection.
        api_response = api_instance.create_connection(connection_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ConnectionManagementApi->create_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_definition** | [**ConnectionDefinition**](ConnectionDefinition.md)| Information about the new connection. |

### Return type

[**Connection**](Connection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The connection has been created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> delete_connection(id, type)

Delete a connection.

Delete a connection with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import connection_management_api
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
    api_instance = connection_management_api.ConnectionManagementApi(api_client)
    id = "id_example" # str | Identifier of the connection to delete.
    type = "ServiceNowConnection" # str | Type of connection to delete. Valid values are `WebhookConnection`, `ServiceNowConnection`.

    # example passing only required values which don't have defaults set
    try:
        # Delete a connection.
        api_instance.delete_connection(id, type)
    except sumologic_client.ApiException as e:
        print("Exception when calling ConnectionManagementApi->delete_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the connection to delete. |
 **type** | **str**| Type of connection to delete. Valid values are &#x60;WebhookConnection&#x60;, &#x60;ServiceNowConnection&#x60;. |

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
**204** | Connection was deleted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection**
> Connection get_connection(id, )

Get a connection.

Get a connection with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import connection_management_api
from sumologic_client.model.connection import Connection
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
    api_instance = connection_management_api.ConnectionManagementApi(api_client)
    id = "id_example" # str | Identifier of connection to return.

    # example passing only required values which don't have defaults set
    try:
        # Get a connection.
        api_response = api_instance.get_connection(id, )
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ConnectionManagementApi->get_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of connection to return. |
 **type** | **str**| Type of connection to return. Valid values are &#x60;WebhookConnection&#x60;, &#x60;ServiceNowConnection&#x60;. | defaults to "WebhookConnection"

### Return type

[**Connection**](Connection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection object that was requested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connections**
> ListConnectionsResponse list_connections()

Get a list of connections.

Get a list of all connections in the organization. The response is paginated with a default limit of 100 connections per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import connection_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_connections_response import ListConnectionsResponse
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
    api_instance = connection_management_api.ConnectionManagementApi(api_client)
    limit = 100 # int | Limit the number of connections returned in the response. The number of connections returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. `token` is set to null when no more pages are left. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of connections.
        api_response = api_instance.list_connections(limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ConnectionManagementApi->list_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of connections returned in the response. The number of connections returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. &#x60;token&#x60; is set to null when no more pages are left. | [optional]

### Return type

[**ListConnectionsResponse**](ListConnectionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of connections in the organization. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection**
> TestConnectionResponse test_connection(connection_definition)

Test a new connection url.

Test a new connection url is valid and can connect.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import connection_management_api
from sumologic_client.model.test_connection_response import TestConnectionResponse
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.connection_definition import ConnectionDefinition
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
    api_instance = connection_management_api.ConnectionManagementApi(api_client)
    connection_definition = ConnectionDefinition() # ConnectionDefinition | Information about the new connection.

    # example passing only required values which don't have defaults set
    try:
        # Test a new connection url.
        api_response = api_instance.test_connection(connection_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ConnectionManagementApi->test_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_definition** | [**ConnectionDefinition**](ConnectionDefinition.md)| Information about the new connection. |

### Return type

[**TestConnectionResponse**](TestConnectionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The connection url has been tested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection**
> Connection update_connection(id, connection_definition)

Update a connection.

Update an existing connection.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import connection_management_api
from sumologic_client.model.connection import Connection
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.connection_definition import ConnectionDefinition
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
    api_instance = connection_management_api.ConnectionManagementApi(api_client)
    id = "id_example" # str | Identifier of the connection to update.
    connection_definition = ConnectionDefinition() # ConnectionDefinition | Information to update about the connection.

    # example passing only required values which don't have defaults set
    try:
        # Update a connection.
        api_response = api_instance.update_connection(id, connection_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ConnectionManagementApi->update_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the connection to update. |
 **connection_definition** | [**ConnectionDefinition**](ConnectionDefinition.md)| Information to update about the connection. |

### Return type

[**Connection**](Connection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The connection was successfully modified. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# sumologic_client.ServiceAllowlistManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_allowlisted_cidrs**](ServiceAllowlistManagementApi.md#add_allowlisted_cidrs) | **POST** /v1/serviceAllowlist/addresses/add | Allowlist CIDRs/IP addresses.
[**delete_allowlisted_cidrs**](ServiceAllowlistManagementApi.md#delete_allowlisted_cidrs) | **POST** /v1/serviceAllowlist/addresses/remove | Remove allowlisted CIDRs/IP addresses.
[**disable_allowlisting**](ServiceAllowlistManagementApi.md#disable_allowlisting) | **POST** /v1/serviceAllowlist/disable | Disable service allowlisting.
[**enable_allowlisting**](ServiceAllowlistManagementApi.md#enable_allowlisting) | **POST** /v1/serviceAllowlist/enable | Enable service allowlisting.
[**get_allowlisting_status**](ServiceAllowlistManagementApi.md#get_allowlisting_status) | **GET** /v1/serviceAllowlist/status | Get the allowlisting status.
[**list_allowlisted_cidrs**](ServiceAllowlistManagementApi.md#list_allowlisted_cidrs) | **GET** /v1/serviceAllowlist/addresses | List all allowlisted CIDRs/IP addresses.


# **add_allowlisted_cidrs**
> CidrList add_allowlisted_cidrs(cidr_list)

Allowlist CIDRs/IP addresses.

Add CIDR notations and/or IP addresses to the allowlist of the organization if not already there. When service allowlisting functionality is enabled, CIDRs/IP addresses that are allowlisted will have access to Sumo Logic and/or content sharing.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import service_allowlist_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.cidr_list import CidrList
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
    api_instance = service_allowlist_management_api.ServiceAllowlistManagementApi(api_client)
    cidr_list = CidrList(
        data=[
            Cidr(
                cidr="192.35.24.1",
                description="Accountant",
            ),
        ],
    ) # CidrList | List of all CIDR notations and/or IP addresses to be added to the allowlist of the organization.

    # example passing only required values which don't have defaults set
    try:
        # Allowlist CIDRs/IP addresses.
        api_response = api_instance.add_allowlisted_cidrs(cidr_list)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ServiceAllowlistManagementApi->add_allowlisted_cidrs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cidr_list** | [**CidrList**](CidrList.md)| List of all CIDR notations and/or IP addresses to be added to the allowlist of the organization. |

### Return type

[**CidrList**](CidrList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all allowlisted CIDR notations and/or IP addresses for the organization. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_allowlisted_cidrs**
> CidrList delete_allowlisted_cidrs(cidr_list)

Remove allowlisted CIDRs/IP addresses.

Remove allowlisted CIDR notations and/or IP addresses from the organization. Removed CIDRs/IPs will immediately lose access to Sumo Logic and content sharing.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import service_allowlist_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.cidr_list import CidrList
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
    api_instance = service_allowlist_management_api.ServiceAllowlistManagementApi(api_client)
    cidr_list = CidrList(
        data=[
            Cidr(
                cidr="192.35.24.1",
                description="Accountant",
            ),
        ],
    ) # CidrList | List of all CIDR notations and/or IP addresses to be removed from the allowlist of the organization.

    # example passing only required values which don't have defaults set
    try:
        # Remove allowlisted CIDRs/IP addresses.
        api_response = api_instance.delete_allowlisted_cidrs(cidr_list)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ServiceAllowlistManagementApi->delete_allowlisted_cidrs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cidr_list** | [**CidrList**](CidrList.md)| List of all CIDR notations and/or IP addresses to be removed from the allowlist of the organization. |

### Return type

[**CidrList**](CidrList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all allowlisted CIDR notations and/or IP addresses for the organization. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_allowlisting**
> disable_allowlisting(allowlist_type)

Disable service allowlisting.

Disable service allowlisting functionality for login/API authentication or content sharing for the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import service_allowlist_management_api
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
    api_instance = service_allowlist_management_api.ServiceAllowlistManagementApi(api_client)
    allowlist_type = "Login" # str | The type of allowlisting to be disabled. It can be one of: `Login`, `Content`, or `Both`.

    # example passing only required values which don't have defaults set
    try:
        # Disable service allowlisting.
        api_instance.disable_allowlisting(allowlist_type)
    except sumologic_client.ApiException as e:
        print("Exception when calling ServiceAllowlistManagementApi->disable_allowlisting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allowlist_type** | **str**| The type of allowlisting to be disabled. It can be one of: &#x60;Login&#x60;, &#x60;Content&#x60;, or &#x60;Both&#x60;. |

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
**204** | Service allowlisting was disabled successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_allowlisting**
> enable_allowlisting(allowlist_type)

Enable service allowlisting.

Enable service allowlisting functionality for the organization. The service allowlisting can be for 1. Login: If enabled, access to Sumo Logic is granted only to CIDRs/IP addresses that are allowlisted. 2. Content: If enabled, dashboards can be shared with users connecting from CIDRs/IP addresses that are allowlisted without logging in.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import service_allowlist_management_api
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
    api_instance = service_allowlist_management_api.ServiceAllowlistManagementApi(api_client)
    allowlist_type = "Login" # str | The type of allowlisting to be enabled. It can be one of: `Login`, `Content`, or `Both`.

    # example passing only required values which don't have defaults set
    try:
        # Enable service allowlisting.
        api_instance.enable_allowlisting(allowlist_type)
    except sumologic_client.ApiException as e:
        print("Exception when calling ServiceAllowlistManagementApi->enable_allowlisting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allowlist_type** | **str**| The type of allowlisting to be enabled. It can be one of: &#x60;Login&#x60;, &#x60;Content&#x60;, or &#x60;Both&#x60;. |

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
**204** | Service allowlisting was enabled successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allowlisting_status**
> AllowlistingStatus get_allowlisting_status()

Get the allowlisting status.

Get the status of the service allowlisting functionality for login/API authentication or content sharing for the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import service_allowlist_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.allowlisting_status import AllowlistingStatus
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
    api_instance = service_allowlist_management_api.ServiceAllowlistManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the allowlisting status.
        api_response = api_instance.get_allowlisting_status()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ServiceAllowlistManagementApi->get_allowlisting_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AllowlistingStatus**](AllowlistingStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of service allowlisting for Content and Login. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_allowlisted_cidrs**
> CidrList list_allowlisted_cidrs()

List all allowlisted CIDRs/IP addresses.

Get a list of all allowlisted CIDR notations and/or IP addresses for the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import service_allowlist_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.cidr_list import CidrList
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
    api_instance = service_allowlist_management_api.ServiceAllowlistManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all allowlisted CIDRs/IP addresses.
        api_response = api_instance.list_allowlisted_cidrs()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ServiceAllowlistManagementApi->list_allowlisted_cidrs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CidrList**](CidrList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all allowlisted CIDR notations and/or IP addresses for the organization. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# sumologic_client.AccountManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subdomain**](AccountManagementApi.md#create_subdomain) | **POST** /v1/account/subdomain | Create account subdomain.
[**delete_subdomain**](AccountManagementApi.md#delete_subdomain) | **DELETE** /v1/account/subdomain | Delete the configured subdomain.
[**get_account_owner**](AccountManagementApi.md#get_account_owner) | **GET** /v1/account/accountOwner | Get the owner of an account.
[**get_status**](AccountManagementApi.md#get_status) | **GET** /v1/account/status | Get overview of the account status.
[**get_subdomain**](AccountManagementApi.md#get_subdomain) | **GET** /v1/account/subdomain | Get the configured subdomain.
[**recover_subdomains**](AccountManagementApi.md#recover_subdomains) | **POST** /v1/account/subdomain/recover | Recover subdomains for a user.
[**update_subdomain**](AccountManagementApi.md#update_subdomain) | **PUT** /v1/account/subdomain | Update account subdomain.


# **create_subdomain**
> SubdomainDefinitionResponse create_subdomain(configure_subdomain_request)

Create account subdomain.

Create a subdomain. Only the Account Owner can create a subdomain.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import account_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.subdomain_definition_response import SubdomainDefinitionResponse
from sumologic_client.model.configure_subdomain_request import ConfigureSubdomainRequest
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
    api_instance = account_management_api.AccountManagementApi(api_client)
    configure_subdomain_request = ConfigureSubdomainRequest(
        subdomain="my-company",
    ) # ConfigureSubdomainRequest | The new subdomain.

    # example passing only required values which don't have defaults set
    try:
        # Create account subdomain.
        api_response = api_instance.create_subdomain(configure_subdomain_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AccountManagementApi->create_subdomain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configure_subdomain_request** | [**ConfigureSubdomainRequest**](ConfigureSubdomainRequest.md)| The new subdomain. |

### Return type

[**SubdomainDefinitionResponse**](SubdomainDefinitionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created a new subdomain. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subdomain**
> delete_subdomain()

Delete the configured subdomain.

Delete the configured subdomain.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import account_management_api
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
    api_instance = account_management_api.AccountManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete the configured subdomain.
        api_instance.delete_subdomain()
    except sumologic_client.ApiException as e:
        print("Exception when calling AccountManagementApi->delete_subdomain: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**204** | The subdomain was successfully deleted. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_owner**
> str get_account_owner()

Get the owner of an account.

Returns the user identifier of the account owner.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import account_management_api
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
    api_instance = account_management_api.AccountManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the owner of an account.
        api_response = api_instance.get_account_owner()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AccountManagementApi->get_account_owner: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User identifier of the account owner. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> AccountStatusResponse get_status()

Get overview of the account status.

Get information related to the account's plan, pricing model, expiration and payment status.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import account_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.account_status_response import AccountStatusResponse
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
    api_instance = account_management_api.AccountManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get overview of the account status.
        api_response = api_instance.get_status()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AccountManagementApi->get_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountStatusResponse**](AccountStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Overview of the account. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subdomain**
> SubdomainDefinitionResponse get_subdomain()

Get the configured subdomain.

Get the configured subdomain.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import account_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.subdomain_definition_response import SubdomainDefinitionResponse
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
    api_instance = account_management_api.AccountManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the configured subdomain.
        api_response = api_instance.get_subdomain()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AccountManagementApi->get_subdomain: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SubdomainDefinitionResponse**](SubdomainDefinitionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subdomain&#39;s definition. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover_subdomains**
> recover_subdomains(email)

Recover subdomains for a user.

Send an email with the subdomain information for a user with the given email address.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import account_management_api
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
    api_instance = account_management_api.AccountManagementApi(api_client)
    email = "email_example" # str | Email address of the user to get subdomain information.

    # example passing only required values which don't have defaults set
    try:
        # Recover subdomains for a user.
        api_instance.recover_subdomains(email)
    except sumologic_client.ApiException as e:
        print("Exception when calling AccountManagementApi->recover_subdomains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address of the user to get subdomain information. |

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
**204** | An email containing information about associated subdomains for the given email was sent. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subdomain**
> SubdomainDefinitionResponse update_subdomain(configure_subdomain_request)

Update account subdomain.

Update a subdomain. Only the Account Owner can update the subdomain.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import account_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.subdomain_definition_response import SubdomainDefinitionResponse
from sumologic_client.model.configure_subdomain_request import ConfigureSubdomainRequest
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
    api_instance = account_management_api.AccountManagementApi(api_client)
    configure_subdomain_request = ConfigureSubdomainRequest(
        subdomain="my-company",
    ) # ConfigureSubdomainRequest | The new subdomain.

    # example passing only required values which don't have defaults set
    try:
        # Update account subdomain.
        api_response = api_instance.update_subdomain(configure_subdomain_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling AccountManagementApi->update_subdomain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configure_subdomain_request** | [**ConfigureSubdomainRequest**](ConfigureSubdomainRequest.md)| The new subdomain. |

### Return type

[**SubdomainDefinitionResponse**](SubdomainDefinitionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated subdomain&#39;s definition. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# sumologic_client.SamlConfigurationManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_allowlisted_user**](SamlConfigurationManagementApi.md#create_allowlisted_user) | **POST** /v1/saml/allowlistedUsers/{userId} | Allowlist a user.
[**create_identity_provider**](SamlConfigurationManagementApi.md#create_identity_provider) | **POST** /v1/saml/identityProviders | Create a new SAML configuration.
[**delete_allowlisted_user**](SamlConfigurationManagementApi.md#delete_allowlisted_user) | **DELETE** /v1/saml/allowlistedUsers/{userId} | Remove an allowlisted user.
[**delete_identity_provider**](SamlConfigurationManagementApi.md#delete_identity_provider) | **DELETE** /v1/saml/identityProviders/{id} | Delete a SAML configuration.
[**disable_saml_lockdown**](SamlConfigurationManagementApi.md#disable_saml_lockdown) | **POST** /v1/saml/lockdown/disable | Disable SAML lockdown.
[**enable_saml_lockdown**](SamlConfigurationManagementApi.md#enable_saml_lockdown) | **POST** /v1/saml/lockdown/enable | Require SAML for sign-in.
[**get_allowlisted_users**](SamlConfigurationManagementApi.md#get_allowlisted_users) | **GET** /v1/saml/allowlistedUsers | Get list of allowlisted users.
[**get_identity_providers**](SamlConfigurationManagementApi.md#get_identity_providers) | **GET** /v1/saml/identityProviders | Get a list of SAML configurations.
[**update_identity_provider**](SamlConfigurationManagementApi.md#update_identity_provider) | **PUT** /v1/saml/identityProviders/{id} | Update a SAML configuration.


# **create_allowlisted_user**
> AllowlistedUserResult create_allowlisted_user(user_id)

Allowlist a user.

Allowlist a user from SAML lockdown allowing them to sign in using a password in addition to SAML.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import saml_configuration_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.allowlisted_user_result import AllowlistedUserResult
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
    api_instance = saml_configuration_management_api.SamlConfigurationManagementApi(api_client)
    user_id = "userId_example" # str | Identifier of the user.

    # example passing only required values which don't have defaults set
    try:
        # Allowlist a user.
        api_response = api_instance.create_allowlisted_user(user_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling SamlConfigurationManagementApi->create_allowlisted_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Identifier of the user. |

### Return type

[**AllowlistedUserResult**](AllowlistedUserResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User was successfully allowlisted. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_identity_provider**
> SamlIdentityProvider create_identity_provider(saml_identity_provider_request)

Create a new SAML configuration.

Create a new SAML configuration in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import saml_configuration_management_api
from sumologic_client.model.saml_identity_provider import SamlIdentityProvider
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.saml_identity_provider_request import SamlIdentityProviderRequest
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
    api_instance = saml_configuration_management_api.SamlConfigurationManagementApi(api_client)
    saml_identity_provider_request = SamlIdentityProviderRequest(
        sp_initiated_login_path="http://www.okta.com/abxcseyuiwelflkdjh",
        configuration_name="SumoLogic",
        issuer="http://www.okta.com/abxcseyuiwelflkdjh",
        sp_initiated_login_enabled=False,
        authn_request_url="https://service.sumologic.com/sumo/saml/login/9483922",
        x509cert1="x509cert1_example",
        x509cert2="",
        x509cert3="",
        on_demand_provisioning_enabled=OnDemandProvisioningInfo(
            first_name_attribute="http://schemas.microsoft.com/ws/2008/06/identity/claims/givenname",
            last_name_attribute="http://schemas.microsoft.com/ws/2008/06/identity/claims/surname",
            on_demand_provisioning_roles=[
                "Analyst/Administrator",
            ],
        ),
        roles_attribute="Sumo_Role",
        logout_enabled=False,
        logout_url="https://www.sumologic.com",
        email_attribute="attribute/subject",
        debug_mode=False,
        sign_authn_request=False,
        disable_requested_authn_context=False,
        is_redirect_binding=False,
    ) # SamlIdentityProviderRequest | The configuration of the SAML identity provider.

    # example passing only required values which don't have defaults set
    try:
        # Create a new SAML configuration.
        api_response = api_instance.create_identity_provider(saml_identity_provider_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling SamlConfigurationManagementApi->create_identity_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_identity_provider_request** | [**SamlIdentityProviderRequest**](SamlIdentityProviderRequest.md)| The configuration of the SAML identity provider. |

### Return type

[**SamlIdentityProvider**](SamlIdentityProvider.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SAML configuration was successfully created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_allowlisted_user**
> delete_allowlisted_user(user_id)

Remove an allowlisted user.

Remove an allowlisted user requiring them to sign in using SAML.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import saml_configuration_management_api
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
    api_instance = saml_configuration_management_api.SamlConfigurationManagementApi(api_client)
    user_id = "userId_example" # str | Identifier of user that will no longer be allowlisted from SAML Lockdown.

    # example passing only required values which don't have defaults set
    try:
        # Remove an allowlisted user.
        api_instance.delete_allowlisted_user(user_id)
    except sumologic_client.ApiException as e:
        print("Exception when calling SamlConfigurationManagementApi->delete_allowlisted_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Identifier of user that will no longer be allowlisted from SAML Lockdown. |

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
**204** | User was successfully removed from the allowlist for SAML Lockdown. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_provider**
> delete_identity_provider(id)

Delete a SAML configuration.

Delete a SAML configuration with the given identifier from the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import saml_configuration_management_api
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
    api_instance = saml_configuration_management_api.SamlConfigurationManagementApi(api_client)
    id = "id_example" # str | Identifier of the SAML configuration to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a SAML configuration.
        api_instance.delete_identity_provider(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling SamlConfigurationManagementApi->delete_identity_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the SAML configuration to delete. |

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
**204** | The SAML configuration was deleted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_saml_lockdown**
> disable_saml_lockdown()

Disable SAML lockdown.

Disable SAML lockdown for the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import saml_configuration_management_api
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
    api_instance = saml_configuration_management_api.SamlConfigurationManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Disable SAML lockdown.
        api_instance.disable_saml_lockdown()
    except sumologic_client.ApiException as e:
        print("Exception when calling SamlConfigurationManagementApi->disable_saml_lockdown: %s\n" % e)
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
**204** | SAML lockdown was disabled successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_saml_lockdown**
> enable_saml_lockdown()

Require SAML for sign-in.

Enabling SAML lockdown requires users to sign in using SAML preventing them from logging in with an email and password.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import saml_configuration_management_api
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
    api_instance = saml_configuration_management_api.SamlConfigurationManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Require SAML for sign-in.
        api_instance.enable_saml_lockdown()
    except sumologic_client.ApiException as e:
        print("Exception when calling SamlConfigurationManagementApi->enable_saml_lockdown: %s\n" % e)
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
**204** | SAML lockdown was enabled successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allowlisted_users**
> [AllowlistedUserResult] get_allowlisted_users()

Get list of allowlisted users.

Get a list of allowlisted users.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import saml_configuration_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.allowlisted_user_result import AllowlistedUserResult
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
    api_instance = saml_configuration_management_api.SamlConfigurationManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get list of allowlisted users.
        api_response = api_instance.get_allowlisted_users()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling SamlConfigurationManagementApi->get_allowlisted_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[AllowlistedUserResult]**](AllowlistedUserResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of allowlisted users from the organization. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_providers**
> [SamlIdentityProvider] get_identity_providers()

Get a list of SAML configurations.

Get a list of all SAML configurations in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import saml_configuration_management_api
from sumologic_client.model.saml_identity_provider import SamlIdentityProvider
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
    api_instance = saml_configuration_management_api.SamlConfigurationManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of SAML configurations.
        api_response = api_instance.get_identity_providers()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling SamlConfigurationManagementApi->get_identity_providers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[SamlIdentityProvider]**](SamlIdentityProvider.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of SAML configurations in the organization. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_identity_provider**
> SamlIdentityProvider update_identity_provider(id, saml_identity_provider_request)

Update a SAML configuration.

Update an existing SAML configuration in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import saml_configuration_management_api
from sumologic_client.model.saml_identity_provider import SamlIdentityProvider
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.saml_identity_provider_request import SamlIdentityProviderRequest
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
    api_instance = saml_configuration_management_api.SamlConfigurationManagementApi(api_client)
    id = "id_example" # str | Identifier of the SAML configuration to update.
    saml_identity_provider_request = SamlIdentityProviderRequest(
        sp_initiated_login_path="http://www.okta.com/abxcseyuiwelflkdjh",
        configuration_name="SumoLogic",
        issuer="http://www.okta.com/abxcseyuiwelflkdjh",
        sp_initiated_login_enabled=False,
        authn_request_url="https://service.sumologic.com/sumo/saml/login/9483922",
        x509cert1="x509cert1_example",
        x509cert2="",
        x509cert3="",
        on_demand_provisioning_enabled=OnDemandProvisioningInfo(
            first_name_attribute="http://schemas.microsoft.com/ws/2008/06/identity/claims/givenname",
            last_name_attribute="http://schemas.microsoft.com/ws/2008/06/identity/claims/surname",
            on_demand_provisioning_roles=[
                "Analyst/Administrator",
            ],
        ),
        roles_attribute="Sumo_Role",
        logout_enabled=False,
        logout_url="https://www.sumologic.com",
        email_attribute="attribute/subject",
        debug_mode=False,
        sign_authn_request=False,
        disable_requested_authn_context=False,
        is_redirect_binding=False,
    ) # SamlIdentityProviderRequest | Information to update in the SAML configuration.

    # example passing only required values which don't have defaults set
    try:
        # Update a SAML configuration.
        api_response = api_instance.update_identity_provider(id, saml_identity_provider_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling SamlConfigurationManagementApi->update_identity_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the SAML configuration to update. |
 **saml_identity_provider_request** | [**SamlIdentityProviderRequest**](SamlIdentityProviderRequest.md)| Information to update in the SAML configuration. |

### Return type

[**SamlIdentityProvider**](SamlIdentityProvider.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SAML configuration was successfully modified. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


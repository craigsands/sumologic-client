# sumologic_client.UserManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserManagementApi.md#create_user) | **POST** /v1/users | Create a new user.
[**delete_user**](UserManagementApi.md#delete_user) | **DELETE** /v1/users/{id} | Delete a user.
[**disable_mfa**](UserManagementApi.md#disable_mfa) | **PUT** /v1/users/{id}/mfa/disable | Disable MFA for user.
[**get_user**](UserManagementApi.md#get_user) | **GET** /v1/users/{id} | Get a user.
[**list_users**](UserManagementApi.md#list_users) | **GET** /v1/users | Get a list of users.
[**request_change_email**](UserManagementApi.md#request_change_email) | **POST** /v1/users/{id}/email/requestChange | Change email address.
[**reset_password**](UserManagementApi.md#reset_password) | **POST** /v1/users/{id}/password/reset | Reset password.
[**unlock_user**](UserManagementApi.md#unlock_user) | **POST** /v1/users/{id}/unlock | Unlock a user.
[**update_user**](UserManagementApi.md#update_user) | **PUT** /v1/users/{id} | Update a user.


# **create_user**
> UserModel create_user(create_user_definition)

Create a new user.

Create a new user in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import user_management_api
from sumologic_client.model.user_model import UserModel
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.create_user_definition import CreateUserDefinition
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
    api_instance = user_management_api.UserManagementApi(api_client)
    create_user_definition = CreateUserDefinition(
        first_name="John",
        last_name="Doe",
        email="johndoe@acme.com",
        role_ids=["00000000000001DF","00000000000002D2"],
    ) # CreateUserDefinition | Information about the new user.

    # example passing only required values which don't have defaults set
    try:
        # Create a new user.
        api_response = api_instance.create_user(create_user_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling UserManagementApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_definition** | [**CreateUserDefinition**](CreateUserDefinition.md)| Information about the new user. |

### Return type

[**UserModel**](UserModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user has been created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(id)

Delete a user.

Delete a user with the given identifier from the organization and transfer their content to the user with the identifier specified in \"transferTo\".

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import user_management_api
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
    api_instance = user_management_api.UserManagementApi(api_client)
    id = "id_example" # str | Identifier of the user to delete.
    transfer_to = "transferTo_example" # str | Identifier of the user to receive the transfer of content from the deleted user. <br> **Note:** If `deleteContent` is not set to `true`, and no user identifier is specified in `transferTo`, content from the deleted user is transferred to the executing user. (optional)
    delete_content = True # bool | Whether to delete content from the deleted user or not. <br> **Warning:** If `deleteContent` is set to `true`, all of the content for the user being deleted is permanently deleted and cannot be recovered. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a user.
        api_instance.delete_user(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling UserManagementApi->delete_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a user.
        api_instance.delete_user(id, transfer_to=transfer_to, delete_content=delete_content)
    except sumologic_client.ApiException as e:
        print("Exception when calling UserManagementApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user to delete. |
 **transfer_to** | **str**| Identifier of the user to receive the transfer of content from the deleted user. &lt;br&gt; **Note:** If &#x60;deleteContent&#x60; is not set to &#x60;true&#x60;, and no user identifier is specified in &#x60;transferTo&#x60;, content from the deleted user is transferred to the executing user. | [optional]
 **delete_content** | **bool**| Whether to delete content from the deleted user or not. &lt;br&gt; **Warning:** If &#x60;deleteContent&#x60; is set to &#x60;true&#x60;, all of the content for the user being deleted is permanently deleted and cannot be recovered. | [optional]

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
**204** | User was deleted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_mfa**
> disable_mfa(id, disable_mfa_request)

Disable MFA for user.

Disable multi-factor authentication for given user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import user_management_api
from sumologic_client.model.disable_mfa_request import DisableMfaRequest
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
    api_instance = user_management_api.UserManagementApi(api_client)
    id = "id_example" # str | Identifier of the user to disable MFA for.
    disable_mfa_request = DisableMfaRequest(
        email="johndoe@cme.com",
        password="password_example",
    ) # DisableMfaRequest | Email and Password of the user to disable MFA for.

    # example passing only required values which don't have defaults set
    try:
        # Disable MFA for user.
        api_instance.disable_mfa(id, disable_mfa_request)
    except sumologic_client.ApiException as e:
        print("Exception when calling UserManagementApi->disable_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user to disable MFA for. |
 **disable_mfa_request** | [**DisableMfaRequest**](DisableMfaRequest.md)| Email and Password of the user to disable MFA for. |

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
**204** | User&#39;s MFA was disabled successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserModel get_user(id)

Get a user.

Get a user with the given identifier from the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import user_management_api
from sumologic_client.model.user_model import UserModel
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
    api_instance = user_management_api.UserManagementApi(api_client)
    id = "id_example" # str | Identifier of user to return.

    # example passing only required values which don't have defaults set
    try:
        # Get a user.
        api_response = api_instance.get_user(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling UserManagementApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of user to return. |

### Return type

[**UserModel**](UserModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User object that was requested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUserModelsResponse list_users()

Get a list of users.

Get a list of all users in the organization. The response is paginated with a default limit of 100 users per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import user_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_user_models_response import ListUserModelsResponse
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
    api_instance = user_management_api.UserManagementApi(api_client)
    limit = 100 # int | Limit the number of users returned in the response. The number of users returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. `token` is set to null when no more pages are left. (optional)
    sort_by = "sortBy_example" # str | Sort the list of users by the `firstName`, `lastName`, or `email` field. (optional)
    email = "email_example" # str | Find user with the given email address. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of users.
        api_response = api_instance.list_users(limit=limit, token=token, sort_by=sort_by, email=email)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling UserManagementApi->list_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of users returned in the response. The number of users returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. &#x60;token&#x60; is set to null when no more pages are left. | [optional]
 **sort_by** | **str**| Sort the list of users by the &#x60;firstName&#x60;, &#x60;lastName&#x60;, or &#x60;email&#x60; field. | [optional]
 **email** | **str**| Find user with the given email address. | [optional]

### Return type

[**ListUserModelsResponse**](ListUserModelsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of users in the organization. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_change_email**
> request_change_email(id, change_email_request)

Change email address.

An email with an activation link is sent to the user’s new email address. The user must click the link in the email within seven days to complete the email address change, or the link will expire.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import user_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.change_email_request import ChangeEmailRequest
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
    api_instance = user_management_api.UserManagementApi(api_client)
    id = "id_example" # str | Identifier of the user to change email address.
    change_email_request = ChangeEmailRequest(
        email="johndoe@acme.com",
    ) # ChangeEmailRequest | New email address of the user.

    # example passing only required values which don't have defaults set
    try:
        # Change email address.
        api_instance.request_change_email(id, change_email_request)
    except sumologic_client.ApiException as e:
        print("Exception when calling UserManagementApi->request_change_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user to change email address. |
 **change_email_request** | [**ChangeEmailRequest**](ChangeEmailRequest.md)| New email address of the user. |

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
**204** | Email change request was submitted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(id)

Reset password.

Reset a user's password.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import user_management_api
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
    api_instance = user_management_api.UserManagementApi(api_client)
    id = "id_example" # str | Identifier of the user to reset password.

    # example passing only required values which don't have defaults set
    try:
        # Reset password.
        api_instance.reset_password(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling UserManagementApi->reset_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user to reset password. |

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
**204** | User&#39;s password was reset successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_user**
> unlock_user(id)

Unlock a user.

Unlock another user's account.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import user_management_api
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
    api_instance = user_management_api.UserManagementApi(api_client)
    id = "id_example" # str | The id of the user that needs to be unlocked.

    # example passing only required values which don't have defaults set
    try:
        # Unlock a user.
        api_instance.unlock_user(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling UserManagementApi->unlock_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the user that needs to be unlocked. |

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
**204** | User&#39;s account was unlocked successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserModel update_user(id, update_user_definition)

Update a user.

Update an existing user in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import user_management_api
from sumologic_client.model.user_model import UserModel
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.update_user_definition import UpdateUserDefinition
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
    api_instance = user_management_api.UserManagementApi(api_client)
    id = "id_example" # str | Identifier of the user to update.
    update_user_definition = UpdateUserDefinition(
        first_name="John",
        last_name="Doe",
        is_active=True,
        role_ids=["00000000000001DF","00000000000002D2"],
    ) # UpdateUserDefinition | Information to update about the user.

    # example passing only required values which don't have defaults set
    try:
        # Update a user.
        api_response = api_instance.update_user(id, update_user_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling UserManagementApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user to update. |
 **update_user_definition** | [**UpdateUserDefinition**](UpdateUserDefinition.md)| Information to update about the user. |

### Return type

[**UserModel**](UserModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user was successfully modified. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


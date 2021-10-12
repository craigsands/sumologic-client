# sumologic_client.RoleManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_role_to_user**](RoleManagementApi.md#assign_role_to_user) | **PUT** /v1/roles/{roleId}/users/{userId} | Assign a role to a user.
[**create_role**](RoleManagementApi.md#create_role) | **POST** /v1/roles | Create a new role.
[**delete_role**](RoleManagementApi.md#delete_role) | **DELETE** /v1/roles/{id} | Delete a role.
[**get_role**](RoleManagementApi.md#get_role) | **GET** /v1/roles/{id} | Get a role.
[**list_roles**](RoleManagementApi.md#list_roles) | **GET** /v1/roles | Get a list of roles.
[**remove_role_from_user**](RoleManagementApi.md#remove_role_from_user) | **DELETE** /v1/roles/{roleId}/users/{userId} | Remove role from a user.
[**update_role**](RoleManagementApi.md#update_role) | **PUT** /v1/roles/{id} | Update a role.


# **assign_role_to_user**
> RoleModel assign_role_to_user(role_id, user_id)

Assign a role to a user.

Assign a role to a user in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import role_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.role_model import RoleModel
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
    api_instance = role_management_api.RoleManagementApi(api_client)
    role_id = "roleId_example" # str | Identifier of the role to assign.
    user_id = "userId_example" # str | Identifier of the user to assign the role to.

    # example passing only required values which don't have defaults set
    try:
        # Assign a role to a user.
        api_response = api_instance.assign_role_to_user(role_id, user_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling RoleManagementApi->assign_role_to_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Identifier of the role to assign. |
 **user_id** | **str**| Identifier of the user to assign the role to. |

### Return type

[**RoleModel**](RoleModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role was successfully assigned to the user. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> RoleModel create_role(create_role_definition)

Create a new role.

Create a new role in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import role_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.role_model import RoleModel
from sumologic_client.model.create_role_definition import CreateRoleDefinition
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
    api_instance = role_management_api.RoleManagementApi(api_client)
    create_role_definition = CreateRoleDefinition(
        name="DataAdmin",
        description="Manage data of the org.",
        filter_predicate="!_sourceCategory=billing",
        users=["0000000006743FE0","0000000005FCE0EE"],
        capabilities=["manageContent","manageDataVolumeFeed","manageFieldExtractionRules","manageS3DataForwarding"],
        autofill_dependencies=True,
    ) # CreateRoleDefinition | Information about the new role.

    # example passing only required values which don't have defaults set
    try:
        # Create a new role.
        api_response = api_instance.create_role(create_role_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling RoleManagementApi->create_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_role_definition** | [**CreateRoleDefinition**](CreateRoleDefinition.md)| Information about the new role. |

### Return type

[**RoleModel**](RoleModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The role has been created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(id)

Delete a role.

Delete a role with the given identifier from the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import role_management_api
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
    api_instance = role_management_api.RoleManagementApi(api_client)
    id = "id_example" # str | Identifier of the role to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a role.
        api_instance.delete_role(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling RoleManagementApi->delete_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the role to delete. |

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
**204** | Role was deleted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleModel get_role(id)

Get a role.

Get a role with the given identifier in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import role_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.role_model import RoleModel
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
    api_instance = role_management_api.RoleManagementApi(api_client)
    id = "id_example" # str | Identifier of the role to fetch.

    # example passing only required values which don't have defaults set
    try:
        # Get a role.
        api_response = api_instance.get_role(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling RoleManagementApi->get_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the role to fetch. |

### Return type

[**RoleModel**](RoleModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role object that was requested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> ListRoleModelsResponse list_roles()

Get a list of roles.

Get a list of all the roles in the organization. The response is paginated with a default limit of 100 roles per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import role_management_api
from sumologic_client.model.list_role_models_response import ListRoleModelsResponse
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
    api_instance = role_management_api.RoleManagementApi(api_client)
    limit = 100 # int | Limit the number of roles returned in the response. The number of roles returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. `token` is set to null when no more pages are left. (optional)
    sort_by = "sortBy_example" # str | Sort the list of roles by the `name` field. (optional)
    name = "name_example" # str | Only return roles matching the given name. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of roles.
        api_response = api_instance.list_roles(limit=limit, token=token, sort_by=sort_by, name=name)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling RoleManagementApi->list_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of roles returned in the response. The number of roles returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. &#x60;token&#x60; is set to null when no more pages are left. | [optional]
 **sort_by** | **str**| Sort the list of roles by the &#x60;name&#x60; field. | [optional]
 **name** | **str**| Only return roles matching the given name. | [optional]

### Return type

[**ListRoleModelsResponse**](ListRoleModelsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of roles in the organization. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role_from_user**
> remove_role_from_user(role_id, user_id)

Remove role from a user.

Remove a role from a user in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import role_management_api
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
    api_instance = role_management_api.RoleManagementApi(api_client)
    role_id = "roleId_example" # str | Identifier of the role to delete.
    user_id = "userId_example" # str | Identifier of the user to remove the role from.

    # example passing only required values which don't have defaults set
    try:
        # Remove role from a user.
        api_instance.remove_role_from_user(role_id, user_id)
    except sumologic_client.ApiException as e:
        print("Exception when calling RoleManagementApi->remove_role_from_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Identifier of the role to delete. |
 **user_id** | **str**| Identifier of the user to remove the role from. |

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
**204** | Role was successfully removed from the user. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> RoleModel update_role(id, update_role_definition)

Update a role.

Update an existing role in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import role_management_api
from sumologic_client.model.update_role_definition import UpdateRoleDefinition
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.role_model import RoleModel
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
    api_instance = role_management_api.RoleManagementApi(api_client)
    id = "id_example" # str | Identifier of the role to update.
    update_role_definition = UpdateRoleDefinition(
        name="DataAdmin",
        description="Manage data of the org.",
        filter_predicate="!_sourceCategory=billing",
        users=["0000000006743FE0","0000000005FCE0EE"],
        capabilities=["manageContent","manageDataVolumeFeed","manageFieldExtractionRules","manageS3DataForwarding"],
        autofill_dependencies=True,
    ) # UpdateRoleDefinition | Information to update about the role.

    # example passing only required values which don't have defaults set
    try:
        # Update a role.
        api_response = api_instance.update_role(id, update_role_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling RoleManagementApi->update_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the role to update. |
 **update_role_definition** | [**UpdateRoleDefinition**](UpdateRoleDefinition.md)| Information to update about the role. |

### Return type

[**RoleModel**](RoleModel.md)

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


# sumologic_client.FieldManagementV1Api

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_field**](FieldManagementV1Api.md#create_field) | **POST** /v1/fields | Create a new field.
[**delete_field**](FieldManagementV1Api.md#delete_field) | **DELETE** /v1/fields/{id} | Delete a custom field.
[**disable_field**](FieldManagementV1Api.md#disable_field) | **DELETE** /v1/fields/{id}/disable | Disable a custom field.
[**enable_field**](FieldManagementV1Api.md#enable_field) | **PUT** /v1/fields/{id}/enable | Enable custom field with a specified identifier.
[**get_built_in_field**](FieldManagementV1Api.md#get_built_in_field) | **GET** /v1/fields/builtin/{id} | Get a built-in field.
[**get_custom_field**](FieldManagementV1Api.md#get_custom_field) | **GET** /v1/fields/{id} | Get a custom field.
[**get_field_quota**](FieldManagementV1Api.md#get_field_quota) | **GET** /v1/fields/quota | Get capacity information.
[**list_built_in_fields**](FieldManagementV1Api.md#list_built_in_fields) | **GET** /v1/fields/builtin | Get a list of built-in fields.
[**list_custom_fields**](FieldManagementV1Api.md#list_custom_fields) | **GET** /v1/fields | Get a list of all custom fields.
[**list_dropped_fields**](FieldManagementV1Api.md#list_dropped_fields) | **GET** /v1/fields/dropped | Get a list of dropped fields.


# **create_field**
> CustomField create_field(field_name)

Create a new field.

Adding a field will define it in the Fields schema allowing it to be assigned as metadata to your logs.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import field_management_v1_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.custom_field import CustomField
from sumologic_client.model.field_name import FieldName
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
    api_instance = field_management_v1_api.FieldManagementV1Api(api_client)
    field_name = FieldName(
        field_name="hostIP",
    ) # FieldName | Name of a field to add. The name is used as the key in the key-value pair.

    # example passing only required values which don't have defaults set
    try:
        # Create a new field.
        api_response = api_instance.create_field(field_name)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FieldManagementV1Api->create_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | [**FieldName**](FieldName.md)| Name of a field to add. The name is used as the key in the key-value pair. |

### Return type

[**CustomField**](CustomField.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The field was created successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field**
> delete_field(id)

Delete a custom field.

Deleting a field does not delete historical data assigned with that field. If you  delete a field by mistake and one or more of those dependencies break, you can  re-add the field to get things working properly again. You should always disable  a field and ensure things are behaving as expected before deleting a field.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import field_management_v1_api
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
    api_instance = field_management_v1_api.FieldManagementV1Api(api_client)
    id = "00000000031D02DA" # str | Identifier of a field to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a custom field.
        api_instance.delete_field(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling FieldManagementV1Api->delete_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a field to delete. |

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
**204** | The field was successfully deleted. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_field**
> disable_field(id)

Disable a custom field.

After disabling a field Sumo Logic will start dropping its incoming values at ingest. As a result, they won't be searchable or usable. Historical values are not removed and remain searchable.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import field_management_v1_api
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
    api_instance = field_management_v1_api.FieldManagementV1Api(api_client)
    id = "00000000031D02DA" # str | Identifier of a field to disable.

    # example passing only required values which don't have defaults set
    try:
        # Disable a custom field.
        api_instance.disable_field(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling FieldManagementV1Api->disable_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a field to disable. |

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
**204** | Field has been disabled. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_field**
> enable_field(id)

Enable custom field with a specified identifier.

Fields have to be enabled to be assigned to your data. This operation ensures that a specified field is enabled and Sumo Logic will treat it as safe to process. All manually created custom fields are  enabled by default.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import field_management_v1_api
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
    api_instance = field_management_v1_api.FieldManagementV1Api(api_client)
    id = "00000000031D02DA" # str | Identifier of a field to enable.

    # example passing only required values which don't have defaults set
    try:
        # Enable custom field with a specified identifier.
        api_instance.enable_field(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling FieldManagementV1Api->enable_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a field to enable. |

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
**204** | Field has been enabled. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_built_in_field**
> BuiltinField get_built_in_field(id)

Get a built-in field.

Get the details of a built-in field.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import field_management_v1_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.builtin_field import BuiltinField
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
    api_instance = field_management_v1_api.FieldManagementV1Api(api_client)
    id = "000000000000000A" # str | Identifier of a built-in field.

    # example passing only required values which don't have defaults set
    try:
        # Get a built-in field.
        api_response = api_instance.get_built_in_field(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FieldManagementV1Api->get_built_in_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a built-in field. |

### Return type

[**BuiltinField**](BuiltinField.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the built-in field. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field**
> CustomField get_custom_field(id)

Get a custom field.

Get the details of a custom field.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import field_management_v1_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.custom_field import CustomField
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
    api_instance = field_management_v1_api.FieldManagementV1Api(api_client)
    id = "00000000031D02DA" # str | Identifier of a field.

    # example passing only required values which don't have defaults set
    try:
        # Get a custom field.
        api_response = api_instance.get_custom_field(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FieldManagementV1Api->get_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a field. |

### Return type

[**CustomField**](CustomField.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the custom field. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_quota**
> FieldQuotaUsage get_field_quota()

Get capacity information.

Every account has a limited number of fields available. This endpoint returns your account limitations and remaining quota.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import field_management_v1_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.field_quota_usage import FieldQuotaUsage
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
    api_instance = field_management_v1_api.FieldManagementV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get capacity information.
        api_response = api_instance.get_field_quota()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FieldManagementV1Api->get_field_quota: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FieldQuotaUsage**](FieldQuotaUsage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current fields capacity usage (fields count). |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_built_in_fields**
> ListBuiltinFieldsResponse list_built_in_fields()

Get a list of built-in fields.

Built-in fields are created automatically by Sumo Logic for standard configuration purposes. They include `_sourceHost` and `_sourceCategory`. Built-in fields can't be deleted or disabled.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import field_management_v1_api
from sumologic_client.model.list_builtin_fields_response import ListBuiltinFieldsResponse
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
    api_instance = field_management_v1_api.FieldManagementV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of built-in fields.
        api_response = api_instance.list_built_in_fields()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FieldManagementV1Api->list_built_in_fields: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListBuiltinFieldsResponse**](ListBuiltinFieldsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all built-in fields. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_fields**
> ListCustomFieldsResponse list_custom_fields()

Get a list of all custom fields.

Request a list of all the custom fields configured in your account.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import field_management_v1_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_custom_fields_response import ListCustomFieldsResponse
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
    api_instance = field_management_v1_api.FieldManagementV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of all custom fields.
        api_response = api_instance.list_custom_fields()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FieldManagementV1Api->list_custom_fields: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCustomFieldsResponse**](ListCustomFieldsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all custom fields. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dropped_fields**
> ListDroppedFieldsResponse list_dropped_fields()

Get a list of dropped fields.

Dropped fields are fields sent to Sumo Logic, but are ignored since they are not defined in your Fields schema. In order to save these values a field must both exist and be enabled.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import field_management_v1_api
from sumologic_client.model.list_dropped_fields_response import ListDroppedFieldsResponse
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
    api_instance = field_management_v1_api.FieldManagementV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of dropped fields.
        api_response = api_instance.list_dropped_fields()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling FieldManagementV1Api->list_dropped_fields: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListDroppedFieldsResponse**](ListDroppedFieldsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of dropped fields.  |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


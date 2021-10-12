# sumologic_client.DynamicParsingRuleManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dynamic_parsing_rule**](DynamicParsingRuleManagementApi.md#create_dynamic_parsing_rule) | **POST** /v1/dynamicParsingRules | Create a new dynamic parsing rule.
[**delete_dynamic_parsing_rule**](DynamicParsingRuleManagementApi.md#delete_dynamic_parsing_rule) | **DELETE** /v1/dynamicParsingRules/{id} | Delete a dynamic parsing rule.
[**get_dynamic_parsing_rule**](DynamicParsingRuleManagementApi.md#get_dynamic_parsing_rule) | **GET** /v1/dynamicParsingRules/{id} | Get a dynamic parsing rule.
[**list_dynamic_parsing_rules**](DynamicParsingRuleManagementApi.md#list_dynamic_parsing_rules) | **GET** /v1/dynamicParsingRules | Get a list of dynamic parsing rules.
[**update_dynamic_parsing_rule**](DynamicParsingRuleManagementApi.md#update_dynamic_parsing_rule) | **PUT** /v1/dynamicParsingRules/{id} | Update a dynamic parsing rule.


# **create_dynamic_parsing_rule**
> DynamicRule create_dynamic_parsing_rule(dynamic_rule_definition)

Create a new dynamic parsing rule.

Create a new dynamic parsing rule.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dynamic_parsing_rule_management_api
from sumologic_client.model.dynamic_rule_definition import DynamicRuleDefinition
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.dynamic_rule import DynamicRule
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
    api_instance = dynamic_parsing_rule_management_api.DynamicParsingRuleManagementApi(api_client)
    dynamic_rule_definition = DynamicRuleDefinition(
        name="DynamicParsingRule123",
        scope="_sourceHost=127.0.0.1",
        enabled=False,
    ) # DynamicRuleDefinition | Information about the new dynamic parsing rule.

    # example passing only required values which don't have defaults set
    try:
        # Create a new dynamic parsing rule.
        api_response = api_instance.create_dynamic_parsing_rule(dynamic_rule_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling DynamicParsingRuleManagementApi->create_dynamic_parsing_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_rule_definition** | [**DynamicRuleDefinition**](DynamicRuleDefinition.md)| Information about the new dynamic parsing rule. |

### Return type

[**DynamicRule**](DynamicRule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dynamic parsing rule has been created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dynamic_parsing_rule**
> delete_dynamic_parsing_rule(id)

Delete a dynamic parsing rule.

Delete a dynamic parsing rule with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dynamic_parsing_rule_management_api
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
    api_instance = dynamic_parsing_rule_management_api.DynamicParsingRuleManagementApi(api_client)
    id = "0000000001C41EE4" # str | Identifier of the dynamic parsing rule to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a dynamic parsing rule.
        api_instance.delete_dynamic_parsing_rule(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling DynamicParsingRuleManagementApi->delete_dynamic_parsing_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the dynamic parsing rule to delete. |

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
**204** | Dynamic parsing rule was deleted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_parsing_rule**
> DynamicRule get_dynamic_parsing_rule(id)

Get a dynamic parsing rule.

Get a dynamic parsing rule with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dynamic_parsing_rule_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.dynamic_rule import DynamicRule
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
    api_instance = dynamic_parsing_rule_management_api.DynamicParsingRuleManagementApi(api_client)
    id = "0000000001C41EE4" # str | Identifier of dynamic parsing rule to return.

    # example passing only required values which don't have defaults set
    try:
        # Get a dynamic parsing rule.
        api_response = api_instance.get_dynamic_parsing_rule(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling DynamicParsingRuleManagementApi->get_dynamic_parsing_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of dynamic parsing rule to return. |

### Return type

[**DynamicRule**](DynamicRule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dynamic parsing rule object that was requested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dynamic_parsing_rules**
> ListDynamicRulesResponse list_dynamic_parsing_rules()

Get a list of dynamic parsing rules.

Get a list of all dynamic parsing rules. The response is paginated with a default limit of 100 dynamic parsing rules per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dynamic_parsing_rule_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_dynamic_rules_response import ListDynamicRulesResponse
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
    api_instance = dynamic_parsing_rule_management_api.DynamicParsingRuleManagementApi(api_client)
    limit = 10 # int | Limit the number of dynamic parsing rules returned in the response. The number of dynamic parsing rules returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "0000000001C51FF7" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of dynamic parsing rules.
        api_response = api_instance.list_dynamic_parsing_rules(limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling DynamicParsingRuleManagementApi->list_dynamic_parsing_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of dynamic parsing rules returned in the response. The number of dynamic parsing rules returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. | [optional]

### Return type

[**ListDynamicRulesResponse**](ListDynamicRulesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of dynamic parsing rules. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dynamic_parsing_rule**
> DynamicRule update_dynamic_parsing_rule(id, dynamic_rule_definition)

Update a dynamic parsing rule.

Update an existing dynamic parsing rule. All properties specified in the request are replaced. Missing properties are set to their default values.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dynamic_parsing_rule_management_api
from sumologic_client.model.dynamic_rule_definition import DynamicRuleDefinition
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.dynamic_rule import DynamicRule
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
    api_instance = dynamic_parsing_rule_management_api.DynamicParsingRuleManagementApi(api_client)
    id = "0000000001C41EE4" # str | Identifier of the dynamic parsing rule to update.
    dynamic_rule_definition = DynamicRuleDefinition(
        name="DynamicParsingRule123",
        scope="_sourceHost=127.0.0.1",
        enabled=False,
    ) # DynamicRuleDefinition | Information to update about the dynamic parsing rule.

    # example passing only required values which don't have defaults set
    try:
        # Update a dynamic parsing rule.
        api_response = api_instance.update_dynamic_parsing_rule(id, dynamic_rule_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling DynamicParsingRuleManagementApi->update_dynamic_parsing_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the dynamic parsing rule to update. |
 **dynamic_rule_definition** | [**DynamicRuleDefinition**](DynamicRuleDefinition.md)| Information to update about the dynamic parsing rule. |

### Return type

[**DynamicRule**](DynamicRule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dynamic parsing rule was successfully modified. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


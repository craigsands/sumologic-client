# sumologic_client.ExtractionRuleManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_extraction_rule**](ExtractionRuleManagementApi.md#create_extraction_rule) | **POST** /v1/extractionRules | Create a new field extraction rule.
[**delete_extraction_rule**](ExtractionRuleManagementApi.md#delete_extraction_rule) | **DELETE** /v1/extractionRules/{id} | Delete a field extraction rule.
[**get_extraction_rule**](ExtractionRuleManagementApi.md#get_extraction_rule) | **GET** /v1/extractionRules/{id} | Get a field extraction rule.
[**list_extraction_rules**](ExtractionRuleManagementApi.md#list_extraction_rules) | **GET** /v1/extractionRules | Get a list of field extraction rules.
[**update_extraction_rule**](ExtractionRuleManagementApi.md#update_extraction_rule) | **PUT** /v1/extractionRules/{id} | Update a field extraction rule.


# **create_extraction_rule**
> ExtractionRule create_extraction_rule(extraction_rule_definition)

Create a new field extraction rule.

Create a new field extraction rule.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import extraction_rule_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.extraction_rule import ExtractionRule
from sumologic_client.model.extraction_rule_definition import ExtractionRuleDefinition
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
    api_instance = extraction_rule_management_api.ExtractionRuleManagementApi(api_client)
    extraction_rule_definition = ExtractionRuleDefinition() # ExtractionRuleDefinition | Information about the new field extraction rule.

    # example passing only required values which don't have defaults set
    try:
        # Create a new field extraction rule.
        api_response = api_instance.create_extraction_rule(extraction_rule_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ExtractionRuleManagementApi->create_extraction_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extraction_rule_definition** | [**ExtractionRuleDefinition**](ExtractionRuleDefinition.md)| Information about the new field extraction rule. |

### Return type

[**ExtractionRule**](ExtractionRule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The field extraction rule has been created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extraction_rule**
> delete_extraction_rule(id)

Delete a field extraction rule.

Delete a field extraction rule with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import extraction_rule_management_api
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
    api_instance = extraction_rule_management_api.ExtractionRuleManagementApi(api_client)
    id = "id_example" # str | Identifier of the field extraction rule to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a field extraction rule.
        api_instance.delete_extraction_rule(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling ExtractionRuleManagementApi->delete_extraction_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the field extraction rule to delete. |

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
**204** | Extraction rule was deleted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extraction_rule**
> ExtractionRule get_extraction_rule(id)

Get a field extraction rule.

Get a field extraction rule with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import extraction_rule_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.extraction_rule import ExtractionRule
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
    api_instance = extraction_rule_management_api.ExtractionRuleManagementApi(api_client)
    id = "id_example" # str | Identifier of field extraction rule to return.

    # example passing only required values which don't have defaults set
    try:
        # Get a field extraction rule.
        api_response = api_instance.get_extraction_rule(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ExtractionRuleManagementApi->get_extraction_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of field extraction rule to return. |

### Return type

[**ExtractionRule**](ExtractionRule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extraction rule object that was requested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_extraction_rules**
> ListExtractionRulesResponse list_extraction_rules()

Get a list of field extraction rules.

Get a list of all field extraction rules. The response is paginated with a default limit of 100 field extraction rules per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import extraction_rule_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_extraction_rules_response import ListExtractionRulesResponse
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
    api_instance = extraction_rule_management_api.ExtractionRuleManagementApi(api_client)
    limit = 100 # int | Limit the number of field extraction rules returned in the response. The number of field extraction rules returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of field extraction rules.
        api_response = api_instance.list_extraction_rules(limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ExtractionRuleManagementApi->list_extraction_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of field extraction rules returned in the response. The number of field extraction rules returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. | [optional]

### Return type

[**ListExtractionRulesResponse**](ListExtractionRulesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of field extraction rules. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_extraction_rule**
> ExtractionRule update_extraction_rule(id, update_extraction_rule_definition)

Update a field extraction rule.

Update an existing field extraction rule. All properties specified in the request are replaced. Missing properties are set to their default values.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import extraction_rule_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.extraction_rule import ExtractionRule
from sumologic_client.model.update_extraction_rule_definition import UpdateExtractionRuleDefinition
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
    api_instance = extraction_rule_management_api.ExtractionRuleManagementApi(api_client)
    id = "id_example" # str | Identifier of the field extraction rule to update.
    update_extraction_rule_definition = UpdateExtractionRuleDefinition() # UpdateExtractionRuleDefinition | Information to update about the field extraction rule.

    # example passing only required values which don't have defaults set
    try:
        # Update a field extraction rule.
        api_response = api_instance.update_extraction_rule(id, update_extraction_rule_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ExtractionRuleManagementApi->update_extraction_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the field extraction rule to update. |
 **update_extraction_rule_definition** | [**UpdateExtractionRuleDefinition**](UpdateExtractionRuleDefinition.md)| Information to update about the field extraction rule. |

### Return type

[**ExtractionRule**](ExtractionRule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The field extraction rule was successfully modified. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


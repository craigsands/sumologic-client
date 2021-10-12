# sumologic_client.TransformationRuleManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rule**](TransformationRuleManagementApi.md#create_rule) | **POST** /v1/transformationRules | Create a new transformation rule.
[**delete_rule**](TransformationRuleManagementApi.md#delete_rule) | **DELETE** /v1/transformationRules/{id} | Delete a transformation rule.
[**get_transformation_rule**](TransformationRuleManagementApi.md#get_transformation_rule) | **GET** /v1/transformationRules/{id} | Get a transformation rule.
[**get_transformation_rules**](TransformationRuleManagementApi.md#get_transformation_rules) | **GET** /v1/transformationRules | Get a list of transformation rules.
[**update_transformation_rule**](TransformationRuleManagementApi.md#update_transformation_rule) | **PUT** /v1/transformationRules/{id} | Update a transformation rule.


# **create_rule**
> TransformationRuleResponse create_rule(transformation_rule_request)

Create a new transformation rule.

Create a new transformation rule.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import transformation_rule_management_api
from sumologic_client.model.transformation_rule_request import TransformationRuleRequest
from sumologic_client.model.transformation_rule_response import TransformationRuleResponse
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
    api_instance = transformation_rule_management_api.TransformationRuleManagementApi(api_client)
    transformation_rule_request = TransformationRuleRequest(
        rule_definition=TransformationRuleDefinition(
            name="Transformation Rule 1",
            selector="_sourceCategory=metricsstore",
            dimension_transformations=[
                DimensionTransformation(),
            ],
            transformed_metrics_retention=8,
            retention=8,
        ),
        enabled=True,
    ) # TransformationRuleRequest | The configuration of the transformation rule to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a new transformation rule.
        api_response = api_instance.create_rule(transformation_rule_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling TransformationRuleManagementApi->create_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transformation_rule_request** | [**TransformationRuleRequest**](TransformationRuleRequest.md)| The configuration of the transformation rule to create. |

### Return type

[**TransformationRuleResponse**](TransformationRuleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transformation rule was successfully created. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> delete_rule(id)

Delete a transformation rule.

Delete a transformation rule with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import transformation_rule_management_api
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
    api_instance = transformation_rule_management_api.TransformationRuleManagementApi(api_client)
    id = "id_example" # str | Identifier of the transformation rule to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a transformation rule.
        api_instance.delete_rule(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling TransformationRuleManagementApi->delete_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the transformation rule to delete. |

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
**204** | The transformation rule was successfully deleted. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transformation_rule**
> TransformationRuleResponse get_transformation_rule(id)

Get a transformation rule.

Get a transformation rule with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import transformation_rule_management_api
from sumologic_client.model.transformation_rule_response import TransformationRuleResponse
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
    api_instance = transformation_rule_management_api.TransformationRuleManagementApi(api_client)
    id = "id_example" # str | Identifier of transformation rule to return.

    # example passing only required values which don't have defaults set
    try:
        # Get a transformation rule.
        api_response = api_instance.get_transformation_rule(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling TransformationRuleManagementApi->get_transformation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of transformation rule to return. |

### Return type

[**TransformationRuleResponse**](TransformationRuleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transformation rule object that was requested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transformation_rules**
> TransformationRulesResponse get_transformation_rules()

Get a list of transformation rules.

Get a list of transformation rules in the organization. The response is paginated with a default limit of 100 rules per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import transformation_rule_management_api
from sumologic_client.model.transformation_rules_response import TransformationRulesResponse
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
    api_instance = transformation_rule_management_api.TransformationRuleManagementApi(api_client)
    limit = 10 # int | Limit the number of transformation rules returned in the response. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. `token` is set to null when no more pages are left. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of transformation rules.
        api_response = api_instance.get_transformation_rules(limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling TransformationRuleManagementApi->get_transformation_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of transformation rules returned in the response. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. &#x60;token&#x60; is set to null when no more pages are left. | [optional]

### Return type

[**TransformationRulesResponse**](TransformationRulesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of transformation rules. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transformation_rule**
> TransformationRuleResponse update_transformation_rule(id, transformation_rule_request)

Update a transformation rule.

Update an existing transformation rule. All properties specified in the request are replaced. Missing properties will remain the same.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import transformation_rule_management_api
from sumologic_client.model.transformation_rule_request import TransformationRuleRequest
from sumologic_client.model.transformation_rule_response import TransformationRuleResponse
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
    api_instance = transformation_rule_management_api.TransformationRuleManagementApi(api_client)
    id = "id_example" # str | Identifier of the transformation rule to update.
    transformation_rule_request = TransformationRuleRequest(
        rule_definition=TransformationRuleDefinition(
            name="Transformation Rule 1",
            selector="_sourceCategory=metricsstore",
            dimension_transformations=[
                DimensionTransformation(),
            ],
            transformed_metrics_retention=8,
            retention=8,
        ),
        enabled=True,
    ) # TransformationRuleRequest | Information to update about the transformation rule.

    # example passing only required values which don't have defaults set
    try:
        # Update a transformation rule.
        api_response = api_instance.update_transformation_rule(id, transformation_rule_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling TransformationRuleManagementApi->update_transformation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the transformation rule to update. |
 **transformation_rule_request** | [**TransformationRuleRequest**](TransformationRuleRequest.md)| Information to update about the transformation rule. |

### Return type

[**TransformationRuleResponse**](TransformationRuleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transformation rule was successfully modified. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


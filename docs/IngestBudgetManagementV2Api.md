# sumologic_client.IngestBudgetManagementV2Api

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ingest_budget_v2**](IngestBudgetManagementV2Api.md#create_ingest_budget_v2) | **POST** /v2/ingestBudgets | Create a new ingest budget.
[**delete_ingest_budget_v2**](IngestBudgetManagementV2Api.md#delete_ingest_budget_v2) | **DELETE** /v2/ingestBudgets/{id} | Delete an ingest budget.
[**get_ingest_budget_v2**](IngestBudgetManagementV2Api.md#get_ingest_budget_v2) | **GET** /v2/ingestBudgets/{id} | Get an ingest budget.
[**list_ingest_budgets_v2**](IngestBudgetManagementV2Api.md#list_ingest_budgets_v2) | **GET** /v2/ingestBudgets | Get a list of ingest budgets.
[**reset_usage_v2**](IngestBudgetManagementV2Api.md#reset_usage_v2) | **POST** /v2/ingestBudgets/{id}/usage/reset | Reset usage.
[**update_ingest_budget_v2**](IngestBudgetManagementV2Api.md#update_ingest_budget_v2) | **PUT** /v2/ingestBudgets/{id} | Update an ingest budget.


# **create_ingest_budget_v2**
> IngestBudgetV2 create_ingest_budget_v2(ingest_budget_definition_v2)

Create a new ingest budget.

Create a new ingest budget.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v2_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.ingest_budget_definition_v2 import IngestBudgetDefinitionV2
from sumologic_client.model.ingest_budget_v2 import IngestBudgetV2
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
    api_instance = ingest_budget_management_v2_api.IngestBudgetManagementV2Api(api_client)
    ingest_budget_definition_v2 = IngestBudgetDefinitionV2(
        name="Developer Budget",
        scope="_sourceCategory=*prod*nginx*",
        capacity_bytes=1000,
        timezone="America/Los_Angeles",
        reset_time="23:30",
        description="description_example",
        action="stopCollecting",
        audit_threshold=85,
    ) # IngestBudgetDefinitionV2 | Information about the new ingest budget.

    # example passing only required values which don't have defaults set
    try:
        # Create a new ingest budget.
        api_response = api_instance.create_ingest_budget_v2(ingest_budget_definition_v2)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV2Api->create_ingest_budget_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_budget_definition_v2** | [**IngestBudgetDefinitionV2**](IngestBudgetDefinitionV2.md)| Information about the new ingest budget. |

### Return type

[**IngestBudgetV2**](IngestBudgetV2.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ingest budget has been created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ingest_budget_v2**
> delete_ingest_budget_v2(id)

Delete an ingest budget.

Delete an ingest budget with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v2_api
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
    api_instance = ingest_budget_management_v2_api.IngestBudgetManagementV2Api(api_client)
    id = "id_example" # str | Identifier of the ingest budget to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete an ingest budget.
        api_instance.delete_ingest_budget_v2(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV2Api->delete_ingest_budget_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the ingest budget to delete. |

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
**204** | The ingest budget was deleted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingest_budget_v2**
> IngestBudgetV2 get_ingest_budget_v2(id)

Get an ingest budget.

Get an ingest budget by the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v2_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.ingest_budget_v2 import IngestBudgetV2
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
    api_instance = ingest_budget_management_v2_api.IngestBudgetManagementV2Api(api_client)
    id = "id_example" # str | Identifier of ingest budget to return.

    # example passing only required values which don't have defaults set
    try:
        # Get an ingest budget.
        api_response = api_instance.get_ingest_budget_v2(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV2Api->get_ingest_budget_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of ingest budget to return. |

### Return type

[**IngestBudgetV2**](IngestBudgetV2.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ingest budget object that was requested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ingest_budgets_v2**
> ListIngestBudgetsResponseV2 list_ingest_budgets_v2()

Get a list of ingest budgets.

Get a list of all ingest budgets. The response is paginated with a default limit of 100 budgets per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v2_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_ingest_budgets_response_v2 import ListIngestBudgetsResponseV2
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
    api_instance = ingest_budget_management_v2_api.IngestBudgetManagementV2Api(api_client)
    limit = 100 # int | Limit the number of budgets returned in the response. The number of budgets returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of ingest budgets.
        api_response = api_instance.list_ingest_budgets_v2(limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV2Api->list_ingest_budgets_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of budgets returned in the response. The number of budgets returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. | [optional]

### Return type

[**ListIngestBudgetsResponseV2**](ListIngestBudgetsResponseV2.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of budgets. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_usage_v2**
> reset_usage_v2(id)

Reset usage.

Reset ingest budget's current usage to 0 before the scheduled reset time.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v2_api
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
    api_instance = ingest_budget_management_v2_api.IngestBudgetManagementV2Api(api_client)
    id = "id_example" # str | Identifier of the ingest budget to reset usage.

    # example passing only required values which don't have defaults set
    try:
        # Reset usage.
        api_instance.reset_usage_v2(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV2Api->reset_usage_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the ingest budget to reset usage. |

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
**200** | Ingest budget&#39;s usage was reset successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ingest_budget_v2**
> IngestBudgetV2 update_ingest_budget_v2(id, ingest_budget_definition_v2)

Update an ingest budget.

Update an existing ingest budget. All properties specified in the request are required.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v2_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.ingest_budget_definition_v2 import IngestBudgetDefinitionV2
from sumologic_client.model.ingest_budget_v2 import IngestBudgetV2
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
    api_instance = ingest_budget_management_v2_api.IngestBudgetManagementV2Api(api_client)
    id = "id_example" # str | Identifier of the ingest budget to update.
    ingest_budget_definition_v2 = IngestBudgetDefinitionV2(
        name="Developer Budget",
        scope="_sourceCategory=*prod*nginx*",
        capacity_bytes=1000,
        timezone="America/Los_Angeles",
        reset_time="23:30",
        description="description_example",
        action="stopCollecting",
        audit_threshold=85,
    ) # IngestBudgetDefinitionV2 | Information to update about the ingest budget.

    # example passing only required values which don't have defaults set
    try:
        # Update an ingest budget.
        api_response = api_instance.update_ingest_budget_v2(id, ingest_budget_definition_v2)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV2Api->update_ingest_budget_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the ingest budget to update. |
 **ingest_budget_definition_v2** | [**IngestBudgetDefinitionV2**](IngestBudgetDefinitionV2.md)| Information to update about the ingest budget. |

### Return type

[**IngestBudgetV2**](IngestBudgetV2.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ingest budget was successfully modified. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


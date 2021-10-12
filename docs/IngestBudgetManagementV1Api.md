# sumologic_client.IngestBudgetManagementV1Api

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_collector_to_budget**](IngestBudgetManagementV1Api.md#assign_collector_to_budget) | **PUT** /v1/ingestBudgets/{id}/collectors/{collectorId} | Assign a Collector to a budget.
[**create_ingest_budget**](IngestBudgetManagementV1Api.md#create_ingest_budget) | **POST** /v1/ingestBudgets | Create a new ingest budget.
[**delete_ingest_budget**](IngestBudgetManagementV1Api.md#delete_ingest_budget) | **DELETE** /v1/ingestBudgets/{id} | Delete an ingest budget.
[**get_assigned_collectors**](IngestBudgetManagementV1Api.md#get_assigned_collectors) | **GET** /v1/ingestBudgets/{id}/collectors | Get a list of Collectors.
[**get_ingest_budget**](IngestBudgetManagementV1Api.md#get_ingest_budget) | **GET** /v1/ingestBudgets/{id} | Get an ingest budget.
[**list_ingest_budgets**](IngestBudgetManagementV1Api.md#list_ingest_budgets) | **GET** /v1/ingestBudgets | Get a list of ingest budgets.
[**remove_collector_from_budget**](IngestBudgetManagementV1Api.md#remove_collector_from_budget) | **DELETE** /v1/ingestBudgets/{id}/collectors/{collectorId} | Remove Collector from a budget.
[**reset_usage**](IngestBudgetManagementV1Api.md#reset_usage) | **POST** /v1/ingestBudgets/{id}/usage/reset | Reset usage.
[**update_ingest_budget**](IngestBudgetManagementV1Api.md#update_ingest_budget) | **PUT** /v1/ingestBudgets/{id} | Update an ingest budget.


# **assign_collector_to_budget**
> IngestBudget assign_collector_to_budget(id, collector_id)

Assign a Collector to a budget.

Assign a Collector to a budget.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v1_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.ingest_budget import IngestBudget
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
    api_instance = ingest_budget_management_v1_api.IngestBudgetManagementV1Api(api_client)
    id = "id_example" # str | Identifier of the ingest budget to assign to the Collector.
    collector_id = "collectorId_example" # str | Identifier of the Collector to assign.

    # example passing only required values which don't have defaults set
    try:
        # Assign a Collector to a budget.
        api_response = api_instance.assign_collector_to_budget(id, collector_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV1Api->assign_collector_to_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the ingest budget to assign to the Collector. |
 **collector_id** | **str**| Identifier of the Collector to assign. |

### Return type

[**IngestBudget**](IngestBudget.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collector was successfully assigned to the ingest budget. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ingest_budget**
> IngestBudget create_ingest_budget(ingest_budget_definition)

Create a new ingest budget.

Create a new ingest budget.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v1_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.ingest_budget_definition import IngestBudgetDefinition
from sumologic_client.model.ingest_budget import IngestBudget
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
    api_instance = ingest_budget_management_v1_api.IngestBudgetManagementV1Api(api_client)
    ingest_budget_definition = IngestBudgetDefinition(
        name="Developer Budget",
        field_value="dev_30_gb",
        capacity_bytes=1000,
        timezone="America/Los_Angeles",
        reset_time="23:30",
        description="description_example",
        action="stopCollecting",
        audit_threshold=85,
    ) # IngestBudgetDefinition | Information about the new ingest budget.

    # example passing only required values which don't have defaults set
    try:
        # Create a new ingest budget.
        api_response = api_instance.create_ingest_budget(ingest_budget_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV1Api->create_ingest_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_budget_definition** | [**IngestBudgetDefinition**](IngestBudgetDefinition.md)| Information about the new ingest budget. |

### Return type

[**IngestBudget**](IngestBudget.md)

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

# **delete_ingest_budget**
> delete_ingest_budget(id)

Delete an ingest budget.

Delete an ingest budget with the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v1_api
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
    api_instance = ingest_budget_management_v1_api.IngestBudgetManagementV1Api(api_client)
    id = "id_example" # str | Identifier of the ingest budget to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete an ingest budget.
        api_instance.delete_ingest_budget(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV1Api->delete_ingest_budget: %s\n" % e)
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

# **get_assigned_collectors**
> ListCollectorIdentitiesResponse get_assigned_collectors(id)

Get a list of Collectors.

Get a list of Collectors assigned to an ingest budget. The response is paginated with a default limit of 100 Collectors per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v1_api
from sumologic_client.model.list_collector_identities_response import ListCollectorIdentitiesResponse
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
    api_instance = ingest_budget_management_v1_api.IngestBudgetManagementV1Api(api_client)
    id = "id_example" # str | Identifier of ingest budget to which Collectors are assigned.
    limit = 100 # int | Limit the number of Collectors returned in the response. The number of Collectors returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of Collectors.
        api_response = api_instance.get_assigned_collectors(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV1Api->get_assigned_collectors: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of Collectors.
        api_response = api_instance.get_assigned_collectors(id, limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV1Api->get_assigned_collectors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of ingest budget to which Collectors are assigned. |
 **limit** | **int**| Limit the number of Collectors returned in the response. The number of Collectors returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. | [optional]

### Return type

[**ListCollectorIdentitiesResponse**](ListCollectorIdentitiesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Collectors. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingest_budget**
> IngestBudget get_ingest_budget(id)

Get an ingest budget.

Get an ingest budget by the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v1_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.ingest_budget import IngestBudget
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
    api_instance = ingest_budget_management_v1_api.IngestBudgetManagementV1Api(api_client)
    id = "id_example" # str | Identifier of ingest budget to return.

    # example passing only required values which don't have defaults set
    try:
        # Get an ingest budget.
        api_response = api_instance.get_ingest_budget(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV1Api->get_ingest_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of ingest budget to return. |

### Return type

[**IngestBudget**](IngestBudget.md)

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

# **list_ingest_budgets**
> ListIngestBudgetsResponse list_ingest_budgets()

Get a list of ingest budgets.

Get a list of all ingest budgets. The response is paginated with a default limit of 100 budgets per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v1_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_ingest_budgets_response import ListIngestBudgetsResponse
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
    api_instance = ingest_budget_management_v1_api.IngestBudgetManagementV1Api(api_client)
    limit = 100 # int | Limit the number of budgets returned in the response. The number of budgets returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of ingest budgets.
        api_response = api_instance.list_ingest_budgets(limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV1Api->list_ingest_budgets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of budgets returned in the response. The number of budgets returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. | [optional]

### Return type

[**ListIngestBudgetsResponse**](ListIngestBudgetsResponse.md)

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

# **remove_collector_from_budget**
> IngestBudget remove_collector_from_budget(id, collector_id)

Remove Collector from a budget.

Remove Collector from a budget.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v1_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.ingest_budget import IngestBudget
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
    api_instance = ingest_budget_management_v1_api.IngestBudgetManagementV1Api(api_client)
    id = "id_example" # str | Identifier of the ingest budget to unassign from the Collector.
    collector_id = "collectorId_example" # str | Identifier of the Collector to unassign.

    # example passing only required values which don't have defaults set
    try:
        # Remove Collector from a budget.
        api_response = api_instance.remove_collector_from_budget(id, collector_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV1Api->remove_collector_from_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the ingest budget to unassign from the Collector. |
 **collector_id** | **str**| Identifier of the Collector to unassign. |

### Return type

[**IngestBudget**](IngestBudget.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collector was successfully unassigned from the ingest budget. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_usage**
> reset_usage(id)

Reset usage.

Reset ingest budget's current usage to 0 before the scheduled reset time.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v1_api
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
    api_instance = ingest_budget_management_v1_api.IngestBudgetManagementV1Api(api_client)
    id = "id_example" # str | Identifier of the ingest budget to reset usage.

    # example passing only required values which don't have defaults set
    try:
        # Reset usage.
        api_instance.reset_usage(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV1Api->reset_usage: %s\n" % e)
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

# **update_ingest_budget**
> IngestBudget update_ingest_budget(id, ingest_budget_definition)

Update an ingest budget.

Update an existing ingest budget. All properties specified in the request are required.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import ingest_budget_management_v1_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.ingest_budget_definition import IngestBudgetDefinition
from sumologic_client.model.ingest_budget import IngestBudget
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
    api_instance = ingest_budget_management_v1_api.IngestBudgetManagementV1Api(api_client)
    id = "id_example" # str | Identifier of the ingest budget to update.
    ingest_budget_definition = IngestBudgetDefinition(
        name="Developer Budget",
        field_value="dev_30_gb",
        capacity_bytes=1000,
        timezone="America/Los_Angeles",
        reset_time="23:30",
        description="description_example",
        action="stopCollecting",
        audit_threshold=85,
    ) # IngestBudgetDefinition | Information to update about the ingest budget.

    # example passing only required values which don't have defaults set
    try:
        # Update an ingest budget.
        api_response = api_instance.update_ingest_budget(id, ingest_budget_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling IngestBudgetManagementV1Api->update_ingest_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the ingest budget to update. |
 **ingest_budget_definition** | [**IngestBudgetDefinition**](IngestBudgetDefinition.md)| Information to update about the ingest budget. |

### Return type

[**IngestBudget**](IngestBudget.md)

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


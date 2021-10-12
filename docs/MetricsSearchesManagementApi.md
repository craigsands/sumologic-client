# sumologic_client.MetricsSearchesManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metrics_search**](MetricsSearchesManagementApi.md#create_metrics_search) | **POST** /v1/metricsSearches | Save a metrics search.
[**delete_metrics_search**](MetricsSearchesManagementApi.md#delete_metrics_search) | **DELETE** /v1/metricsSearches/{id} | Deletes a metrics search.
[**get_metrics_search**](MetricsSearchesManagementApi.md#get_metrics_search) | **GET** /v1/metricsSearches/{id} | Get a metrics search.
[**update_metrics_search**](MetricsSearchesManagementApi.md#update_metrics_search) | **PUT** /v1/metricsSearches/{id} | Updates a metrics search.


# **create_metrics_search**
> MetricsSearchInstance create_metrics_search(save_metrics_search_request)

Save a metrics search.

Saves a metrics search in the content library. Metrics search consists of one or more queries, a time range, a quantization period and a set of chart properties like line width.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import metrics_searches_management_api
from sumologic_client.model.metrics_search_instance import MetricsSearchInstance
from sumologic_client.model.save_metrics_search_request import SaveMetricsSearchRequest
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
    api_instance = metrics_searches_management_api.MetricsSearchesManagementApi(api_client)
    save_metrics_search_request = SaveMetricsSearchRequest() # SaveMetricsSearchRequest | The definition of the metrics search.

    # example passing only required values which don't have defaults set
    try:
        # Save a metrics search.
        api_response = api_instance.create_metrics_search(save_metrics_search_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MetricsSearchesManagementApi->create_metrics_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_metrics_search_request** | [**SaveMetricsSearchRequest**](SaveMetricsSearchRequest.md)| The definition of the metrics search. |

### Return type

[**MetricsSearchInstance**](MetricsSearchInstance.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created metrics search. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metrics_search**
> delete_metrics_search(id)

Deletes a metrics search.

Deletes a metrics search from the content library.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import metrics_searches_management_api
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
    api_instance = metrics_searches_management_api.MetricsSearchesManagementApi(api_client)
    id = "id_example" # str | Identifier of the metrics search.

    # example passing only required values which don't have defaults set
    try:
        # Deletes a metrics search.
        api_instance.delete_metrics_search(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling MetricsSearchesManagementApi->delete_metrics_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the metrics search. |

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
**204** | The metrics search was successfully deleted. |  -  |
**0** | The operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_search**
> MetricsSearchInstance get_metrics_search(id)

Get a metrics search.

Returns a metrics search with the specified identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import metrics_searches_management_api
from sumologic_client.model.metrics_search_instance import MetricsSearchInstance
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
    api_instance = metrics_searches_management_api.MetricsSearchesManagementApi(api_client)
    id = "id_example" # str | Identifier of the metrics search.

    # example passing only required values which don't have defaults set
    try:
        # Get a metrics search.
        api_response = api_instance.get_metrics_search(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MetricsSearchesManagementApi->get_metrics_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the metrics search. |

### Return type

[**MetricsSearchInstance**](MetricsSearchInstance.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A metrics search object with metadata. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metrics_search**
> MetricsSearchInstance update_metrics_search(id, metrics_search_v1)

Updates a metrics search.

Updates a metrics search with the specified identifier. Partial updates are not supported, you must provide values for all fields.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import metrics_searches_management_api
from sumologic_client.model.metrics_search_instance import MetricsSearchInstance
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.metrics_search_v1 import MetricsSearchV1
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
    api_instance = metrics_searches_management_api.MetricsSearchesManagementApi(api_client)
    id = "id_example" # str | Identifier of the metrics search.
    metrics_search_v1 = MetricsSearchV1(
        title="Short title",
        description="Long and detailed description",
        time_range=ResolvableTimeRange(),
        log_query="my_metric | timeslice 1m | count by _timeslice",
        metrics_queries=[
            MetricsSearchQuery(
                row_id="A",
                query="my_metric | avg",
            ),
        ],
        desired_quantization_in_secs=60,
        properties="{ \"key\": \"value\" }",
    ) # MetricsSearchV1 | An updated metrics search definition.

    # example passing only required values which don't have defaults set
    try:
        # Updates a metrics search.
        api_response = api_instance.update_metrics_search(id, metrics_search_v1)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MetricsSearchesManagementApi->update_metrics_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the metrics search. |
 **metrics_search_v1** | [**MetricsSearchV1**](MetricsSearchV1.md)| An updated metrics search definition. |

### Return type

[**MetricsSearchInstance**](MetricsSearchInstance.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metrics saved search that was updated. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


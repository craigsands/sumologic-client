# sumologic_client.MetricsQueryApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_metrics_queries**](MetricsQueryApi.md#run_metrics_queries) | **POST** /v1/metricsQueries | Run metrics queries


# **run_metrics_queries**
> MetricsQueryResponse run_metrics_queries(metrics_query_request)

Run metrics queries

Execute up to six metrics queries. If you specify multiple queries, each is returned as a separate set of time series. For more information see [Metrics Queries](https://help.sumologic.com/?cid=10144).

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import metrics_query_api
from sumologic_client.model.metrics_query_response import MetricsQueryResponse
from sumologic_client.model.metrics_query_request import MetricsQueryRequest
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
    api_instance = metrics_query_api.MetricsQueryApi(api_client)
    metrics_query_request = MetricsQueryRequest(
        queries=[
            MetricsQueryRow(
                row_id="A",
                query="metric=CPU_Idle",
                quantization=60000,
                rollup="Avg",
                timeshift=-3600000,
                transient=True,
            ),
        ],
        time_range=ResolvableTimeRange(),
    ) # MetricsQueryRequest | The parameters for the metrics query.

    # example passing only required values which don't have defaults set
    try:
        # Run metrics queries
        api_response = api_instance.run_metrics_queries(metrics_query_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling MetricsQueryApi->run_metrics_queries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics_query_request** | [**MetricsQueryRequest**](MetricsQueryRequest.md)| The parameters for the metrics query. |

### Return type

[**MetricsQueryResponse**](MetricsQueryResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A set of time series grouped by the query. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


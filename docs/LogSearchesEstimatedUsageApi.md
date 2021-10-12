# sumologic_client.LogSearchesEstimatedUsageApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_search_estimated_usage**](LogSearchesEstimatedUsageApi.md#get_log_search_estimated_usage) | **POST** /v1/logSearches/estimatedUsage | Gets estimated usage details.
[**get_log_search_estimated_usage_by_tier**](LogSearchesEstimatedUsageApi.md#get_log_search_estimated_usage_by_tier) | **POST** /v1/logSearches/estimatedUsageByTier | Gets Tier Wise estimated usage details.


# **get_log_search_estimated_usage**
> LogSearchEstimatedUsageDefinition get_log_search_estimated_usage(log_search_estimated_usage_request)

Gets estimated usage details.

Gets the estimated volume of data that would be scanned for a given log search in the Infrequent data tier. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import log_searches_estimated_usage_api
from sumologic_client.model.log_search_estimated_usage_definition import LogSearchEstimatedUsageDefinition
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.log_search_estimated_usage_request import LogSearchEstimatedUsageRequest
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
    api_instance = log_searches_estimated_usage_api.LogSearchesEstimatedUsageApi(api_client)
    log_search_estimated_usage_request = LogSearchEstimatedUsageRequest() # LogSearchEstimatedUsageRequest | The definition of the log search estimated usage.

    # example passing only required values which don't have defaults set
    try:
        # Gets estimated usage details.
        api_response = api_instance.get_log_search_estimated_usage(log_search_estimated_usage_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling LogSearchesEstimatedUsageApi->get_log_search_estimated_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_search_estimated_usage_request** | [**LogSearchEstimatedUsageRequest**](LogSearchEstimatedUsageRequest.md)| The definition of the log search estimated usage. |

### Return type

[**LogSearchEstimatedUsageDefinition**](LogSearchEstimatedUsageDefinition.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Log search information along with its estimated usage details. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_search_estimated_usage_by_tier**
> LogSearchEstimatedUsageByTierDefinition get_log_search_estimated_usage_by_tier(log_search_estimated_usage_request_v2)

Gets Tier Wise estimated usage details.

Gets the estimated volume of data that would be scanned for a given log search per data tier. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import log_searches_estimated_usage_api
from sumologic_client.model.log_search_estimated_usage_request_v2 import LogSearchEstimatedUsageRequestV2
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.log_search_estimated_usage_by_tier_definition import LogSearchEstimatedUsageByTierDefinition
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
    api_instance = log_searches_estimated_usage_api.LogSearchesEstimatedUsageApi(api_client)
    log_search_estimated_usage_request_v2 = LogSearchEstimatedUsageRequestV2() # LogSearchEstimatedUsageRequestV2 | The definition of the log search estimated usage.

    # example passing only required values which don't have defaults set
    try:
        # Gets Tier Wise estimated usage details.
        api_response = api_instance.get_log_search_estimated_usage_by_tier(log_search_estimated_usage_request_v2)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling LogSearchesEstimatedUsageApi->get_log_search_estimated_usage_by_tier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_search_estimated_usage_request_v2** | [**LogSearchEstimatedUsageRequestV2**](LogSearchEstimatedUsageRequestV2.md)| The definition of the log search estimated usage. |

### Return type

[**LogSearchEstimatedUsageByTierDefinition**](LogSearchEstimatedUsageByTierDefinition.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Log search information along with its tier wise estimated usage details. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


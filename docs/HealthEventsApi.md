# sumologic_client.HealthEventsApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_all_health_events**](HealthEventsApi.md#list_all_health_events) | **GET** /v1/healthEvents | Get a list of health events.
[**list_all_health_events_for_resources**](HealthEventsApi.md#list_all_health_events_for_resources) | **POST** /v1/healthEvents/resources | Health events for specific resources.


# **list_all_health_events**
> ListHealthEventResponse list_all_health_events()

Get a list of health events.

Get a list of all the unresolved health events in your account.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import health_events_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_health_event_response import ListHealthEventResponse
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
    api_instance = health_events_api.HealthEventsApi(api_client)
    limit = 100 # int | Limit the number of health events returned in the response. The number of health events returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. `token` is set to null when no more pages are left. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of health events.
        api_response = api_instance.list_all_health_events(limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling HealthEventsApi->list_all_health_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of health events returned in the response. The number of health events returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. &#x60;token&#x60; is set to null when no more pages are left. | [optional]

### Return type

[**ListHealthEventResponse**](ListHealthEventResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of all the health events. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_health_events_for_resources**
> ListHealthEventResponse list_all_health_events_for_resources(resource_identities)

Health events for specific resources.

Get a list of all the unresolved events in your account that belong to the supplied resource identifiers.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import health_events_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.resource_identities import ResourceIdentities
from sumologic_client.model.list_health_event_response import ListHealthEventResponse
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
    api_instance = health_events_api.HealthEventsApi(api_client)
    resource_identities = ResourceIdentities(
        data=[
            ResourceIdentity(),
        ],
    ) # ResourceIdentities | Resource identifiers to request health events from.
    limit = 100 # int | Limit the number of health events returned in the response. The number of health events returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. `token` is set to null when no more pages are left. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Health events for specific resources.
        api_response = api_instance.list_all_health_events_for_resources(resource_identities)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling HealthEventsApi->list_all_health_events_for_resources: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Health events for specific resources.
        api_response = api_instance.list_all_health_events_for_resources(resource_identities, limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling HealthEventsApi->list_all_health_events_for_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_identities** | [**ResourceIdentities**](ResourceIdentities.md)| Resource identifiers to request health events from. |
 **limit** | **int**| Limit the number of health events returned in the response. The number of health events returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. &#x60;token&#x60; is set to null when no more pages are left. | [optional]

### Return type

[**ListHealthEventResponse**](ListHealthEventResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all the health events for the specified resources. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


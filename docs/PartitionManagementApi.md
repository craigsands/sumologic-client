# sumologic_client.PartitionManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_retention_update**](PartitionManagementApi.md#cancel_retention_update) | **POST** /v1/partitions/{id}/cancelRetentionUpdate | Cancel a retention update for a partition
[**create_partition**](PartitionManagementApi.md#create_partition) | **POST** /v1/partitions | Create a new partition.
[**decommission_partition**](PartitionManagementApi.md#decommission_partition) | **POST** /v1/partitions/{id}/decommission | Decommission a partition.
[**get_partition**](PartitionManagementApi.md#get_partition) | **GET** /v1/partitions/{id} | Get a partition.
[**list_partitions**](PartitionManagementApi.md#list_partitions) | **GET** /v1/partitions | Get a list of partitions.
[**update_partition**](PartitionManagementApi.md#update_partition) | **PUT** /v1/partitions/{id} | Update a partition.


# **cancel_retention_update**
> cancel_retention_update(id)

Cancel a retention update for a partition

Cancel update to retention of a partition for which retention was updated previously using `reduceRetentionPeriodImmediately` parameter as false

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import partition_management_api
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
    api_instance = partition_management_api.PartitionManagementApi(api_client)
    id = "1" # str | Identifier of the partition to cancel the retention update for.

    # example passing only required values which don't have defaults set
    try:
        # Cancel a retention update for a partition
        api_instance.cancel_retention_update(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling PartitionManagementApi->cancel_retention_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the partition to cancel the retention update for. |

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
**204** | The retention update was cancelled successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_partition**
> Partition create_partition(create_partition_definition)

Create a new partition.

Create a new partition.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import partition_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.partition import Partition
from sumologic_client.model.create_partition_definition import CreatePartitionDefinition
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
    api_instance = partition_management_api.PartitionManagementApi(api_client)
    create_partition_definition = CreatePartitionDefinition(
        name="apache",
        routing_expression="_sourcecategory=*/Apache",
        analytics_tier="continuous",
        retention_period=365,
        is_compliant=False,
    ) # CreatePartitionDefinition | Information about the new partition.

    # example passing only required values which don't have defaults set
    try:
        # Create a new partition.
        api_response = api_instance.create_partition(create_partition_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PartitionManagementApi->create_partition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_partition_definition** | [**CreatePartitionDefinition**](CreatePartitionDefinition.md)| Information about the new partition. |

### Return type

[**Partition**](Partition.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partition has been created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decommission_partition**
> decommission_partition(id)

Decommission a partition.

Decommission a partition with the given identifier from the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import partition_management_api
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
    api_instance = partition_management_api.PartitionManagementApi(api_client)
    id = "id_example" # str | Identifier of the partition to decommission.

    # example passing only required values which don't have defaults set
    try:
        # Decommission a partition.
        api_instance.decommission_partition(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling PartitionManagementApi->decommission_partition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the partition to decommission. |

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
**200** | The partition was decommissioned successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partition**
> Partition get_partition(id)

Get a partition.

Get a partition with the given identifier from the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import partition_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.partition import Partition
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
    api_instance = partition_management_api.PartitionManagementApi(api_client)
    id = "id_example" # str | Identifier of partition to return.

    # example passing only required values which don't have defaults set
    try:
        # Get a partition.
        api_response = api_instance.get_partition(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PartitionManagementApi->get_partition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of partition to return. |

### Return type

[**Partition**](Partition.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Partition object that was requested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_partitions**
> ListPartitionsResponse list_partitions()

Get a list of partitions.

Get a list of all partitions in the organization. The response is paginated with a default limit of 100 partitions per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import partition_management_api
from sumologic_client.model.list_partitions_response import ListPartitionsResponse
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
    api_instance = partition_management_api.PartitionManagementApi(api_client)
    limit = 100 # int | Limit the number of partitions returned in the response. The number of partitions returned may be less than the `limit`. (optional) if omitted the server will use the default value of 100
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. `token` is set to null when no more pages are left. (optional)
    view_types = ["AuditIndex","Partition"] # [str] | The type of partitions to retrieve. Valid values are:   1. `DefaultView`: To get General Index partition.   2. `Partition`: To get user defined views/partitions.   3. `AuditIndex`: To get the internal audit indexes. Eg. sumologic_audit_events.  More than one type of partitions can be retrieved in same request. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of partitions.
        api_response = api_instance.list_partitions(limit=limit, token=token, view_types=view_types)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PartitionManagementApi->list_partitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of partitions returned in the response. The number of partitions returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 100
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. &#x60;token&#x60; is set to null when no more pages are left. | [optional]
 **view_types** | **[str]**| The type of partitions to retrieve. Valid values are:   1. &#x60;DefaultView&#x60;: To get General Index partition.   2. &#x60;Partition&#x60;: To get user defined views/partitions.   3. &#x60;AuditIndex&#x60;: To get the internal audit indexes. Eg. sumologic_audit_events.  More than one type of partitions can be retrieved in same request. | [optional]

### Return type

[**ListPartitionsResponse**](ListPartitionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of partitions in the organization. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_partition**
> Partition update_partition(id, update_partition_definition)

Update a partition.

Update an existing partition in the organization.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import partition_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.update_partition_definition import UpdatePartitionDefinition
from sumologic_client.model.partition import Partition
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
    api_instance = partition_management_api.PartitionManagementApi(api_client)
    id = "id_example" # str | Identifier of the partition to update.
    update_partition_definition = UpdatePartitionDefinition(
        retention_period=365,
        reduce_retention_period_immediately=False,
        is_compliant=False,
        routing_expression="_sourcecategory=*/Apache",
    ) # UpdatePartitionDefinition | Information to update about the partition.

    # example passing only required values which don't have defaults set
    try:
        # Update a partition.
        api_response = api_instance.update_partition(id, update_partition_definition)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PartitionManagementApi->update_partition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the partition to update. |
 **update_partition_definition** | [**UpdatePartitionDefinition**](UpdatePartitionDefinition.md)| Information to update about the partition. |

### Return type

[**Partition**](Partition.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partition was successfully modified. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# sumologic_client.ArchiveManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_archive_job**](ArchiveManagementApi.md#create_archive_job) | **POST** /v1/archive/{sourceId}/jobs | Create an ingestion job.
[**delete_archive_job**](ArchiveManagementApi.md#delete_archive_job) | **DELETE** /v1/archive/{sourceId}/jobs/{id} | Delete an ingestion job.
[**list_archive_jobs_by_source_id**](ArchiveManagementApi.md#list_archive_jobs_by_source_id) | **GET** /v1/archive/{sourceId}/jobs | Get ingestion jobs for an Archive Source.
[**list_archive_jobs_count_per_source**](ArchiveManagementApi.md#list_archive_jobs_count_per_source) | **GET** /v1/archive/jobs/count | List ingestion jobs for all Archive Sources.


# **create_archive_job**
> ArchiveJob create_archive_job(source_id, create_archive_job_request)

Create an ingestion job.

Create an ingestion job to pull data from your S3 bucket.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import archive_management_api
from sumologic_client.model.create_archive_job_request import CreateArchiveJobRequest
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.archive_job import ArchiveJob
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
    api_instance = archive_management_api.ArchiveManagementApi(api_client)
    source_id = "000000000606C009" # str | The identifier of the Archive Source for which the job is to be added.
    create_archive_job_request = CreateArchiveJobRequest(
        name="name_example",
        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # CreateArchiveJobRequest | The definition of the ingestion job to create.

    # example passing only required values which don't have defaults set
    try:
        # Create an ingestion job.
        api_response = api_instance.create_archive_job(source_id, create_archive_job_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ArchiveManagementApi->create_archive_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The identifier of the Archive Source for which the job is to be added. |
 **create_archive_job_request** | [**CreateArchiveJobRequest**](CreateArchiveJobRequest.md)| The definition of the ingestion job to create. |

### Return type

[**ArchiveJob**](ArchiveJob.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ingestion job was created successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_archive_job**
> delete_archive_job(source_id, id)

Delete an ingestion job.

Delete an ingestion job with the given identifier from the organization. The delete operation is only possible for jobs with a Succeeded or Failed status.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import archive_management_api
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
    api_instance = archive_management_api.ArchiveManagementApi(api_client)
    source_id = "sourceId_example" # str | The identifier of the Archive Source.
    id = "id_example" # str | The identifier of the ingestion job to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete an ingestion job.
        api_instance.delete_archive_job(source_id, id)
    except sumologic_client.ApiException as e:
        print("Exception when calling ArchiveManagementApi->delete_archive_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The identifier of the Archive Source. |
 **id** | **str**| The identifier of the ingestion job to delete. |

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
**204** | The ingestion job was deleted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_archive_jobs_by_source_id**
> ListArchiveJobsResponse list_archive_jobs_by_source_id(source_id)

Get ingestion jobs for an Archive Source.

Get a list of all the ingestion jobs created on an Archive Source. The response is paginated with a default limit of 10 jobs per page.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import archive_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_archive_jobs_response import ListArchiveJobsResponse
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
    api_instance = archive_management_api.ArchiveManagementApi(api_client)
    source_id = "000000000606C009" # str | The identifier of an Archive Source.
    limit = 10 # int | Limit the number of jobs returned in the response. The number of jobs returned may be less than the `limit`. (optional) if omitted the server will use the default value of 10
    token = "token_example" # str | Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. `token` is set to null when no more pages are left. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get ingestion jobs for an Archive Source.
        api_response = api_instance.list_archive_jobs_by_source_id(source_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ArchiveManagementApi->list_archive_jobs_by_source_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get ingestion jobs for an Archive Source.
        api_response = api_instance.list_archive_jobs_by_source_id(source_id, limit=limit, token=token)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ArchiveManagementApi->list_archive_jobs_by_source_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The identifier of an Archive Source. |
 **limit** | **int**| Limit the number of jobs returned in the response. The number of jobs returned may be less than the &#x60;limit&#x60;. | [optional] if omitted the server will use the default value of 10
 **token** | **str**| Continuation token to get the next page of results. A page object with the next continuation token is returned in the response body. Subsequent GET requests should specify the continuation token to get the next page of results. &#x60;token&#x60; is set to null when no more pages are left. | [optional]

### Return type

[**ListArchiveJobsResponse**](ListArchiveJobsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of ingestion jobs for an Archive Source. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_archive_jobs_count_per_source**
> ListArchiveJobsCount list_archive_jobs_count_per_source()

List ingestion jobs for all Archive Sources.

Get a list of all Archive Sources with the count and status of ingestion jobs.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import archive_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.list_archive_jobs_count import ListArchiveJobsCount
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
    api_instance = archive_management_api.ArchiveManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List ingestion jobs for all Archive Sources.
        api_response = api_instance.list_archive_jobs_count_per_source()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling ArchiveManagementApi->list_archive_jobs_count_per_source: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListArchiveJobsCount**](ListArchiveJobsCount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Archive Sources with ingestion jobs. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


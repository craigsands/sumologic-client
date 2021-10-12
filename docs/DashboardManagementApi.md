# sumologic_client.DashboardManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](DashboardManagementApi.md#create_dashboard) | **POST** /v2/dashboards | Create a new dashboard.
[**delete_dashboard**](DashboardManagementApi.md#delete_dashboard) | **DELETE** /v2/dashboards/{id} | Delete a dashboard.
[**generate_dashboard_report**](DashboardManagementApi.md#generate_dashboard_report) | **POST** /v2/dashboards/reportJobs | Start a report job
[**get_async_report_generation_result**](DashboardManagementApi.md#get_async_report_generation_result) | **GET** /v2/dashboards/reportJobs/{jobId}/result | Get report generation job result
[**get_async_report_generation_status**](DashboardManagementApi.md#get_async_report_generation_status) | **GET** /v2/dashboards/reportJobs/{jobId}/status | Get report generation job status
[**get_dashboard**](DashboardManagementApi.md#get_dashboard) | **GET** /v2/dashboards/{id} | Get a dashboard.
[**update_dashboard**](DashboardManagementApi.md#update_dashboard) | **PUT** /v2/dashboards/{id} | Update a dashboard.


# **create_dashboard**
> Dashboard create_dashboard(dashboard_request)

Create a new dashboard.

Creates a new dashboard.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dashboard_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.dashboard import Dashboard
from sumologic_client.model.dashboard_request import DashboardRequest
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
    api_instance = dashboard_management_api.DashboardManagementApi(api_client)
    dashboard_request = DashboardRequest(
        title="Kubernetes Dashboard",
        description="A view of pods, namespaces and nodes of your cluster.",
        folder_id="000000000C1C17C6",
        topology_label_map=TopologyLabelMap(
            data={
                "key": TopologyLabelValuesList([
                    "kube-scheduler",
                ]),
            },
        ),
        domain="aws",
        refresh_interval=30,
        time_range=ResolvableTimeRange(),
        panels=[
            Panel(),
        ],
        layout=Layout(),
        variables=[
            Variable(
                id="id_example",
                name="_sourceHost",
                display_name="Source Host",
                default_value="default_value",
                source_definition=VariableSourceDefinition(),
                allow_multi_select=False,
                include_all_option=True,
                hide_from_ui=False,
                value_type="Any",
            ),
        ],
        theme="light",
    ) # DashboardRequest | Information to create the new dashboard.

    # example passing only required values which don't have defaults set
    try:
        # Create a new dashboard.
        api_response = api_instance.create_dashboard(dashboard_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling DashboardManagementApi->create_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_request** | [**DashboardRequest**](DashboardRequest.md)| Information to create the new dashboard. |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dashboard has been created. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> delete_dashboard(id)

Delete a dashboard.

Delete a dashboard by the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dashboard_management_api
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
    api_instance = dashboard_management_api.DashboardManagementApi(api_client)
    id = "id_example" # str | Identifier of the dashboard to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a dashboard.
        api_instance.delete_dashboard(id)
    except sumologic_client.ApiException as e:
        print("Exception when calling DashboardManagementApi->delete_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the dashboard to delete. |

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
**204** | Dashboard was deleted successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_dashboard_report**
> BeginAsyncJobResponse generate_dashboard_report(generate_report_request)

Start a report job

Schedule an asynchronous job to generate a report from a template. All items in the template will be included unless specified. See template section for more details on individual templates. Reports can be generated in Pdf or Png format and exported in various methods (ex. direct download). You will get back an asynchronous job identifier on success. Use the [getAsyncReportGenerationStatus](#operation/getAsyncExportStatus) endpoint and the job identifier you got back in the response to track the status of an asynchronous report generation job. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dashboard_management_api
from sumologic_client.model.generate_report_request import GenerateReportRequest
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.begin_async_job_response import BeginAsyncJobResponse
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
    api_instance = dashboard_management_api.DashboardManagementApi(api_client)
    generate_report_request = GenerateReportRequest(
        action=ReportAction(),
        export_format="Pdf",
        timezone="America/Los_Angeles",
        template=Template(),
    ) # GenerateReportRequest | Request for a report.

    # example passing only required values which don't have defaults set
    try:
        # Start a report job
        api_response = api_instance.generate_dashboard_report(generate_report_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling DashboardManagementApi->generate_dashboard_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_report_request** | [**GenerateReportRequest**](GenerateReportRequest.md)| Request for a report. |

### Return type

[**BeginAsyncJobResponse**](BeginAsyncJobResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export job has been scheduled. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_report_generation_result**
> file_type get_async_report_generation_result(job_id)

Get report generation job result

Get the result of an asynchronous report generation request for the given job identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dashboard_management_api
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
    api_instance = dashboard_management_api.DashboardManagementApi(api_client)
    job_id = "jobId_example" # str | The identifier of the asynchronous report generation job.

    # example passing only required values which don't have defaults set
    try:
        # Get report generation job result
        api_response = api_instance.get_async_report_generation_result(job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling DashboardManagementApi->get_async_report_generation_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The identifier of the asynchronous report generation job. |

### Return type

**file_type**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, image/png, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of export job. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_report_generation_status**
> AsyncJobStatus get_async_report_generation_status(job_id)

Get report generation job status

Get the status of an asynchronous report generation request for the given job identifier. On success, use the [getReportGenerationResult](#operation/getAsyncReportGenerationResult) endpoint to get the result of the report generation job.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dashboard_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.async_job_status import AsyncJobStatus
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
    api_instance = dashboard_management_api.DashboardManagementApi(api_client)
    job_id = "jobId_example" # str | The identifier of the asynchronous report generation job.

    # example passing only required values which don't have defaults set
    try:
        # Get report generation job status
        api_response = api_instance.get_async_report_generation_status(job_id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling DashboardManagementApi->get_async_report_generation_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The identifier of the asynchronous report generation job. |

### Return type

[**AsyncJobStatus**](AsyncJobStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of the report generation job. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard**
> Dashboard get_dashboard(id)

Get a dashboard.

Get a dashboard by the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dashboard_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.dashboard import Dashboard
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
    api_instance = dashboard_management_api.DashboardManagementApi(api_client)
    id = "id_example" # str | UUID of the dashboard to return.

    # example passing only required values which don't have defaults set
    try:
        # Get a dashboard.
        api_response = api_instance.get_dashboard(id)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling DashboardManagementApi->get_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID of the dashboard to return. |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard object that was requested. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> Dashboard update_dashboard(id, dashboard_request)

Update a dashboard.

Update a dashboard by the given identifier.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import dashboard_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.dashboard import Dashboard
from sumologic_client.model.dashboard_request import DashboardRequest
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
    api_instance = dashboard_management_api.DashboardManagementApi(api_client)
    id = "id_example" # str | Identifier of the dashboard to update.
    dashboard_request = DashboardRequest(
        title="Kubernetes Dashboard",
        description="A view of pods, namespaces and nodes of your cluster.",
        folder_id="000000000C1C17C6",
        topology_label_map=TopologyLabelMap(
            data={
                "key": TopologyLabelValuesList([
                    "kube-scheduler",
                ]),
            },
        ),
        domain="aws",
        refresh_interval=30,
        time_range=ResolvableTimeRange(),
        panels=[
            Panel(),
        ],
        layout=Layout(),
        variables=[
            Variable(
                id="id_example",
                name="_sourceHost",
                display_name="Source Host",
                default_value="default_value",
                source_definition=VariableSourceDefinition(),
                allow_multi_select=False,
                include_all_option=True,
                hide_from_ui=False,
                value_type="Any",
            ),
        ],
        theme="light",
    ) # DashboardRequest | Information to update on the dashboard.

    # example passing only required values which don't have defaults set
    try:
        # Update a dashboard.
        api_response = api_instance.update_dashboard(id, dashboard_request)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling DashboardManagementApi->update_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the dashboard to update. |
 **dashboard_request** | [**DashboardRequest**](DashboardRequest.md)| Information to update on the dashboard. |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dashboard was successfully modified. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


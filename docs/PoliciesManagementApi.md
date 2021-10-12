# sumologic_client.PoliciesManagementApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_policy**](PoliciesManagementApi.md#get_audit_policy) | **GET** /v1/policies/audit | Get Audit policy.
[**get_data_access_level_policy**](PoliciesManagementApi.md#get_data_access_level_policy) | **GET** /v1/policies/dataAccessLevel | Get Data Access Level policy.
[**get_max_user_session_timeout_policy**](PoliciesManagementApi.md#get_max_user_session_timeout_policy) | **GET** /v1/policies/maxUserSessionTimeout | Get Max User Session Timeout policy.
[**get_search_audit_policy**](PoliciesManagementApi.md#get_search_audit_policy) | **GET** /v1/policies/searchAudit | Get Search Audit policy.
[**get_share_dashboards_outside_organization_policy**](PoliciesManagementApi.md#get_share_dashboards_outside_organization_policy) | **GET** /v1/policies/shareDashboardsOutsideOrganization | Get Share Dashboards Outside Organization policy.
[**get_user_concurrent_sessions_limit_policy**](PoliciesManagementApi.md#get_user_concurrent_sessions_limit_policy) | **GET** /v1/policies/userConcurrentSessionsLimit | Get User Concurrent Sessions Limit policy.
[**set_audit_policy**](PoliciesManagementApi.md#set_audit_policy) | **PUT** /v1/policies/audit | Set Audit policy.
[**set_data_access_level_policy**](PoliciesManagementApi.md#set_data_access_level_policy) | **PUT** /v1/policies/dataAccessLevel | Set Data Access Level policy.
[**set_max_user_session_timeout_policy**](PoliciesManagementApi.md#set_max_user_session_timeout_policy) | **PUT** /v1/policies/maxUserSessionTimeout | Set Max User Session Timeout policy.
[**set_search_audit_policy**](PoliciesManagementApi.md#set_search_audit_policy) | **PUT** /v1/policies/searchAudit | Set Search Audit policy.
[**set_share_dashboards_outside_organization_policy**](PoliciesManagementApi.md#set_share_dashboards_outside_organization_policy) | **PUT** /v1/policies/shareDashboardsOutsideOrganization | Set Share Dashboards Outside Organization policy.
[**set_user_concurrent_sessions_limit_policy**](PoliciesManagementApi.md#set_user_concurrent_sessions_limit_policy) | **PUT** /v1/policies/userConcurrentSessionsLimit | Set User Concurrent Sessions Limit policy.


# **get_audit_policy**
> AuditPolicy get_audit_policy()

Get Audit policy.

Get the Audit policy. This policy specifies whether audit records for your account are enabled. You can access details about reported account events in the Sumo Logic Audit Index. [Learn More](https://help.sumologic.com/Manage/Security/Audit-Index)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.audit_policy import AuditPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Audit policy.
        api_response = api_instance.get_audit_policy()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->get_audit_policy: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditPolicy**](AuditPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Audit policy. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_access_level_policy**
> DataAccessLevelPolicy get_data_access_level_policy()

Get Data Access Level policy.

Get the Data Access Level policy. When enabled, this policy sets the default data access level for all newly created dashboards to the viewer’s role access filter. Otherwise, newly created dashboards will default to the sharer’s role access filter and might display data that viewers’ roles don’t allow them to view. [Learn More](https://help.sumologic.com/Manage/Security/Data_Access_Level_for_Shared_Dashboards)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.data_access_level_policy import DataAccessLevelPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Data Access Level policy.
        api_response = api_instance.get_data_access_level_policy()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->get_data_access_level_policy: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DataAccessLevelPolicy**](DataAccessLevelPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Data Access Level policy. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_max_user_session_timeout_policy**
> MaxUserSessionTimeoutPolicy get_max_user_session_timeout_policy()

Get Max User Session Timeout policy.

Get the Max User Session Timeout policy. When enabled, this policy sets the maximum web session timeout users are able to configure within their user preferences. Users preferences will be updated to match this value only if their current preference is set to a higher value. [Learn More](https://help.sumologic.com/Manage/Security/Set_a_Maximum_Web_Session_Timeout)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.max_user_session_timeout_policy import MaxUserSessionTimeoutPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Max User Session Timeout policy.
        api_response = api_instance.get_max_user_session_timeout_policy()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->get_max_user_session_timeout_policy: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MaxUserSessionTimeoutPolicy**](MaxUserSessionTimeoutPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Max User Session Timeout policy. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_audit_policy**
> SearchAuditPolicy get_search_audit_policy()

Get Search Audit policy.

Get the Search Audit policy. This policy specifies whether search records for your account are enabled. You can access details about your account's search capacity, queries run by users from the Sumo Search Audit Index. [Learn More](https://help.sumologic.com/Manage/Security/Search_Audit_Index)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.search_audit_policy import SearchAuditPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Search Audit policy.
        api_response = api_instance.get_search_audit_policy()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->get_search_audit_policy: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SearchAuditPolicy**](SearchAuditPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Search Audit policy. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share_dashboards_outside_organization_policy**
> ShareDashboardsOutsideOrganizationPolicy get_share_dashboards_outside_organization_policy()

Get Share Dashboards Outside Organization policy.

Get the Share Dashboards Outside Organization policy. This policy allows users to share the dashboard with view only privileges outside of the organization (capability must be enabled from the Roles page). Disabling this policy will disable all dashboards that have been shared outside of the organization. [Learn More](https://help.sumologic.com/Visualizations-and-Alerts/Dashboards/Share_Dashboards/Share_a_Dashboard_Outside_Your_Org)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.share_dashboards_outside_organization_policy import ShareDashboardsOutsideOrganizationPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Share Dashboards Outside Organization policy.
        api_response = api_instance.get_share_dashboards_outside_organization_policy()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->get_share_dashboards_outside_organization_policy: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ShareDashboardsOutsideOrganizationPolicy**](ShareDashboardsOutsideOrganizationPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Share Dashboards Outside Organization policy. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_concurrent_sessions_limit_policy**
> UserConcurrentSessionsLimitPolicy get_user_concurrent_sessions_limit_policy()

Get User Concurrent Sessions Limit policy.

Get the User Concurrent Sessions Limit policy. When enabled, the number of concurrent sessions a user may have is limited to the value entered. If a user exceeds the allowed number of sessions, the user's oldest session will be logged out to accommodate the new one. Disabling this policy means a user may have an unlimited number of concurrent sessions. [Learn More](https://help.sumologic.com/Manage/Security/Set_a_Limit_for_User_Concurrent_Sessions)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.user_concurrent_sessions_limit_policy import UserConcurrentSessionsLimitPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get User Concurrent Sessions Limit policy.
        api_response = api_instance.get_user_concurrent_sessions_limit_policy()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->get_user_concurrent_sessions_limit_policy: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserConcurrentSessionsLimitPolicy**](UserConcurrentSessionsLimitPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The User Concurrent Sessions Limit policy. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_audit_policy**
> AuditPolicy set_audit_policy(audit_policy)

Set Audit policy.

Set the Audit policy. This policy specifies whether audit records for your account are enabled. You can access details about reported account events in the Sumo Logic Audit Index. [Learn More](https://help.sumologic.com/Manage/Security/Audit-Index)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.audit_policy import AuditPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)
    audit_policy = AuditPolicy(
        enabled=True,
    ) # AuditPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Set Audit policy.
        api_response = api_instance.set_audit_policy(audit_policy)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->set_audit_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_policy** | [**AuditPolicy**](AuditPolicy.md)|  |

### Return type

[**AuditPolicy**](AuditPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit policy was set successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_access_level_policy**
> DataAccessLevelPolicy set_data_access_level_policy(data_access_level_policy)

Set Data Access Level policy.

Set the Data Access Level policy. When enabled, this policy sets the default data access level for all newly created dashboards to the viewer’s role access filter. Otherwise, newly created dashboards will default to the sharer’s role access filter and might display data that viewers’ roles don’t allow them to view. [Learn More](https://help.sumologic.com/Manage/Security/Data_Access_Level_for_Shared_Dashboards)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.data_access_level_policy import DataAccessLevelPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)
    data_access_level_policy = DataAccessLevelPolicy(
        enabled=True,
    ) # DataAccessLevelPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Set Data Access Level policy.
        api_response = api_instance.set_data_access_level_policy(data_access_level_policy)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->set_data_access_level_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_access_level_policy** | [**DataAccessLevelPolicy**](DataAccessLevelPolicy.md)|  |

### Return type

[**DataAccessLevelPolicy**](DataAccessLevelPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data Access Level policy was set successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_max_user_session_timeout_policy**
> MaxUserSessionTimeoutPolicy set_max_user_session_timeout_policy(max_user_session_timeout_policy)

Set Max User Session Timeout policy.

Set the Max User Session Timeout policy. When enabled, this policy sets the maximum web session timeout users are able to configure within their user preferences. Users preferences will be updated to match this value only if their current preference is set to a higher value. [Learn More](https://help.sumologic.com/Manage/Security/Set_a_Maximum_Web_Session_Timeout)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.max_user_session_timeout_policy import MaxUserSessionTimeoutPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)
    max_user_session_timeout_policy = MaxUserSessionTimeoutPolicy(
        max_user_session_timeout="1d",
    ) # MaxUserSessionTimeoutPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Set Max User Session Timeout policy.
        api_response = api_instance.set_max_user_session_timeout_policy(max_user_session_timeout_policy)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->set_max_user_session_timeout_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_user_session_timeout_policy** | [**MaxUserSessionTimeoutPolicy**](MaxUserSessionTimeoutPolicy.md)|  |

### Return type

[**MaxUserSessionTimeoutPolicy**](MaxUserSessionTimeoutPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Max User Session Timeout policy was set successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_search_audit_policy**
> SearchAuditPolicy set_search_audit_policy(search_audit_policy)

Set Search Audit policy.

Set the Search Audit policy. This policy specifies whether search records for your account are enabled. You can access details about your account's search capacity, queries run by users from the Sumo Search Audit Index. [Learn More](https://help.sumologic.com/Manage/Security/Search_Audit_Index)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.search_audit_policy import SearchAuditPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)
    search_audit_policy = SearchAuditPolicy(
        enabled=True,
    ) # SearchAuditPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Set Search Audit policy.
        api_response = api_instance.set_search_audit_policy(search_audit_policy)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->set_search_audit_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_audit_policy** | [**SearchAuditPolicy**](SearchAuditPolicy.md)|  |

### Return type

[**SearchAuditPolicy**](SearchAuditPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search Audit policy was set successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_share_dashboards_outside_organization_policy**
> ShareDashboardsOutsideOrganizationPolicy set_share_dashboards_outside_organization_policy(share_dashboards_outside_organization_policy)

Set Share Dashboards Outside Organization policy.

Set the Share Dashboards Outside Organization policy. This policy allows users to share the dashboard with view only privileges outside of the organization (capability must be enabled from the Roles page). Disabling this policy will disable all dashboards that have been shared outside of the organization. [Learn More](https://help.sumologic.com/Visualizations-and-Alerts/Dashboards/Share_Dashboards/Share_a_Dashboard_Outside_Your_Org)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.share_dashboards_outside_organization_policy import ShareDashboardsOutsideOrganizationPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)
    share_dashboards_outside_organization_policy = ShareDashboardsOutsideOrganizationPolicy(
        enabled=True,
    ) # ShareDashboardsOutsideOrganizationPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Set Share Dashboards Outside Organization policy.
        api_response = api_instance.set_share_dashboards_outside_organization_policy(share_dashboards_outside_organization_policy)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->set_share_dashboards_outside_organization_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_dashboards_outside_organization_policy** | [**ShareDashboardsOutsideOrganizationPolicy**](ShareDashboardsOutsideOrganizationPolicy.md)|  |

### Return type

[**ShareDashboardsOutsideOrganizationPolicy**](ShareDashboardsOutsideOrganizationPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Share Dashboards Outside Organization policy was set successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_concurrent_sessions_limit_policy**
> UserConcurrentSessionsLimitPolicy set_user_concurrent_sessions_limit_policy(user_concurrent_sessions_limit_policy)

Set User Concurrent Sessions Limit policy.

Set the User Concurrent Sessions Limit policy. When enabled, the number of concurrent sessions a user may have is limited to the value entered. If a user exceeds the allowed number of sessions, the user's oldest session will be logged out to accommodate the new one. Disabling this policy means a user may have an unlimited number of concurrent sessions. [Learn More](https://help.sumologic.com/Manage/Security/Set_a_Limit_for_User_Concurrent_Sessions)

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import policies_management_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.user_concurrent_sessions_limit_policy import UserConcurrentSessionsLimitPolicy
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
    api_instance = policies_management_api.PoliciesManagementApi(api_client)
    user_concurrent_sessions_limit_policy = UserConcurrentSessionsLimitPolicy(
        enabled=True,
        max_concurrent_sessions=50,
    ) # UserConcurrentSessionsLimitPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Set User Concurrent Sessions Limit policy.
        api_response = api_instance.set_user_concurrent_sessions_limit_policy(user_concurrent_sessions_limit_policy)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PoliciesManagementApi->set_user_concurrent_sessions_limit_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_concurrent_sessions_limit_policy** | [**UserConcurrentSessionsLimitPolicy**](UserConcurrentSessionsLimitPolicy.md)|  |

### Return type

[**UserConcurrentSessionsLimitPolicy**](UserConcurrentSessionsLimitPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Concurrent Sessions Limit policy was set successfully. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


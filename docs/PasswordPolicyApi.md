# sumologic_client.PasswordPolicyApi

All URIs are relative to *https://api.au.sumologic.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_password_policy**](PasswordPolicyApi.md#get_password_policy) | **GET** /v1/passwordPolicy | Get the current password policy.
[**set_password_policy**](PasswordPolicyApi.md#set_password_policy) | **PUT** /v1/passwordPolicy | Update password policy.


# **get_password_policy**
> PasswordPolicy get_password_policy()

Get the current password policy.

Get the current password policy.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import password_policy_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.password_policy import PasswordPolicy
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
    api_instance = password_policy_api.PasswordPolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the current password policy.
        api_response = api_instance.get_password_policy()
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PasswordPolicyApi->get_password_policy: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PasswordPolicy**](PasswordPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current password policy. |  -  |
**0** | Operation failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_password_policy**
> PasswordPolicy set_password_policy(password_policy)

Update password policy.

Update the current password policy.

### Example

* Basic Authentication (basicAuth):
```python
import time
import sumologic_client
from sumologic_client.api import password_policy_api
from sumologic_client.model.error_response import ErrorResponse
from sumologic_client.model.password_policy import PasswordPolicy
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
    api_instance = password_policy_api.PasswordPolicyApi(api_client)
    password_policy = PasswordPolicy(
        min_length=8,
        max_length=128,
        must_contain_lowercase=True,
        must_contain_uppercase=True,
        must_contain_digits=True,
        must_contain_special_chars=True,
        max_password_age_in_days=365,
        min_unique_passwords=10,
        account_lockout_threshold=6,
        failed_login_reset_duration_in_mins=10,
        account_lockout_duration_in_mins=30,
        require_mfa=False,
        remember_mfa=True,
    ) # PasswordPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update password policy.
        api_response = api_instance.set_password_policy(password_policy)
        pprint(api_response)
    except sumologic_client.ApiException as e:
        print("Exception when calling PasswordPolicyApi->set_password_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_policy** | [**PasswordPolicy**](PasswordPolicy.md)|  |

### Return type

[**PasswordPolicy**](PasswordPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password Policy set successfully. |  -  |
**0** | Setting the password policy failed with an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


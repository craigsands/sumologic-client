"""
    Sumo Logic API

    # Getting Started Welcome to the Sumo Logic API reference. You can use these APIs to interact with the Sumo Logic platform. For information on the collector and search APIs see our [API home page](https://help.sumologic.com/APIs). ## API Endpoints Sumo Logic has several deployments in different geographic locations. You'll need to use the Sumo Logic API endpoint corresponding to your geographic location. See the table below for the different API endpoints by deployment. For details determining your account's deployment see [API endpoints](https://help.sumologic.com/?cid=3011).    <table>     <tr>       <td> <strong>Deployment</strong> </td>       <td> <strong>Endpoint</strong> </td>     </tr>     <tr>       <td> AU </td>       <td> https://api.au.sumologic.com/api/ </td>     </tr>     <tr>       <td> CA </td>       <td> https://api.ca.sumologic.com/api/ </td>     </tr>     <tr>       <td> DE </td>       <td> https://api.de.sumologic.com/api/ </td>     </tr>     <tr>       <td> EU </td>       <td> https://api.eu.sumologic.com/api/ </td>     </tr>     <tr>       <td> FED </td>       <td> https://api.fed.sumologic.com/api/ </td>     </tr>     <tr>       <td> IN </td>       <td> https://api.in.sumologic.com/api/ </td>     </tr>     <tr>       <td> JP </td>       <td> https://api.jp.sumologic.com/api/ </td>     </tr>     <tr>       <td> US1 </td>       <td> https://api.sumologic.com/api/ </td>     </tr>     <tr>       <td> US2 </td>       <td> https://api.us2.sumologic.com/api/ </td>     </tr>   </table>  ## Authentication Sumo Logic supports the following options for API authentication: - Access ID and Access Key - Base64 encoded Access ID and Access Key  See [Access Keys](https://help.sumologic.com/Manage/Security/Access-Keys) to generate an Access Key. Make sure to copy the key you create, because it is displayed only once. When you have an Access ID and Access Key you can execute requests such as the following:   ```bash   curl -u \"<accessId>:<accessKey>\" -X GET https://api.<deployment>.sumologic.com/api/v1/users   ```  Where `deployment` is either `au`, `ca`, `de`, `eu`, `fed`, `in`, `jp`, `us1`, or `us2`. See [API endpoints](#section/API-Endpoints) for details.  If you prefer to use basic access authentication, you can do a Base64 encoding of your `<accessId>:<accessKey>` to authenticate your HTTPS request. The following is an example request, replace the placeholder `<encoded>` with your encoded Access ID and Access Key string:   ```bash   curl -H \"Authorization: Basic <encoded>\" -X GET https://api.<deployment>.sumologic.com/api/v1/users   ```   Refer to [API Authentication](https://help.sumologic.com/?cid=3012) for a Base64 example.  ## Status Codes Generic status codes that apply to all our APIs. See the [HTTP status code registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) for reference.   <table>     <tr>       <td> <strong>HTTP Status Code</strong> </td>       <td> <strong>Error Code</strong> </td>       <td> <strong>Description</strong> </td>     </tr>     <tr>       <td> 301 </td>       <td> moved </td>       <td> The requested resource SHOULD be accessed through returned URI in Location Header. See [troubleshooting](https://help.sumologic.com/APIs/Troubleshooting-APIs/API-301-Error-Moved) for details.</td>     </tr>     <tr>       <td> 401 </td>       <td> unauthorized </td>       <td> Credential could not be verified.</td>     </tr>     <tr>       <td> 403 </td>       <td> forbidden </td>       <td> This operation is not allowed for your account type or the user doesn't have the role capability to perform this action. See [troubleshooting](https://help.sumologic.com/APIs/Troubleshooting-APIs/API-403-Error-This-operation-is-not-allowed-for-your-account-type) for details.</td>     </tr>     <tr>       <td> 404 </td>       <td> notfound </td>       <td> Requested resource could not be found. </td>     </tr>     <tr>       <td> 405 </td>       <td> method.unsupported </td>       <td> Unsupported method for URL. </td>     </tr>     <tr>       <td> 415 </td>       <td> contenttype.invalid </td>       <td> Invalid content type. </td>     </tr>     <tr>       <td> 429 </td>       <td> rate.limit.exceeded </td>       <td> The API request rate is higher than 4 request per second or inflight API requests are higher than 10 request per second. </td>     </tr>     <tr>       <td> 500 </td>       <td> internal.error </td>       <td> Internal server error. </td>     </tr>     <tr>       <td> 503 </td>       <td> service.unavailable </td>       <td> Service is currently unavailable. </td>     </tr>   </table>  ## Filtering Some API endpoints support filtering results on a specified set of fields. Each endpoint that supports filtering will list the fields that can be filtered. Multiple fields can be combined by using an ampersand `&` character.  For example, to get 20 users whose `firstName` is `John` and `lastName` is `Doe`:   ```bash   api.sumologic.com/v1/users?limit=20&firstName=John&lastName=Doe   ```  ## Sorting Some API endpoints support sorting fields by using the `sortBy` query parameter. The default sort order is ascending. Prefix the field with a minus sign `-` to sort in descending order.  For example, to get 20 users sorted by their `email` in descending order:   ```bash   api.sumologic.com/v1/users?limit=20&sort=-email   ```  ## Asynchronous Request Asynchronous requests do not wait for results, instead they immediately respond back with a job identifier while the job runs in the background. You can use the job identifier to track the status of the asynchronous job request. Here is a typical flow for an asynchronous request. 1. Start an asynchronous job. On success, a job identifier is returned. The job identifier uniquely identifies   your asynchronous job.  2. Once started, use the job identifier from step 1 to track the status of your asynchronous job. An asynchronous   request will typically provide an endpoint to poll for the status of asynchronous job. A successful response   from the status endpoint will have the following structure:   ```json   {       \"status\": \"Status of asynchronous request\",       \"statusMessage\": \"Optional message with additional information in case request succeeds\",       \"error\": \"Error object in case request fails\"   }   ```   The `status` field can have one of the following values:     1. `Success`: The job succeeded. The `statusMessage` field might have additional information.     2. `InProgress`: The job is still running.     3. `Failed`: The job failed. The `error` field in the response will have more information about the failure.  3. Some asynchronous APIs may provide a third endpoint (like [export result](#operation/getAsyncExportResult))   to fetch the result of an asynchronous job.   ### Example Let's say we want to export a folder with the identifier `0000000006A2E86F`. We will use the [async export](#operation/beginAsyncExport) API to export all the content under the folder with `id=0000000006A2E86F`. 1. Start an export job for the folder   ```bash   curl -X POST -u \"<accessId>:<accessKey>\" https://api.<deployment>.sumologic.com/api/v2/content/0000000006A2E86F/export   ```   See [authentication section](#section/Authentication) for more details about `accessId`, `accessKey`, and   `deployment`.   On success, you will get back a job identifier. In the response below, `C03E086C137F38B4` is the job identifier.   ```bash   {       \"id\": \"C03E086C137F38B4\"   }   ```  2. Now poll for the status of the asynchronous job with the [status](#operation/getAsyncExportStatus) endpoint.   ```bash   curl -X GET -u \"<accessId>:<accessKey>\" https://api.<deployment>.sumologic.com/api/v2/content/0000000006A2E86F/export/C03E086C137F38B4/status   ```   You may get a response like   ```json   {       \"status\": \"InProgress\",       \"statusMessage\": null,       \"error\": null   }   ```   It implies the job is still in progress. Keep polling till the status is either `Success` or `Failed`.  3. When the asynchronous job completes (`status != \"InProgress\"`), you can fetch the results with the   [export result](#operation/getAsyncExportResult) endpoint.   ```bash   curl -X GET -u \"<accessId>:<accessKey>\" https://api.<deployment>.sumologic.com/api/v2/content/0000000006A2E86F/export/C03E086C137F38B4/result   ```    The asynchronous job may fail (`status == \"Failed\"`). You can look at the `error` field for more details.   ```json   {       \"status\": \"Failed\",       \"errors\": {           \"code\": \"content1:too_many_items\",           \"message\": \"Too many objects: object count(1100) was greater than limit 1000\"       }   }   ```   ## Rate Limiting * A rate limit of four API requests per second (240 requests per minute) applies to all API calls from a user. * A rate limit of 10 concurrent requests to any API endpoint applies to an access key.  If a rate is exceeded, a rate limit exceeded 429 status code is returned.  ## Generating Clients You can use [OpenAPI Generator](https://openapi-generator.tech) to generate clients from the YAML file to access the API.  ### Using [NPM](https://www.npmjs.com/get-npm) 1. Install [NPM package wrapper](https://github.com/openapitools/openapi-generator-cli) globally, exposing the CLI   on the command line:   ```bash   npm install @openapitools/openapi-generator-cli -g   ```   You can see detailed instructions [here](https://openapi-generator.tech/docs/installation#npm).  2. Download the [YAML file](/docs/sumologic-api.yaml) and save it locally. Let's say the file is saved as `sumologic-api.yaml`. 3. Use the following command to generate `python` client inside the `sumo/client/python` directory:   ```bash   openapi-generator generate -i sumologic-api.yaml -g python -o sumo/client/python   ```   ### Using [Homebrew](https://brew.sh/) 1. Install OpenAPI Generator   ```bash   brew install openapi-generator   ```  2. Download the [YAML file](/docs/sumologic-api.yaml) and save it locally. Let's say the file is saved as `sumologic-api.yaml`. 3. Use the following command to generate `python` client side code inside the `sumo/client/python` directory:   ```bash   openapi-generator generate -i sumologic-api.yaml -g python -o sumo/client/python   ```   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from sumologic_client.api_client import ApiClient, Endpoint as _Endpoint
from sumologic_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from sumologic_client.model.async_job_status import AsyncJobStatus
from sumologic_client.model.begin_async_job_response import BeginAsyncJobResponse
from sumologic_client.model.content import Content
from sumologic_client.model.content_path import ContentPath
from sumologic_client.model.content_sync_definition import ContentSyncDefinition
from sumologic_client.model.error_response import ErrorResponse


class ContentManagementApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __async_copy_status(
            self,
            id,
            job_id,
            **kwargs
        ):
            """Content copy job status.  # noqa: E501

            Get the status of the copy request with the given job identifier. On success, field `statusMessage` will contain identifier of the newly copied content in format: `id: {hexIdentifier}`.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.async_copy_status(id, job_id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): The identifier of the content which was copied.
                job_id (str): The identifier of the asynchronous copy request job.

            Keyword Args:
                is_admin_mode (str): Set this to \"true\" if you want to perform the request as a Content Administrator.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AsyncJobStatus
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            kwargs['job_id'] = \
                job_id
            return self.call_with_http_info(**kwargs)

        self.async_copy_status = _Endpoint(
            settings={
                'response_type': (AsyncJobStatus,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/{id}/copy/{jobId}/status',
                'operation_id': 'async_copy_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'job_id',
                    'is_admin_mode',
                ],
                'required': [
                    'id',
                    'job_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'job_id':
                        (str,),
                    'is_admin_mode':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'job_id': 'jobId',
                    'is_admin_mode': 'isAdminMode',
                },
                'location_map': {
                    'id': 'path',
                    'job_id': 'path',
                    'is_admin_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__async_copy_status
        )

        def __begin_async_copy(
            self,
            id,
            destination_folder,
            **kwargs
        ):
            """Start a content copy job.  # noqa: E501

            Start an asynchronous content copy job with the given identifier to the destination folder. If the content item is a folder, everything under the folder is copied recursively.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.begin_async_copy(id, destination_folder, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): The identifier of the content item to copy. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format.
                destination_folder (str): The identifier of the destination folder.

            Keyword Args:
                is_admin_mode (str): Set this to \"true\" if you want to perform the request as a Content Administrator.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BeginAsyncJobResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            kwargs['destination_folder'] = \
                destination_folder
            return self.call_with_http_info(**kwargs)

        self.begin_async_copy = _Endpoint(
            settings={
                'response_type': (BeginAsyncJobResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/{id}/copy',
                'operation_id': 'begin_async_copy',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'destination_folder',
                    'is_admin_mode',
                ],
                'required': [
                    'id',
                    'destination_folder',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'destination_folder':
                        (str,),
                    'is_admin_mode':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'destination_folder': 'destinationFolder',
                    'is_admin_mode': 'isAdminMode',
                },
                'location_map': {
                    'id': 'path',
                    'destination_folder': 'query',
                    'is_admin_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__begin_async_copy
        )

        def __begin_async_delete(
            self,
            id,
            **kwargs
        ):
            """Start a content deletion job.  # noqa: E501

            Start an asynchronous content deletion job with the given identifier.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.begin_async_delete(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Identifier of the content to delete. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format.

            Keyword Args:
                is_admin_mode (str): Set this to \"true\" if you want to perform the request as a Content Administrator.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BeginAsyncJobResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.begin_async_delete = _Endpoint(
            settings={
                'response_type': (BeginAsyncJobResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/{id}/delete',
                'operation_id': 'begin_async_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'is_admin_mode',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'is_admin_mode':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'is_admin_mode': 'isAdminMode',
                },
                'location_map': {
                    'id': 'path',
                    'is_admin_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__begin_async_delete
        )

        def __begin_async_export(
            self,
            id,
            **kwargs
        ):
            """Start a content export job.  # noqa: E501

            Schedule an _asynchronous_ export of content with the given identifier. You will get back an asynchronous job identifier on success. Use the [getAsyncExportStatus](#operation/getAsyncExportStatus) endpoint and the job identifier you got back in the response to track the status of an asynchronous export job. If the content item is a folder, everything under the folder is exported recursively. Keep in mind when exporting large folders that there is a limit of 1000 content objects that can be exported at once. If you want to import more than 1000 content objects, then be sure to split the import into batches of 1000 objects or less. The results from the export are compatible with the Library import feature in the Sumo Logic user interface as well as the API content import job.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.begin_async_export(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): The identifier of the content item to export. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format.

            Keyword Args:
                is_admin_mode (str): Set this to \"true\" if you want to perform the request as a Content Administrator.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BeginAsyncJobResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.begin_async_export = _Endpoint(
            settings={
                'response_type': (BeginAsyncJobResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/{id}/export',
                'operation_id': 'begin_async_export',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'is_admin_mode',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'is_admin_mode':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'is_admin_mode': 'isAdminMode',
                },
                'location_map': {
                    'id': 'path',
                    'is_admin_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__begin_async_export
        )

        def __begin_async_import(
            self,
            folder_id,
            content_sync_definition,
            **kwargs
        ):
            """Start a content import job.  # noqa: E501

            Schedule an asynchronous import of content inside an existing folder with the given identifier. Import requests can be used to create or update content within a folder. Content items need to have a unique name within their folder. If there is already a content item with the same name in the folder, you can set the `overwrite` parameter to `true` to overwrite existing content items. By default, the `overwrite` parameter is set to `false`, where the import will fail if a content item with the same name already exist. Keep in mind when importing large folders that there is a limit of 1000 content objects that can be imported at once. If you want to import more than 1000 content objects, then be sure to split the import into batches of 1000 objects or less.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.begin_async_import(folder_id, content_sync_definition, async_req=True)
            >>> result = thread.get()

            Args:
                folder_id (str): The identifier of the folder to import into. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format.
                content_sync_definition (ContentSyncDefinition): The content to import.

            Keyword Args:
                is_admin_mode (str): Set this to \"true\" if you want to perform the request as a Content Administrator.. [optional]
                overwrite (bool): Set this to \"true\" to overwrite a content item if the name already exists.. [optional] if omitted the server will use the default value of False
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BeginAsyncJobResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['folder_id'] = \
                folder_id
            kwargs['content_sync_definition'] = \
                content_sync_definition
            return self.call_with_http_info(**kwargs)

        self.begin_async_import = _Endpoint(
            settings={
                'response_type': (BeginAsyncJobResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/folders/{folderId}/import',
                'operation_id': 'begin_async_import',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'folder_id',
                    'content_sync_definition',
                    'is_admin_mode',
                    'overwrite',
                ],
                'required': [
                    'folder_id',
                    'content_sync_definition',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'folder_id':
                        (str,),
                    'content_sync_definition':
                        (ContentSyncDefinition,),
                    'is_admin_mode':
                        (str,),
                    'overwrite':
                        (bool,),
                },
                'attribute_map': {
                    'folder_id': 'folderId',
                    'is_admin_mode': 'isAdminMode',
                    'overwrite': 'overwrite',
                },
                'location_map': {
                    'folder_id': 'path',
                    'content_sync_definition': 'body',
                    'is_admin_mode': 'header',
                    'overwrite': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__begin_async_import
        )

        def __get_async_delete_status(
            self,
            id,
            job_id,
            **kwargs
        ):
            """Content deletion job status.  # noqa: E501

            Get the status of an asynchronous content deletion job request for the given job identifier.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_async_delete_status(id, job_id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Identifier of the content to delete.
                job_id (str): The identifier of the asynchronous job.

            Keyword Args:
                is_admin_mode (str): Set this to \"true\" if you want to perform the request as a Content Administrator.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AsyncJobStatus
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            kwargs['job_id'] = \
                job_id
            return self.call_with_http_info(**kwargs)

        self.get_async_delete_status = _Endpoint(
            settings={
                'response_type': (AsyncJobStatus,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/{id}/delete/{jobId}/status',
                'operation_id': 'get_async_delete_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'job_id',
                    'is_admin_mode',
                ],
                'required': [
                    'id',
                    'job_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'job_id':
                        (str,),
                    'is_admin_mode':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'job_id': 'jobId',
                    'is_admin_mode': 'isAdminMode',
                },
                'location_map': {
                    'id': 'path',
                    'job_id': 'path',
                    'is_admin_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_async_delete_status
        )

        def __get_async_export_result(
            self,
            content_id,
            job_id,
            **kwargs
        ):
            """Content export job result.  # noqa: E501

            Get results from content export job for the given job identifier. The results from this export are incompatible with the Library import feature in the Sumo user interface.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_async_export_result(content_id, job_id, async_req=True)
            >>> result = thread.get()

            Args:
                content_id (str): The identifier of the exported content item.
                job_id (str): The identifier of the asynchronous job.

            Keyword Args:
                is_admin_mode (str): Set this to \"true\" if you want to perform the request as a Content Administrator.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ContentSyncDefinition
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['content_id'] = \
                content_id
            kwargs['job_id'] = \
                job_id
            return self.call_with_http_info(**kwargs)

        self.get_async_export_result = _Endpoint(
            settings={
                'response_type': (ContentSyncDefinition,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/{contentId}/export/{jobId}/result',
                'operation_id': 'get_async_export_result',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'content_id',
                    'job_id',
                    'is_admin_mode',
                ],
                'required': [
                    'content_id',
                    'job_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'content_id':
                        (str,),
                    'job_id':
                        (str,),
                    'is_admin_mode':
                        (str,),
                },
                'attribute_map': {
                    'content_id': 'contentId',
                    'job_id': 'jobId',
                    'is_admin_mode': 'isAdminMode',
                },
                'location_map': {
                    'content_id': 'path',
                    'job_id': 'path',
                    'is_admin_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_async_export_result
        )

        def __get_async_export_status(
            self,
            content_id,
            job_id,
            **kwargs
        ):
            """Content export job status.  # noqa: E501

            Get the status of an asynchronous content export request for the given job identifier. On success, use the [getExportResult](#operation/getAsyncExportResult) endpoint to get the result of the export job.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_async_export_status(content_id, job_id, async_req=True)
            >>> result = thread.get()

            Args:
                content_id (str): The identifier of the exported content item.
                job_id (str): The identifier of the asynchronous export job.

            Keyword Args:
                is_admin_mode (str): Set this to \"true\" if you want to perform the request as a Content Administrator.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AsyncJobStatus
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['content_id'] = \
                content_id
            kwargs['job_id'] = \
                job_id
            return self.call_with_http_info(**kwargs)

        self.get_async_export_status = _Endpoint(
            settings={
                'response_type': (AsyncJobStatus,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/{contentId}/export/{jobId}/status',
                'operation_id': 'get_async_export_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'content_id',
                    'job_id',
                    'is_admin_mode',
                ],
                'required': [
                    'content_id',
                    'job_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'content_id':
                        (str,),
                    'job_id':
                        (str,),
                    'is_admin_mode':
                        (str,),
                },
                'attribute_map': {
                    'content_id': 'contentId',
                    'job_id': 'jobId',
                    'is_admin_mode': 'isAdminMode',
                },
                'location_map': {
                    'content_id': 'path',
                    'job_id': 'path',
                    'is_admin_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_async_export_status
        )

        def __get_async_import_status(
            self,
            folder_id,
            job_id,
            **kwargs
        ):
            """Content import job status.  # noqa: E501

            Get the status of a content import job for the given job identifier.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_async_import_status(folder_id, job_id, async_req=True)
            >>> result = thread.get()

            Args:
                folder_id (str): The identifier of the folder to import into.
                job_id (str): The identifier of the import request.

            Keyword Args:
                is_admin_mode (str): Set this to \"true\" if you want to perform the request as a Content Administrator.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AsyncJobStatus
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['folder_id'] = \
                folder_id
            kwargs['job_id'] = \
                job_id
            return self.call_with_http_info(**kwargs)

        self.get_async_import_status = _Endpoint(
            settings={
                'response_type': (AsyncJobStatus,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/folders/{folderId}/import/{jobId}/status',
                'operation_id': 'get_async_import_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'folder_id',
                    'job_id',
                    'is_admin_mode',
                ],
                'required': [
                    'folder_id',
                    'job_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'folder_id':
                        (str,),
                    'job_id':
                        (str,),
                    'is_admin_mode':
                        (str,),
                },
                'attribute_map': {
                    'folder_id': 'folderId',
                    'job_id': 'jobId',
                    'is_admin_mode': 'isAdminMode',
                },
                'location_map': {
                    'folder_id': 'path',
                    'job_id': 'path',
                    'is_admin_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_async_import_status
        )

        def __get_item_by_path(
            self,
            path,
            **kwargs
        ):
            """Get content item by path.  # noqa: E501

            Get a content item corresponding to the given path.  _Path is specified in the required query parameter `path`. The path should be URL encoded._ For example, to get \"Acme Corp\" folder of a user \"user@sumo.com\" you can use the following curl command:   ```bash   curl https://api.sumologic.com/api/v2/content/path?path=/Library/Users/user%40sumo.com/Acme%20Corp   ```   The absolute path to a content item should be specified to get the item. The content library has \"Library\" folder at the root level. For items in \"Personal\" folder, the base path is \"/Library/Users/user@sumo.com\" where \"user@sumo.com\" is the email address of the user. For example if a user with email address `wile@acme.com` has `Rockets` folder inside Personal folder, the path of Rockets folder will be `/Library/Users/wile@acme.com/Rockets`.  For items in \"Admin Recommended\" folder, the base path is \"/Library/Admin Recommended\". For example, given a folder `Acme` in Admin Recommended folder, the path will be `/Library/Admin Recommended/Acme`.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_item_by_path(path, async_req=True)
            >>> result = thread.get()

            Args:
                path (str): Path of the content item to retrieve.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Content
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['path'] = \
                path
            return self.call_with_http_info(**kwargs)

        self.get_item_by_path = _Endpoint(
            settings={
                'response_type': (Content,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/path',
                'operation_id': 'get_item_by_path',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'path',
                ],
                'required': [
                    'path',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'path':
                        (str,),
                },
                'attribute_map': {
                    'path': 'path',
                },
                'location_map': {
                    'path': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_item_by_path
        )

        def __get_path_by_id(
            self,
            content_id,
            **kwargs
        ):
            """Get path of an item.  # noqa: E501

            Get full path of a content item with the given identifier.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_path_by_id(content_id, async_req=True)
            >>> result = thread.get()

            Args:
                content_id (str): Identifier of the content item to get the path.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ContentPath
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['content_id'] = \
                content_id
            return self.call_with_http_info(**kwargs)

        self.get_path_by_id = _Endpoint(
            settings={
                'response_type': (ContentPath,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/{contentId}/path',
                'operation_id': 'get_path_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'content_id',
                ],
                'required': [
                    'content_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'content_id':
                        (str,),
                },
                'attribute_map': {
                    'content_id': 'contentId',
                },
                'location_map': {
                    'content_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_path_by_id
        )

        def __move_item(
            self,
            destination_folder_id,
            id,
            **kwargs
        ):
            """Move an item.  # noqa: E501

            Moves an item from its current location to another folder.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.move_item(destination_folder_id, id, async_req=True)
            >>> result = thread.get()

            Args:
                destination_folder_id (str): Identifier of the destination folder.
                id (str): Identifier of the item the user wants to move.

            Keyword Args:
                is_admin_mode (str): Set this to \"true\" if you want to perform the request as a Content Administrator.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['destination_folder_id'] = \
                destination_folder_id
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.move_item = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v2/content/{id}/move',
                'operation_id': 'move_item',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'destination_folder_id',
                    'id',
                    'is_admin_mode',
                ],
                'required': [
                    'destination_folder_id',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'destination_folder_id':
                        (str,),
                    'id':
                        (str,),
                    'is_admin_mode':
                        (str,),
                },
                'attribute_map': {
                    'destination_folder_id': 'destinationFolderId',
                    'id': 'id',
                    'is_admin_mode': 'isAdminMode',
                },
                'location_map': {
                    'destination_folder_id': 'query',
                    'id': 'path',
                    'is_admin_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__move_item
        )

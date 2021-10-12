# LookupAsyncJobStatus

Lookup table async job status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | An identifier returned in response to an asynchronous request. | 
**status** | **str** | Whether or not the request is pending (&#x60;Pending&#x60;), in progress (&#x60;InProgress&#x60;), has completed successfully (&#x60;Success&#x60;), has completed partially with warnings (&#x60;PartialSuccess&#x60;) or has completed with an error (&#x60;Failed&#x60;). | 
**lookup_content_id** | **str** | Content id of lookup table on which this operation was performed. | 
**lookup_name** | **str** | Name of lookup table on which this operation was performed. | 
**lookup_content_path** | **str** | Content path of lookup table on which this operation was performed. | 
**user_id** | **str** | User id of user who initiated this operation. | 
**created_at** | **datetime** | Creation time of this job in UTC. | 
**modified_at** | **datetime** | Timestamp in UTC when status was last updated. | 
**status_messages** | **[str]** | Additional status messages generated if any if the status is &#x60;Success&#x60;. | [optional] 
**errors** | [**[ErrorDescription]**](ErrorDescription.md) | More information about the failures, if the status is &#x60;Failed&#x60;. | [optional] 
**warnings** | [**[WarningDescription]**](WarningDescription.md) | More information about the warnings, if the status is &#x60;PartialSuccess&#x60;. | [optional] 
**request_type** | **str** | Type of asynchronous request made:   - &#x60;BulkMerge&#x60;   - &#x60;BulkReplace&#x60;   - &#x60;Truncate&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



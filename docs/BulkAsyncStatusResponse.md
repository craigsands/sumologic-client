# BulkAsyncStatusResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_statuses** | [**{str: (AsyncJobStatus,)}**](AsyncJobStatus.md) | Map of job identifiers to job statuses. | 
**errors** | [**{str: (BulkErrorResponse,)}**](BulkErrorResponse.md) | Map of content identifiers to error messages for all failed job requests | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



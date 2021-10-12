# IngestBudgetV2AllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the ingest budget. | 
**created_at** | **datetime** | The creation timestamp in UTC of the Ingest Budget. | 
**created_by** | **str** | The identifier of the user who created the Ingest Budget. | 
**modified_at** | **datetime** | The modified timestamp in UTC of the Ingest Budget. | 
**modified_by** | **str** | The identifier of the user who modified the Ingest Budget. | 
**usage_bytes** | **int** | Current usage since the last reset, in bytes. | [optional] 
**usage_status** | **str** | Status of the current usage. Can be &#x60;Normal&#x60;, &#x60;Approaching&#x60;, &#x60;Exceeded&#x60;, or &#x60;Unknown&#x60; (unable to retrieve usage). | [optional] 
**budget_version** | **int** | The version of the Ingest Budget | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



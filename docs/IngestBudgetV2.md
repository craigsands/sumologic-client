# IngestBudgetV2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of the ingest budget. | 
**scope** | **str** | A scope is a constraint that will be used to identify the messages on which budget needs to be applied. A scope is consists of key and value separated by &#x3D;. The field must be enabled in the fields table. Value supports wildcard. e.g. _sourceCategory&#x3D;*prod*payment*, cluster&#x3D;kafka. If the scope is defined _sourceCategory&#x3D;*nginx* in this budget will be applied on messages having fields _sourceCategory&#x3D;prod/nginx, _sourceCategory&#x3D;dev/nginx, or _sourceCategory&#x3D;dev/nginx/error | 
**capacity_bytes** | **int** | Capacity of the ingest budget, in bytes. It takes a few minutes for Collectors to stop collecting when capacity is reached. We recommend setting a soft limit that is lower than your needed hard limit. | 
**timezone** | **str** | Time zone of the reset time for the ingest budget. Follow the format in the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). | 
**reset_time** | **str** | Reset time of the ingest budget in HH:MM format. | 
**action** | **str** | Action to take when ingest budget&#39;s capacity is reached. All actions are audited. Supported values are:   * &#x60;stopCollecting&#x60;   * &#x60;keepCollecting&#x60; | 
**id** | **str** | Unique identifier for the ingest budget. | 
**created_at** | **datetime** | The creation timestamp in UTC of the Ingest Budget. | 
**created_by** | **str** | The identifier of the user who created the Ingest Budget. | 
**modified_at** | **datetime** | The modified timestamp in UTC of the Ingest Budget. | 
**modified_by** | **str** | The identifier of the user who modified the Ingest Budget. | 
**description** | **str** | Description of the ingest budget. | [optional] 
**audit_threshold** | **int** | The threshold as a percentage of when an ingest budget&#39;s capacity usage is logged in the Audit Index. | [optional] 
**usage_bytes** | **int** | Current usage since the last reset, in bytes. | [optional] 
**usage_status** | **str** | Status of the current usage. Can be &#x60;Normal&#x60;, &#x60;Approaching&#x60;, &#x60;Exceeded&#x60;, or &#x60;Unknown&#x60; (unable to retrieve usage). | [optional] 
**budget_version** | **int** | The version of the Ingest Budget | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



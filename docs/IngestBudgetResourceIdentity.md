# IngestBudgetResourceIdentity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the resource. | 
**type** | **str** | -&gt; Resource type. Supported types are - &#x60;Collector&#x60;, &#x60;Source&#x60;, &#x60;IngestBudget&#x60; and &#x60;Organisation&#x60;. | 
**ingest_budget_field_value** | **str** | The unique field value of the ingest budget v1. This will be empty for v2 budgets. | [optional]  if omitted the server will use the default value of "Unknown"
**scope** | **str** | The scope of the ingest budget v2. This will be empty for v1 budgets. | [optional]  if omitted the server will use the default value of "Unknown"
**name** | **str** | The name of the resource. | [optional]  if omitted the server will use the default value of "Unknown"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



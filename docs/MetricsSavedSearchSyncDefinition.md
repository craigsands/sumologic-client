# MetricsSavedSearchSyncDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | [**ResolvableTimeRange**](ResolvableTimeRange.md) |  | 
**metrics_queries** | [**[MetricsSavedSearchQuerySyncDefinition]**](MetricsSavedSearchQuerySyncDefinition.md) | Metrics queries. | 
**desired_quantization_in_secs** | **int** | Desired quantization in seconds. | 
**type** | **str** | The content item type. **Note:**  - &#x60;MewboardSyncDefinition&#x60; _is depreciated, and will soon be removed. Please use_ &#x60;DashboardV2SyncDefinition&#x60;    _instead_.  - Dashboard links are not supported for dashboards. | 
**name** | **str** | The name of the item. | 
**description** | **str** | Item description in the content library. | [optional] 
**log_query** | **str** | Query used to add an overlay to the chart. | [optional] 
**properties** | **str** | Chart properties. This field is optional. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



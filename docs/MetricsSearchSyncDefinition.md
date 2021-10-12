# MetricsSearchSyncDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | [**ResolvableTimeRange**](ResolvableTimeRange.md) |  | 
**queries** | [**[Query]**](Query.md) | Queries of the metrics search page. | 
**type** | **str** | The content item type. **Note:**  - &#x60;MewboardSyncDefinition&#x60; _is depreciated, and will soon be removed. Please use_ &#x60;DashboardV2SyncDefinition&#x60;    _instead_.  - Dashboard links are not supported for dashboards. | 
**name** | **str** | The name of the item. | 
**description** | **str** | Description of the metrics search page. | [optional] 
**visual_settings** | **str** | Visual settings of the metrics search page. Must be a string representing a valid JSON object.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



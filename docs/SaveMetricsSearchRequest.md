# SaveMetricsSearchRequest

The definition of the metrics search to save in the content library.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Item title in the content library. | 
**description** | **str** | Item description in the content library. | 
**time_range** | [**ResolvableTimeRange**](ResolvableTimeRange.md) |  | 
**metrics_queries** | [**[MetricsSearchQuery]**](MetricsSearchQuery.md) | Metrics queries, up to the maximum of six. | 
**parent_id** | **str** | Identifier of a folder to which the metrics search should be added. | 
**log_query** | **str** | Log query used to add an overlay to the chart. | [optional] 
**desired_quantization_in_secs** | **int** | Desired quantization in seconds. | [optional]  if omitted the server will use the default value of 0
**properties** | **str** | Chart properties, like line width, color palette, and the fill missing data method. Leave this field empty to use the defaults. This property contains JSON object encoded as a string.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



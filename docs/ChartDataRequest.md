# ChartDataRequest

Request payload for monitor chart data visualization.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_type** | **str** | The type of monitor. Valid values:   1. &#x60;Logs&#x60;: A logs query monitor.   2. &#x60;Metrics&#x60;: A metrics query monitor. | 
**queries** | [**[MonitorQuery]**](MonitorQuery.md) | All queries from the monitor. | 
**triggers** | [**[TriggerCondition]**](TriggerCondition.md) | Defines the conditions of when to send notifications. | [optional] 
**time_range** | [**ResolvableTimeRange**](ResolvableTimeRange.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



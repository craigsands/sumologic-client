# MonitorQueries

Queries to be validated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_type** | **str** | The type of monitor. Valid values:   1. &#x60;Logs&#x60;: A logs query monitor.   2. &#x60;Metrics&#x60;: A metrics query monitor. | 
**time_range** | **str** | The relative time range of the monitor. | 
**queries** | [**[UnvalidatedMonitorQuery]**](UnvalidatedMonitorQuery.md) | Queries to be validated. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



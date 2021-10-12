# AlertsLibraryAlertUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the alert or folder. | 
**version** | **int** | The version of the alert or folder. | 
**type** | **str** | Type of the object model. | 
**monitor_id** | **str** | The Id of the associated monitor. | [optional] 
**resolved_at** | **datetime, none_type** | The time at which the alert was resolved. | [optional] 
**abnormality_start_time** | **datetime** | The time at which the incident started. | [optional] 
**alert_type** | **str** | The severity of the Alert. Valid values:   1. &#x60;Critical&#x60;   2. &#x60;Warning&#x60;   3. &#x60;MissingData&#x60; | [optional] 
**status** | **str** | The status of the Alert. Valid values:   1. &#x60;Triggered&#x60;   2. &#x60;Resolved&#x60; | [optional] 
**monitor_queries** | [**[AlertMonitorQuery]**](AlertMonitorQuery.md) | All queries from the monitor relevant to the alert. | [optional] 
**trigger_queries** | [**[AlertMonitorQuery]**](AlertMonitorQuery.md) | All queries from the monitor relevant to the alert with triggered time series filters. | [optional] 
**monitor_url** | **str** | URL for this monitor&#39;s view page | [optional] 
**trigger_query_url** | **str** | A link to search with the triggering data and time range | [optional] 
**trigger_conditions** | [**[TriggerCondition]**](TriggerCondition.md) | Trigger conditions which were breached to create this Alert. | [optional] 
**trigger_value** | **float** | The of the query result which breached the trigger condition. | [optional] 
**monitor_type** | **str** | The type of monitor. Valid values:   1. &#x60;Logs&#x60;: A logs query monitor.   2. &#x60;Metrics&#x60;: A metrics query monitor. | [optional] 
**entity_ids** | **[str]** | One or more entity identifiers involved in this Alert. | [optional] 
**notes** | **str** |  | [optional] 
**extra_details** | [**ExtraDetails**](ExtraDetails.md) |  | [optional] 
**alert_condition** | **str, none_type** | The condition which triggered this alert. | [optional] 
**description** | **str** | The description of the alert or folder. | [optional]  if omitted the server will use the default value of ""
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



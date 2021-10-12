# AlertsLibraryAlertResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the alert or folder. | 
**name** | **str** | Identifier of the alert or folder. | 
**description** | **str** | Description of the alert or folder. | 
**version** | **int** | Version of the alert or folder. | 
**created_at** | **datetime** | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. | 
**created_by** | **str** | Identifier of the user who created the resource. | 
**modified_at** | **datetime** | Last modification timestamp in UTC. | 
**modified_by** | **str** | Identifier of the user who last modified the resource. | 
**parent_id** | **str** | Identifier of the parent folder. | 
**content_type** | **str** | Type of the content. Valid values:   1) Alert   2) Folder | 
**type** | **str** | Type of the object model. | 
**is_system** | **bool** | System objects are objects provided by Sumo Logic. System objects can only be localized. Non-local fields can&#39;t be updated. | 
**is_mutable** | **bool** | Immutable objects are \&quot;READ-ONLY\&quot;. | 
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
**is_locked** | **bool** | Whether the object is locked. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



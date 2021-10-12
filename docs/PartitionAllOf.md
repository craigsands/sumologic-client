# PartitionAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the partition. | 
**total_bytes** | **int** | Size of data in partition in bytes. | 
**is_active** | **bool** | This has the value &#x60;true&#x60; if the partition is active and &#x60;false&#x60; if it has been decommissioned. | [optional] 
**new_retention_period** | **int** | If the retentionPeriod is scheduled to be updated in the future (i.e., if retentionPeriod is previously reduced with value of reduceRetentionPeriodImmediately as false), this property gives the future value of retentionPeriod while retentionPeriod gives the current value. retentionPeriod will take up the value of newRetentionPeriod after the scheduled time. | [optional] 
**index_type** | **str** | This has the value &#x60;DefaultIndex&#x60;, &#x60;AuditIndex&#x60;or &#x60;Partition&#x60; depending upon the type of partition. | [optional] 
**retention_effective_at** | **datetime** | When the newRetentionPeriod will become effective in UTC format. | [optional] 
**data_forwarding_id** | **str** | Id of the data forwarding configuration to be used by the partition. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



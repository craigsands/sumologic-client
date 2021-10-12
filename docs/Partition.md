# Partition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the partition. | 
**routing_expression** | **str** | The query that defines the data to be included in the partition. | 
**created_at** | **datetime** | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. | 
**created_by** | **str** | Identifier of the user who created the resource. | 
**modified_at** | **datetime** | Last modification timestamp in UTC. | 
**modified_by** | **str** | Identifier of the user who last modified the resource. | 
**id** | **str** | Unique identifier for the partition. | 
**total_bytes** | **int** | Size of data in partition in bytes. | 
**analytics_tier** | **str** | The Data Tier where the data in the partition will reside. Possible values are:               1. &#x60;continuous&#x60;               2. &#x60;frequent&#x60;               3. &#x60;infrequent&#x60; Note: The \&quot;infrequent\&quot; and \&quot;frequent\&quot; tiers are only to available Cloud Flex Credits Enterprise Suite accounts. | [optional]  if omitted the server will use the default value of "continuous"
**retention_period** | **int** | The number of days to retain data in the partition, or -1 to use the default value for your account.  Only relevant if your account has variable retention enabled. | [optional]  if omitted the server will use the default value of -1
**is_compliant** | **bool** | Whether the partition is compliant or not. Mark a partition as compliant if it contains data used for compliance or audit purpose. Retention for a compliant partition can only be increased and cannot be reduced after the partition is marked compliant. A partition once marked compliant, cannot be marked non-compliant later. | [optional]  if omitted the server will use the default value of False
**is_active** | **bool** | This has the value &#x60;true&#x60; if the partition is active and &#x60;false&#x60; if it has been decommissioned. | [optional] 
**new_retention_period** | **int** | If the retentionPeriod is scheduled to be updated in the future (i.e., if retentionPeriod is previously reduced with value of reduceRetentionPeriodImmediately as false), this property gives the future value of retentionPeriod while retentionPeriod gives the current value. retentionPeriod will take up the value of newRetentionPeriod after the scheduled time. | [optional] 
**index_type** | **str** | This has the value &#x60;DefaultIndex&#x60;, &#x60;AuditIndex&#x60;or &#x60;Partition&#x60; depending upon the type of partition. | [optional] 
**retention_effective_at** | **datetime** | When the newRetentionPeriod will become effective in UTC format. | [optional] 
**data_forwarding_id** | **str** | Id of the data forwarding configuration to be used by the partition. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



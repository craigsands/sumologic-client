# UpdatePartitionDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention_period** | **int** | The number of days to retain data in the partition, or -1 to use the default value for your account. Only relevant if your account has variable retention enabled. | [optional] 
**reduce_retention_period_immediately** | **bool** | This is required if the newly specified &#x60;retentionPeriod&#x60; is less than the existing retention period.  In such a situation, a value of &#x60;true&#x60; says that data between the existing retention period and the new retention period should be deleted immediately; if &#x60;false&#x60;, such data will be deleted after seven days. This property is optional and ignored if the specified &#x60;retentionPeriod&#x60; is greater than or equal to the current retention period. | [optional]  if omitted the server will use the default value of False
**is_compliant** | **bool** | Whether to mark a partition as compliant. Mark a partition as compliant if it contains data used for compliance or audit purpose. Retention for a compliant partition can only be increased and cannot be reduced after the partition marked as compliant. A partition once marked compliant, cannot be marked non-compliant later. | [optional]  if omitted the server will use the default value of False
**routing_expression** | **str** | The query that defines the data to be included in the partition. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



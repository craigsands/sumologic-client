# UpdateScheduledViewDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_forwarding_id** | **str** | An optional ID of a data forwarding configuration to be used by the scheduled view. | [optional] 
**retention_period** | **int** | The number of days to retain data in the scheduled view, or -1 to use the default value for your account.  Only relevant if your account has multi-retention. enabled. | [optional]  if omitted the server will use the default value of -1
**reduce_retention_period_immediately** | **bool** | This is required if the newly specified &#x60;retentionPeriod&#x60; is less than the existing retention period.  In such a situation, a value of &#x60;true&#x60; says that data between the existing retention period and the new retention period should be deleted immediately; if &#x60;false&#x60;, such data will be deleted after seven days. This property is optional and ignored if the specified &#x60;retentionPeriod&#x60; is greater than or equal to the current retention period. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



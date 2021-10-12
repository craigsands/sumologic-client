# CreatePartitionDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the partition. | 
**routing_expression** | **str** | The query that defines the data to be included in the partition. | 
**analytics_tier** | **str** | The Data Tier where the data in the partition will reside. Possible values are:               1. &#x60;continuous&#x60;               2. &#x60;frequent&#x60;               3. &#x60;infrequent&#x60; Note: The \&quot;infrequent\&quot; and \&quot;frequent\&quot; tiers are only to available Cloud Flex Credits Enterprise Suite accounts. | [optional]  if omitted the server will use the default value of "continuous"
**retention_period** | **int** | The number of days to retain data in the partition, or -1 to use the default value for your account.  Only relevant if your account has variable retention enabled. | [optional]  if omitted the server will use the default value of -1
**is_compliant** | **bool** | Whether the partition is compliant or not. Mark a partition as compliant if it contains data used for compliance or audit purpose. Retention for a compliant partition can only be increased and cannot be reduced after the partition is marked compliant. A partition once marked compliant, cannot be marked non-compliant later. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateScheduledViewDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The query that defines the data to be included in the scheduled view. | 
**index_name** | **str** | Name of the index for the scheduled view. | 
**start_time** | **datetime** | Start timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. | 
**retention_period** | **int** | The number of days to retain data in the scheduled view, or -1 to use the default value for your account.  Only relevant if your account has multi-retention. enabled. | [optional]  if omitted the server will use the default value of -1
**data_forwarding_id** | **str** | An optional ID of a data forwarding configuration to be used by the scheduled view. | [optional] 
**parsing_mode** | **str** | Define the parsing mode to scan the JSON format log messages. Possible values are:   1. &#x60;AutoParse&#x60;   2. &#x60;Manual&#x60; In AutoParse mode, the system automatically figures out fields to parse based on the search query. While in the Manual mode, no fields are parsed out automatically. For more information see [Dynamic Parsing](https://help.sumologic.com/?cid&#x3D;0011). | [optional]  if omitted the server will use the default value of "Manual"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



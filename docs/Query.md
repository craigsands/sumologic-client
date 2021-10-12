# Query


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_string** | **str** | The metrics, traces or logs query. | 
**query_type** | **str** | The type of the query, either &#x60;Metrics&#x60;, &#x60;Traces&#x60; or &#x60;Logs&#x60;. | 
**query_key** | **str** | The key for metric, traces or log queries. Used as an identifier for queries. | 
**metrics_query_mode** | **str** | The mode of the metrics query that the user was editing. Can be &#x60;Basic&#x60; or &#x60;Advanced&#x60;. Will ONLY be specified for metrics queries.  | [optional] 
**metrics_query_data** | [**MetricsQueryData**](MetricsQueryData.md) |  | [optional] 
**traces_query_data** | [**TracesQueryData**](TracesQueryData.md) |  | [optional] 
**parse_mode** | **str** | This field only applies for queryType of &#x60;Logs&#x60; but other query types may be supported in the future. Define the parsing mode to scan the JSON format log messages. Possible values are:   1. &#x60;Auto&#x60;   2. &#x60;Manual&#x60; In AutoParse mode, the system automatically figures out fields to parse based on the search query. While in the Manual mode, no fields are parsed out automatically. For more information see [Dynamic Parsing](https://help.sumologic.com/?cid&#x3D;0011). | [optional]  if omitted the server will use the default value of "Auto"
**time_source** | **str** | This field only applies for queryType of &#x60;Logs&#x60; but other query types may be supported in the future. Define the time source of this query. Possible values are &#x60;Message&#x60; and &#x60;Receipt&#x60;. &#x60;Message&#x60; will use the timeStamp on the message, while &#x60;Receipt&#x60; will use the timestamp it was received by Sumo. | [optional]  if omitted the server will use the default value of "Message"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



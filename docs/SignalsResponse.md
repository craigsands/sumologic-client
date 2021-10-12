# SignalsResponse

Signal response object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signal_type** | **str** | The type of the signal to compute. Can be &#x60;LogFluctuation&#x60;, &#x60;DimensionalityExplanation&#x60;, &#x60;GisBenchmark&#x60; or &#x60;Anomalies&#x60;  | 
**signal_id** | **str** | The id for the signal result in hex format. | 
**start_time** | **datetime** | Start time of the signal. | 
**end_time** | **datetime** | End time of the signal. | 
**summary** | **str** | Description of the payload. | 
**payload** | **str** | Json string for computed signal. | 
**open_in_queries** | [**[OpenInQuery]**](OpenInQuery.md) | Raw data queries for the computed signal. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



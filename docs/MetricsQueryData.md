# MetricsQueryData

The data format describing a basic metrics query.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** | The metric of the query. | 
**filters** | [**[MetricsFilter]**](MetricsFilter.md) | A list of filters for the metrics query. | 
**aggregation_type** | **str** | The type of aggregation. Can be &#x60;Count&#x60;, &#x60;Minimum&#x60;, &#x60;Maximum&#x60;, &#x60;Sum&#x60;, &#x60;Average&#x60; or &#x60;None&#x60;. | [optional] 
**group_by** | **str** | The field to group the results by. | [optional] 
**operators** | [**[OperatorData]**](OperatorData.md) | A list of operator data for the metrics query. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



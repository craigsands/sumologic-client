# LogsOutlierConditionAllOf

A rule that defines how logs monitor should evaluate outlier data and trigger notifications.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window** | **int** | Sets the trailing number of data points to calculate mean and sigma. | [optional]  if omitted the server will use the default value of 50
**consecutive** | **int** | Sets the required number of consecutive indicator data points (outliers) to trigger a violation. | [optional]  if omitted the server will use the default value of 1
**direction** | [**OutlierDirection2**](OutlierDirection2.md) |  | [optional] 
**threshold** | **float** | Sets the number of standard deviations for calculating violations. | [optional]  if omitted the server will use the default value of 3.0
**field** | **str** | The name of the field that the trigger condition will alert on. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



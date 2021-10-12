# MetricsOutlierConditionAllOf

A rule that defines how metrics monitor should evaluate outlier data and trigger notifications.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_window** | **str** | The time range used to compute the baseline. | [optional]  if omitted the server will use the default value of "1d"
**direction** | [**OutlierDirection2**](OutlierDirection2.md) |  | [optional] 
**threshold** | **float** | How much should the indicator be different from the baseline for each datapoint. | [optional]  if omitted the server will use the default value of 3.0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



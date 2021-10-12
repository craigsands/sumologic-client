# ColoringRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | Regex string to match queries to apply coloring to. | 
**single_series_aggregate_function** | **str** | Function to aggregate one series into one single value. | 
**multiple_series_aggregate_function** | **str** | Function to aggregate the aggregate values of multiple time series into one single value. | 
**color_thresholds** | [**[ColoringThreshold]**](ColoringThreshold.md) | Color thresholds. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



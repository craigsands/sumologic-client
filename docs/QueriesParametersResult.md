# QueriesParametersResult

Queries validation and extracted parameters result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** | Whether or not if queries are valid. | [optional] 
**errors** | **[str]** | Error messages from validation. | [optional]  if omitted the server will use the default value of []
**logs_outlier** | [**LogsOutlier**](LogsOutlier.md) |  | [optional] 
**metrics_outlier** | [**MetricsOutlier**](MetricsOutlier.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



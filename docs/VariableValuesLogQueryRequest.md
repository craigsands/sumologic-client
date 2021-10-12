# VariableValuesLogQueryRequest

The request to get a log query to populate variable values.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The original log query of the variable. | 
**field** | **str** | A field in log query to populate the variable values. | 
**variables_values** | [**VariablesValuesData**](VariablesValuesData.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



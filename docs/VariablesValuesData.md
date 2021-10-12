# VariablesValuesData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **{str: ([str],)}** | Data for variable values. | defaults to {}
**rich_data** | [**{str: (VariableValuesData,)}**](VariableValuesData.md) | A rich form of data for the variable search, including variable values, status and variable type. This field is different from &#x60;data&#x60; in that it includes an object instead of list as the value in the map. The &#x60;data&#x60; field is kept for backwards compatibility, please use &#x60;richData&#x60; for all usages going forward. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



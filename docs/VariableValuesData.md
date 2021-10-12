# VariableValuesData

Variable values, status, type and errors for the variable values search.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_values** | **[str]** | Values for the variable. | 
**status** | [**DashboardSearchStatus**](DashboardSearchStatus.md) |  | [optional] 
**variable_type** | **str** | The type of the variable. | [optional] 
**value_type** | **str** | The type of value of the variable. Allowed values are &#x60;String&#x60; and Any&#x60;. &#x60;String&#x60; considers as a single phrase and will wrap in double-quotes, &#x60;Any&#x60; is all characters. | [optional]  if omitted the server will use the default value of "Any"
**errors** | [**[ErrorDescription]**](ErrorDescription.md) | Generic errors returned by backend from downstream assemblies. More specific errors will be thrown in the future. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



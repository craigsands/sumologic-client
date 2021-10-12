# Variable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the variable. The variable name is case-insensitive. Only alphanumeric, and underscores are allowed in the variable name.  | 
**source_definition** | [**VariableSourceDefinition**](VariableSourceDefinition.md) |  | 
**id** | **str** | Unique identifier for the variable. | [optional] 
**display_name** | **str** | Display name of the variable shown in the UI. If this field is empty, the name field will be used. The display name is case-insensitive. Only numbers, and underscores are allowed in the variable name. This field is not yet supported by the UI.  | [optional] 
**default_value** | **str** | Default value of the variable. | [optional] 
**allow_multi_select** | **bool** | Allow multiple selections in the values dropdown. | [optional]  if omitted the server will use the default value of False
**include_all_option** | **bool** | Include an \&quot;All\&quot; option at the top of the variable&#39;s values dropdown. | [optional]  if omitted the server will use the default value of True
**hide_from_ui** | **bool** | Hide the variable in the dashboard UI. | [optional]  if omitted the server will use the default value of False
**value_type** | **str** | The type of value of the variable. Allowed values are &#x60;String&#x60; and Any&#x60;. &#x60;String&#x60; considers as a single phrase and will wrap in double-quotes, &#x60;Any&#x60; is all characters. | [optional]  if omitted the server will use the default value of "Any"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



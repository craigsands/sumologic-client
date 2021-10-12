# QueryParameterSyncDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the parameter. | 
**label** | **str** | The label of the parameter. | 
**description** | **str** | A description of the parameter. | 
**data_type** | **str** | The data type of the parameter. Supported values are:   1. &#x60;NUMBER&#x60;   2. &#x60;STRING&#x60;   3. &#x60;QUERY_FRAGMENT&#x60;   4. &#x60;SEARCH_KEYWORD&#x60; | 
**value** | **str** | A value for the parameter. Should be compatible with the type set in dataType field. | 
**auto_complete** | [**ParameterAutoCompleteSyncDefinition**](ParameterAutoCompleteSyncDefinition.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



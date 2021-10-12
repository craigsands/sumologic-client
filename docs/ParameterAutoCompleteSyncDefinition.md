# ParameterAutoCompleteSyncDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_complete_type** | **str** | The autocomplete parameter type. Supported values are:   1. &#x60;SKIP_AUTOCOMPLETE&#x60;   2. &#x60;CSV_AUTOCOMPLETE&#x60;   3. &#x60;AUTOCOMPLETE_KEY&#x60;   4. &#x60;VALUE_ONLY_AUTOCOMPLETE&#x60;   5. &#x60;VALUE_ONLY_LOOKUP_AUTOCOMPLETE&#x60;   6. &#x60;LABEL_VALUE_LOOKUP_AUTOCOMPLETE&#x60; | 
**auto_complete_key** | **str** | The autocomplete key to be used to fetch autocomplete values. | [optional] 
**auto_complete_values** | [**[AutoCompleteValueSyncDefinition]**](AutoCompleteValueSyncDefinition.md) | The array of values of the corresponding autocomplete parameter. | [optional] 
**lookup_file_name** | **str** | The lookup file to use as a source for autocomplete values. | [optional] 
**lookup_label_column** | **str** | The column from the lookup file to use for autocomplete labels. | [optional] 
**lookup_value_column** | **str** | The column from the lookup file to fill the actual value when a particular label is selected. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



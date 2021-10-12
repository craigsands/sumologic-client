# SearchQueryFieldAndType

A log field and its associated type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Log field parsed from log search query. | [optional] 
**field_type** | **str** | The type of the field inferred from log results and explicit configuration. Valid values:   1. &#x60;NumericValue&#x60;: A field with a numerical type.   2. &#x60;DistinctCount&#x60;: A field with a dimensional type. | [optional] 
**is_implicit_field** | **bool** | Indicates if the field is implicit or user defined. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



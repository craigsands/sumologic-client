# TopologySearchLabel

Topology label to search for. Each label has a key and a list of values. If a value is `*`, it means we want to match for all values of the label's key. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of a topology label to search for. | 
**value** | **str** | Value of a topology label to search for. | 
**is_required** | **bool** | Whether the content item is required to contain this label in order to be matched. If true, content items without this label will not be matched. If false, content items without this label will be matched.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



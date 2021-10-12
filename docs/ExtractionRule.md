# ExtractionRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the field extraction rule. Use a name that makes it easy to identify the rule. | 
**scope** | **str** | Scope of the field extraction rule. This could be a sourceCategory, sourceHost, or any other metadata that describes the data you want to extract from. Think of the Scope as the first portion of an ad hoc search, before the first pipe ( | ). You&#39;ll use the Scope to run a search against the rule. | 
**parse_expression** | **str** | Describes the fields to be parsed. | 
**created_at** | **datetime** | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. | 
**created_by** | **str** | Identifier of the user who created the resource. | 
**modified_at** | **datetime** | Last modification timestamp in UTC. | 
**modified_by** | **str** | Identifier of the user who last modified the resource. | 
**id** | **str** | Unique identifier for the field extraction rule. | 
**enabled** | **bool** | Is the field extraction rule enabled. | [optional]  if omitted the server will use the default value of True
**field_names** | **[str]** | List of extracted fields from \&quot;parseExpression\&quot;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



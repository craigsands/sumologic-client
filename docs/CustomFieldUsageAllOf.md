# CustomFieldUsageAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** | Identifier of the field. | 
**data_type** | **str** | Field type. Possible values are &#x60;String&#x60;, &#x60;Long&#x60;, &#x60;Int&#x60;, &#x60;Double&#x60;, &#x60;Boolean&#x60;. | 
**state** | **str** | Indicates whether the field is enabled and its values are being accepted. Possible values are &#x60;Enabled&#x60; and &#x60;Disabled&#x60;. | 
**field_extraction_rules** | **[str]** | An array of hexadecimal identifiers of field extraction rules which use this field. | [optional] 
**roles** | **[str]** | An array of hexadecimal identifiers of roles which use this field in the search filter. | [optional] 
**partitions** | **[str]** | An array of hexadecimal identifiers of partitions which use this field in the routing expression. | [optional] 
**collectors_count** | **int** | Total number of collectors using this field. | [optional] 
**sources_count** | **int** | Total number of sources using this field. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



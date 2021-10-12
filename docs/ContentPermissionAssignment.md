# ContentPermissionAssignment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_name** | **str** | Content permission name. Valid values are: &#x60;View&#x60;, &#x60;GrantView&#x60;, &#x60;Edit&#x60;, &#x60;GrantEdit&#x60;, &#x60;Manage&#x60;, and &#x60;GrantManage&#x60;. | 
**source_type** | **str** | Type of source for the permission. Valid values are: &#x60;user&#x60;, &#x60;role&#x60;, and &#x60;org&#x60;. | 
**source_id** | **str** | An identifier that belongs to the source type chosen above. For e.g. if the sourceType is set to \&quot;user\&quot;, sourceId should be identifier of a user (same goes for &#x60;role&#x60; and &#x60;org&#x60; sourceType) | 
**content_id** | **str** | Unique identifier for the content item. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



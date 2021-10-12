# PermissionSummaryMeta

Permission Summary with additional information like inheritance, revocation, etc about the permission.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the permission. Example values are: &#x60;Read&#x60;, &#x60;Update&#x60;, &#x60;Create&#x60;, etc. | 
**is_inherited** | **bool** | A true value implies that the permission is inherited from some ancestors of the resource. A false value implies that the permission is explicitly assigned to the resource. | 
**is_explicit** | **bool** | A true value implies that the permission is explicitly assigned to the resource. A false value implies that the permission is not explicitly assigned to the resource. | 
**is_revoked** | **bool** | A true value implies that the capability required for this permission has been revoked. | 
**is_recursive** | **bool** | A true value implies that the permission is recursively cascaded down to all the direct and indirect children of the resource. | 
**is_system_defined** | **bool** | A true value implies that the permission is defined by the system on the resource and can not be modified by the user. A false value implies that the permission is defined by the user on the resource and can be modified by the user. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



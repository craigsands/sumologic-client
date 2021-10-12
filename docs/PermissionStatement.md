# PermissionStatement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **[str]** | List of permissions. | 
**subject_type** | **str** | Type of subject for the permission. Valid values are: &#x60;role&#x60;. | 
**subject_id** | **str** | The identifier that belongs to the subject type chosen above. For e.g. if the subjectType is set to &#x60;role&#x60;, subjectId should be the identifier of a role. | 
**target_id** | **str** | The identifier that belongs to the resource this permission assignment applies to. | 
**created_at** | **datetime** | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. | 
**created_by** | **str** | Identifier of the user who created the resource. | 
**modified_at** | **datetime** | Last modification timestamp in UTC. | 
**modified_by** | **str** | Identifier of the user who last modified the resource. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



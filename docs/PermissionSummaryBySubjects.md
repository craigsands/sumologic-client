# PermissionSummaryBySubjects

A list of PermissionSubjects and PermissionSummaryMeta(s) associated with each subject.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_type** | **str** | Type of subject for the permission. Valid values are: &#x60;user&#x60; or &#x60;role&#x60;. | 
**subject_id** | **str** | The identifier that belongs to the subject type chosen above. For e.g. if the subjectType is set to &#x60;user&#x60;, subjectId should be the identifier of a user (same goes for &#x60;role&#x60; subjectType). | 
**permission_summaries** | [**[PermissionSummaryMeta]**](PermissionSummaryMeta.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



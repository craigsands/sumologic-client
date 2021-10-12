# UserModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the user. | 
**last_name** | **str** | Last name of the user. | 
**email** | **str** | Email address of the user. | 
**role_ids** | **[str]** | List of roleIds associated with the user. | 
**created_at** | **datetime** | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. | 
**created_by** | **str** | Identifier of the user who created the resource. | 
**modified_at** | **datetime** | Last modification timestamp in UTC. | 
**modified_by** | **str** | Identifier of the user who last modified the resource. | 
**id** | **str** | Unique identifier for the user. | 
**is_active** | **bool** | True if the user is active. | [optional] 
**is_locked** | **bool** | This has the value &#x60;true&#x60; if the user&#39;s account has been locked. If a user tries to log into their account several times and fails, his or her account will be locked for security reasons. | [optional] 
**is_mfa_enabled** | **bool** | True if multi factor authentication is enabled for the user. | [optional] 
**last_login_timestamp** | **datetime** | Timestamp of the last login for the user in UTC. Will be null if the user has never logged in. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



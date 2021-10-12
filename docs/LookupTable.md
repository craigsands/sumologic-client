# LookupTable

Lookup table definition and metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. | 
**created_by** | **str** | Identifier of the user who created the resource. | 
**modified_at** | **datetime** | Last modification timestamp in UTC. | 
**modified_by** | **str** | Identifier of the user who last modified the resource. | 
**description** | **str** | The description of the lookup table. | 
**fields** | [**[LookupTableField]**](LookupTableField.md) | The list of fields in the lookup table. | 
**primary_keys** | **[str]** | The names of the fields that make up the primary key for the lookup table. These will be a subset of the fields that the table will contain. | 
**name** | **str** | The name of the lookup table. | 
**parent_folder_id** | **str** | The parent-folder-path identifier of the lookup table in the Library. | 
**id** | **str** | Identifier of the lookup table as a content item. | 
**ttl** | **int** | A time to live for each entry in the lookup table (in minutes). 365 days is the maximum time to live for each entry that you can specify. Setting it to 0 means that the records will not expire automatically. | [optional]  if omitted the server will use the default value of 0
**size_limit_action** | **str** | The action that needs to be taken when the size limit is reached for the table. The possible values can be &#x60;StopIncomingMessages&#x60; or &#x60;DeleteOldData&#x60;. DeleteOldData will start deleting old data once size limit is reached whereas StopIncomingMessages will discard all the updates made to the lookup table once size limit is reached. | [optional]  if omitted the server will use the default value of "StopIncomingMessages"
**content_path** | **str** | Address/path of the parent folder of this lookup table in content library. For example, a lookup table existing  in the personal/lookupTable folder for user johndoe would be: /Library/Users/johndoe@acme.com/lookupTable | [optional] 
**size** | **int** | The current size of the lookup table in bytes | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



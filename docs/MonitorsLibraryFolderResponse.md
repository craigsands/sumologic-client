# MonitorsLibraryFolderResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **[str]** | Aggregated permission summary for the calling user. If detailed permission statements are required, please call list permissions endpoint. | 
**children** | [**[MonitorsLibraryBaseResponse]**](MonitorsLibraryBaseResponse.md) | Children of the folder. NOTE: Permissions field will not be filled (empty list) for children. | 
**id** | **str** | Identifier of the monitor or folder. | 
**name** | **str** | Identifier of the monitor or folder. | 
**description** | **str** | Description of the monitor or folder. | 
**version** | **int** | Version of the monitor or folder. | 
**created_at** | **datetime** | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. | 
**created_by** | **str** | Identifier of the user who created the resource. | 
**modified_at** | **datetime** | Last modification timestamp in UTC. | 
**modified_by** | **str** | Identifier of the user who last modified the resource. | 
**parent_id** | **str** | Identifier of the parent folder. | 
**content_type** | **str** | Type of the content. Valid values:   1) Monitor   2) Folder | 
**type** | **str** | Type of the object model. | 
**is_system** | **bool** | System objects are objects provided by Sumo Logic. System objects can only be localized. Non-local fields can&#39;t be updated. | 
**is_mutable** | **bool** | Immutable objects are \&quot;READ-ONLY\&quot;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



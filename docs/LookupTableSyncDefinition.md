# LookupTableSyncDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the lookup table. | 
**fields** | [**[LookupTableField]**](LookupTableField.md) | The list of fields in the lookup table. | 
**primary_keys** | **[str]** | The names of the fields that make up the primary key for the lookup table. These will be a subset of the fields that the table will contain. | 
**type** | **str** | The content item type. **Note:**  - &#x60;MewboardSyncDefinition&#x60; _is depreciated, and will soon be removed. Please use_ &#x60;DashboardV2SyncDefinition&#x60;    _instead_.  - Dashboard links are not supported for dashboards. | 
**name** | **str** | The name of the item. | 
**ttl** | **int** | A time to live for each entry in the lookup table (in minutes). 365 days is the maximum time to live for each entry that you can specify. Setting it to 0 means that the records will not expire automatically. | [optional]  if omitted the server will use the default value of 0
**size_limit_action** | **str** | The action that needs to be taken when the size limit is reached for the table. The possible values can be &#x60;StopIncomingMessages&#x60; or &#x60;DeleteOldData&#x60;. DeleteOldData will start deleting old data once size limit is reached whereas StopIncomingMessages will discard all the updates made to the lookup table once size limit is reached. | [optional]  if omitted the server will use the default value of "StopIncomingMessages"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



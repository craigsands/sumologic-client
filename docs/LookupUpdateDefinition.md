# LookupUpdateDefinition

The updated lookup table parameters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the lookup table. The description cannot be blank. | 
**ttl** | **int** | A time to live for each entry in the lookup table (in minutes). 0 is a special value. A TTL of 0 implies entry will never be deleted from the table. | defaults to 0
**size_limit_action** | **str** | The action that needs to be taken when the size limit is reached for the table. The possible values can be &#x60;StopIncomingMessages&#x60; or &#x60;DeleteOldData&#x60;. DeleteOldData will starting deleting old data once size limit is reached whereas StopIncomingMessages will discard all the updates made to the lookup table once size limit is reached. | [optional]  if omitted the server will use the default value of "StopIncomingMessages"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



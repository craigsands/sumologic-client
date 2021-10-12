# CollectionS3GetObjectAccessDeniedTracker


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracker_id** | **str** | Name that uniquely identifies the health event. It focuses on what happened rather than why. | 
**error** | **str** | Description of the underlying reason for the event change. | 
**description** | **str** | A more elaborate description of why the event occurred. | 
**event_type** | **str** | Event type. | [optional] 
**bucket_name** | **str** | The bucket name of the associated Source. | [optional] 
**access_key** | **str** | The access key used to make the request. In the case of IAM roles, this is the temporary key used for authentication. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



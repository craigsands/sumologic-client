# AsyncJobStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Whether or not the request is in progress (&#x60;InProgress&#x60;), has completed successfully (&#x60;Success&#x60;), or has completed with an error (&#x60;Failed&#x60;). | 
**status_message** | **str** | Additional status message generated if the status is not &#x60;Failed&#x60;. | [optional] 
**error** | [**ErrorDescription**](ErrorDescription.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



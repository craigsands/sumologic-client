# IngestThrottlingTracker


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracker_id** | **str** | Name that uniquely identifies the health event. It focuses on what happened rather than why. | 
**error** | **str** | Description of the underlying reason for the event change. | 
**description** | **str** | A more elaborate description of why the event occurred. | 
**event_type** | **str** | Event type. | [optional] 
**data_type** | **str** | The type of data for which the rate limit was enabled. The possible values are &#x60;LogIngest&#x60; and &#x60;MetricsIngest&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



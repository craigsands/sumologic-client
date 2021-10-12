# LogsStaticConditionAllOf

A rule that defines how logs monitor should evaluate static data and trigger notifications.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | **str** | The relative time range of the monitor. | 
**threshold_type** | [**StaticThresholdType**](StaticThresholdType.md) |  | 
**threshold** | **float** | The data value for the condition. This defines the threshold for when to trigger. Threshold value is not applicable for &#x60;MissingData&#x60; and &#x60;ResolvedMissingData&#x60; triggerTypes and will be ignored if specified. | defaults to 0.0
**field** | **str** | The name of the field that the trigger condition will alert on. The trigger could compare the value of specified field with the threshold. If &#x60;field&#x60; is not specified, monitor would default to result count instead. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



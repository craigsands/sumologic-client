# HealthEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | The unique identifier of the event. | 
**event_name** | **str** | The name of the event. | 
**details** | [**TrackerIdentity**](TrackerIdentity.md) |  | 
**resource_identity** | [**ResourceIdentity**](ResourceIdentity.md) |  | 
**event_time** | **datetime** | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. | 
**subsystem** | **str** | The product area of the event. | 
**severity_level** | **str** | The criticality of the event. It is either &#x60;Error&#x60; or &#x60;Warning&#x60; | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



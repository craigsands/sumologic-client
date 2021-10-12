# WebhookDefinitionAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL for the webhook connection. | 
**default_payload** | **str** | Default payload of the webhook. | 
**headers** | [**[Header]**](Header.md) | List of access authorization headers. | [optional]  if omitted the server will use the default value of []
**custom_headers** | [**[Header]**](Header.md) | List of custom webhook headers. | [optional]  if omitted the server will use the default value of []
**webhook_type** | [**ConnectionType**](ConnectionType.md) |  | [optional] 
**connection_subtype** | [**ConnectionSubtype**](ConnectionSubtype.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



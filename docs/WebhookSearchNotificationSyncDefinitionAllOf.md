# WebhookSearchNotificationSyncDefinitionAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** | Identifier of the webhook connection. | 
**payload** | **str** | A JSON object in the format required by the target WebHook URL. For details on variables that can be used as parameters within your JSON object, please refer to Sumo Logic Doc Hub. | [optional] 
**itemize_alerts** | **bool** | If this field is set to true, one webhook per result will be sent when the trigger conditions are met | [optional]  if omitted the server will use the default value of False
**max_itemized_alerts** | **int** | The maximum number of results for which we send separate alerts. This value should be between 1 and 100. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



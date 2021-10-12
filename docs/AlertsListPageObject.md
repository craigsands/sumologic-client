# AlertsListPageObject

Alert list page object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the alert. | [optional] 
**name** | **str** | Name of the alert. | [optional] 
**severity** | **str** | The severity of the Alert. Valid values:   1. &#x60;Critical&#x60;   2. &#x60;Warning&#x60;   3. &#x60;MissingData&#x60; | [optional] 
**status** | **str** | The status of the Alert. Valid values:   1. &#x60;Active&#x60;   2. &#x60;Resolved&#x60; | [optional] 
**entities_info** | [**[AlertEntityInfo]**](AlertEntityInfo.md) |  | [optional] 
**violation_count** | **str** | The number of unique result groups that have met the alert condition. | [optional] 
**last_violation** | **str** | The condition from the last alert violation. | [optional] 
**duration** | **str** | The current duration of the alert. | [optional] 
**created_at** | **str** | The creation time of the alert. | [optional] 
**last_updated** | **str** | The time when this alert was updated with the most recent violation. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServiceNowFieldsSyncDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The category that the event source uses to identify the event. | [optional] 
**severity** | **int** | An integer value representing the severity of the alert. Supported values are:   - &#x60;0&#x60; for Clear   - &#x60;1&#x60; for Critical   - &#x60;2&#x60; for Major   - &#x60;3&#x60; for Minor   - &#x60;4&#x60; for Warning | [optional] 
**resource** | **str** | The component on the node to which the event applies. | [optional] 
**node** | **str** | The physical or virtual device on which the event occurred. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



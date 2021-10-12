# AccountStatusResponse

Information about the account's plan and payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_model** | **str** | Whether the account is &#x60;cloudflex&#x60; or &#x60;credits&#x60; | 
**can_update_plan** | **bool** | If the plan can be updated by the given user | 
**plan_type** | **str** | Whether the account is &#x60;Free&#x60;/&#x60;Trial&#x60;/&#x60;Paid&#x60; | 
**application_use** | **str** | The current usage of the application. | 
**plan_expiration_days** | **int** | The number of days in which the plan will expire | [optional] 
**account_activated** | **bool** | If the account is activated or not | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



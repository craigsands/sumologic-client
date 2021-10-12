# CurrentPlan

Current plan of the account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | Unique identifier of the product in current plan. Valid values are: 1. &#x60;Free&#x60; 2. &#x60;Trial&#x60; 3. &#x60;Essentials&#x60; 4. &#x60;EnterpriseOps&#x60; 5. &#x60;EnterpriseSec&#x60; 6. &#x60;EnterpriseSuite&#x60;  | 
**plan_cost** | **float** | Cost incurred for the current plan. | 
**billing_frequency** | **str** | Billing frequency for the current plan. Valid values are: 1. &#x60;Monthly&#x60; 2. &#x60;Annually&#x60;  | 
**consumables** | [**[Consumable]**](Consumable.md) | Consumables in the current plan. | [optional] 
**plan_type** | **str** | Whether the account is &#x60;Free&#x60;/&#x60;Trial&#x60;/&#x60;Paid&#x60; | [optional] 
**plan_name** | **str** | The plan name for the product being used. | [optional] 
**discount_amount** | **int** | The discount offered for the given contract period. | [optional] 
**contract_period** | [**ContractPeriod**](ContractPeriod.md) |  | [optional] 
**current_billing_period** | [**CurrentBillingPeriod**](CurrentBillingPeriod.md) |  | [optional] 
**credits** | **int** | Numerical value of the amount of credits | [optional] 
**baselines** | [**Baselines**](Baselines.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



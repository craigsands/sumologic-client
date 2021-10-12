# ContractDetails

Contract details include Entitlements of the customer such as ContinuousLogs, FrequentLogs, Metrics, Storage, and Dashboards along with the entitlement value of each entitlement. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organization identifier of the account. | 
**plan_type** | **str** | Plan name of the account. | 
**entitlements** | [**[Entitlements]**](Entitlements.md) | List of the entitlements of the account. Entitlements of the account are the list of products subscribed by the user. | 
**contract_period** | [**ContractPeriod**](ContractPeriod.md) |  | 
**current_billing_period** | [**CurrentBillingPeriod**](CurrentBillingPeriod.md) |  | 
**shared_buckets** | [**[SharedBucket]**](SharedBucket.md) | Contains list of buckets. Bucket means shared pool from which multiple entitlements can use capacity. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



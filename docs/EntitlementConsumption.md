# EntitlementConsumption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_type** | **str** | String value denoting the type of entitlement. - &#x60;continuous&#x60; for Continuous Analytics, - &#x60;frequent&#x60; for Frequent Analytics, - &#x60;storage&#x60; for Total Storage, - &#x60;metrics&#x60; for Metrics. | 
**operators** | [**[Operator]**](Operator.md) | Operators used on the data. Available operators are &#x60;sum&#x60;, &#x60;average&#x60;, &#x60;usagePercentage&#x60;, &#x60;forecastValue&#x60;, &#x60;forecastPercentage&#x60;, and &#x60;forecastRemainingDays&#x60;. sum - Returns the sum of the usages. average - Returns the average of the usages. usagePercentage - Returns percentage of total capacity used for the startDate and endDate. forecastValue - Returns expected usage value assuming current usage behavior continues. forecastPercentage - Returns expected percentage usage by the endDate assuming current usage behavior continues. forecastRemainingDays- Returns the number of expected days, from today, that consumption will last assuming current usage behavior continues. | 
**contract_type** | **str** | Consumption model of the entitlements, available values are &#x60;DailyAverage&#x60;, &#x60;AnnualBucket&#x60;, and &#x60;Credits&#x60;. | 
**datapoints** | [**[DataPoints]**](DataPoints.md) | Array of data points of the entitlement with their respective date range. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



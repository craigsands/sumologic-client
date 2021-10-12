# TriggerSource

Determines which time series from queries to use for Metrics MissingData and ResolvedMissingData triggers Valid values:   1. `AllTimeSeries`: Evaluate the condition against all time series. (NOTE: This option is only valid if monitorType is `Metrics`)   2. `AnyTimeSeries`: Evaluate the condition against any time series. (NOTE: This option is only valid if monitorType is `Metrics`)   3. `AllResults`: Evaluate the condition against results from all queries. (NOTE: This option is only valid if monitorType is `Logs`)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Determines which time series from queries to use for Metrics MissingData and ResolvedMissingData triggers Valid values:   1. &#x60;AllTimeSeries&#x60;: Evaluate the condition against all time series. (NOTE: This option is only valid if monitorType is &#x60;Metrics&#x60;)   2. &#x60;AnyTimeSeries&#x60;: Evaluate the condition against any time series. (NOTE: This option is only valid if monitorType is &#x60;Metrics&#x60;)   3. &#x60;AllResults&#x60;: Evaluate the condition against results from all queries. (NOTE: This option is only valid if monitorType is &#x60;Logs&#x60;) | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SelfServiceCreditsBaselines

Details of product variables and its quantity as required for credits.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuous_ingest** | **int** | The amount of continuous logs ingest to allocate to the organization, in GBs. | [optional]  if omitted the server will use the default value of 0
**continuous_storage** | **int** | Number of days of continuous logs storage to allocate to the organization, in Days. | [optional]  if omitted the server will use the default value of 0
**metrics** | **int** | The amount of Metrics usage to allocate to the organization, in DPMs (Data Points per Minute). | [optional]  if omitted the server will use the default value of 0
**tracing_ingest** | **int** | The amount of tracing data ingest to allocate to the organization, in GBs. | [optional]  if omitted the server will use the default value of 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



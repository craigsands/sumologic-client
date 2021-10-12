# LogSearchEstimatedUsageDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_string** | **str** | Query to perform. | 
**time_range** | [**ResolvableTimeRange**](ResolvableTimeRange.md) |  | 
**timezone** | **str** | Time zone to get the estimated usage details. Follow the format in the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List).  | 
**estimated_usage_details** | [**EstimatedUsageDetails**](EstimatedUsageDetails.md) |  | 
**run_by_receipt_time** | **bool** | This has the value &#x60;true&#x60; if the search is to be run by receipt time and &#x60;false&#x60; if it is to be run by message time. | [optional]  if omitted the server will use the default value of False
**query_parameters** | [**[QueryParameterSyncDefinition]**](QueryParameterSyncDefinition.md) | Definition of the query parameters. | [optional] 
**parsing_mode** | **str** | Define the parsing mode to scan the JSON format log messages. Possible values are:   1. &#x60;AutoParse&#x60;   2. &#x60;Manual&#x60; In AutoParse mode, the system automatically figures out fields to parse based on the search query. While in the Manual mode, no fields are parsed out automatically. For more information see [Dynamic Parsing](https://help.sumologic.com/?cid&#x3D;0011). | [optional]  if omitted the server will use the default value of "Manual"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# IngestBudgetDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of the ingest budget. | 
**field_value** | **str** | Custom field value that is used to assign Collectors to the ingest budget. | 
**capacity_bytes** | **int** | Capacity of the ingest budget, in bytes. It takes a few minutes for Collectors to stop collecting when capacity is reached. We recommend setting a soft limit that is lower than your needed hard limit. | 
**timezone** | **str** | Time zone of the reset time for the ingest budget. Follow the format in the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). | 
**reset_time** | **str** | Reset time of the ingest budget in HH:MM format. | 
**action** | **str** | Action to take when ingest budget&#39;s capacity is reached. All actions are audited. Supported values are:   * &#x60;stopCollecting&#x60;   * &#x60;keepCollecting&#x60; | 
**description** | **str** | Description of the ingest budget. | [optional] 
**audit_threshold** | **int** | The threshold as a percentage of when an ingest budget&#39;s capacity usage is logged in the Audit Index. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



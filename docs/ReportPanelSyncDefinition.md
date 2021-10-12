# ReportPanelSyncDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The title of the panel. | 
**viewer_type** | **str** | Type of [area chart](https://help.sumologic.com/Dashboards-and-Alerts/Dashboards/Chart-Panel-Types). Supported values are:   1. &#x60;table&#x60; for Table   2. &#x60;bar&#x60; for Bar Chart   3. &#x60;column&#x60; for Column Chart   4. &#x60;line&#x60; for Line Chart   5. &#x60;area&#x60; for Area Chart   6. &#x60;pie&#x60; for Pie Chart   7. &#x60;svv&#x60; for Single Value Viewer   8. &#x60;title&#x60; for Title Panel   9. &#x60;text&#x60; for Text Panel  Values 1-7 are used for Data Panels. | 
**detail_level** | **int** | Supported values are:   - &#x60;1&#x60; for small   - &#x60;2&#x60; for medium   - &#x60;3&#x60; for large | 
**query_string** | **str** | The query to run, for panels associated to log searches. | 
**metrics_queries** | [**[MetricsQuerySyncDefinition]**](MetricsQuerySyncDefinition.md) | The query or queries to run, for panels associated to metrics searches. | 
**time_range** | [**ResolvableTimeRange**](ResolvableTimeRange.md) |  | 
**x** | **int** | The horizontal position of the panel. A sumo screen is divided into 24 columns. The value for x can be any integer from 0 to 24. | 
**y** | **int** | The vertical position of the panel. A sumo screen is divided into 24 rows. The value for y can be any integer from 0 to 24. | 
**width** | **int** | The width of the panel. | 
**height** | **int** | The height of the panel. | 
**properties** | **str** | Visual settings for the panel. | 
**id** | **str** | A string identifier that you can use to refer to the panel in filters.panelIds. | 
**query_parameters** | [**[QueryParameterSyncDefinition]**](QueryParameterSyncDefinition.md) | The parameters for parameterized searches. | 
**desired_quantization_in_secs** | **int** | The quantization interval aligns your time series data to common intervals on the time axis (for example every one minute) to optimize the visualization and performance. | [optional] 
**auto_parsing_info** | [**ReportAutoParsingInfo**](ReportAutoParsingInfo.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DashboardSyncDefinitionAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the dashboard. | 
**detail_level** | **int** | Supported values are:   - &#x60;1&#x60; for small   - &#x60;2&#x60; for medium   - &#x60;3&#x60; for large | 
**properties** | **str** | Visual settings for the panel. | 
**panels** | [**[ReportPanelSyncDefinition]**](ReportPanelSyncDefinition.md) | The panels of the dashboard. _Dashboard links are not supported._ | 
**filters** | [**[ReportFilterSyncDefinition]**](ReportFilterSyncDefinition.md) | The filters for the dashboard. Filters allow you to control the amount of information displayed in your dashboards. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



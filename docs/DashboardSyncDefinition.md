# DashboardSyncDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the dashboard. | 
**detail_level** | **int** | Supported values are:   - &#x60;1&#x60; for small   - &#x60;2&#x60; for medium   - &#x60;3&#x60; for large | 
**properties** | **str** | Visual settings for the panel. | 
**panels** | [**[ReportPanelSyncDefinition]**](ReportPanelSyncDefinition.md) | The panels of the dashboard. _Dashboard links are not supported._ | 
**filters** | [**[ReportFilterSyncDefinition]**](ReportFilterSyncDefinition.md) | The filters for the dashboard. Filters allow you to control the amount of information displayed in your dashboards. | 
**type** | **str** | The content item type. **Note:**  - &#x60;MewboardSyncDefinition&#x60; _is depreciated, and will soon be removed. Please use_ &#x60;DashboardV2SyncDefinition&#x60;    _instead_.  - Dashboard links are not supported for dashboards. | 
**name** | **str** | The name of the item. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



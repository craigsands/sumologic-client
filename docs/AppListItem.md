# AppListItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **str** | Type of the item. Can be &#x60;Dashboard&#x60;, &#x60;Report&#x60;, &#x60;Search&#x60;, &#x60;ScheduledSearch&#x60;, &#x60;MetricsSearch&#x60; or &#x60;Folder&#x60;. | 
**name** | **str** | Name of the item. | 
**description** | **str** | Description of the item. | [optional] 
**query** | **str** | Search query for the item. Applicable only for &#x60;Search&#x60;, &#x60;ScheduledSearch&#x60; and &#x60;MetricsSearch&#x60; itemType. | [optional] 
**screenshot_url** | **str** | URL for the screenshot of the item. Applicable only for &#x60;Dashboard&#x60; and &#x60;Report&#x60; itemType. | [optional] 
**panels** | [**[PanelItem]**](PanelItem.md) | Panels associated with the item. Applicable only for &#x60;Dashboard&#x60; and &#x60;Report&#x60; itemType. | [optional] 
**children** | [**[AppListItem]**](AppListItem.md) | Child content items. Applicable only for &#x60;Folder&#x60; itemType. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



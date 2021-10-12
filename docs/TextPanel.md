# TextPanel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text to display in the panel. | 
**key** | **str** | Key for the panel. Used to create searches for the queries in the panel and configure the layout of the panel in the dashboard.  | 
**panel_type** | **str** | Type of panel. | 
**id** | **str** | Unique identifier for the panel. | [optional] 
**title** | **str** | Title of the panel. | [optional] 
**visual_settings** | **str** | Visual settings of the panel. | [optional] 
**keep_visual_settings_consistent_with_parent** | **bool** | Keeps the visual settings, like series colors, consistent with the settings of the parent panel. | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



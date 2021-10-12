# SumoSearchPanel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**[Query]**](Query.md) | Metrics and log queries of the panel. | 
**key** | **str** | Key for the panel. Used to create searches for the queries in the panel and configure the layout of the panel in the dashboard.  | 
**panel_type** | **str** | Type of panel. | 
**description** | **str** | Description of the panel. | [optional] 
**time_range** | [**ResolvableTimeRange**](ResolvableTimeRange.md) |  | [optional] 
**coloring_rules** | [**[ColoringRule]**](ColoringRule.md) | Rules to set the color of data. | [optional] 
**linked_dashboards** | [**[LinkedDashboard]**](LinkedDashboard.md) | List of linked dashboards. | [optional] 
**id** | **str** | Unique identifier for the panel. | [optional] 
**title** | **str** | Title of the panel. | [optional] 
**visual_settings** | **str** | Visual settings of the panel. | [optional] 
**keep_visual_settings_consistent_with_parent** | **bool** | Keeps the visual settings, like series colors, consistent with the settings of the parent panel. | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



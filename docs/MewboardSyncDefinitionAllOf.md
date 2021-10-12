# MewboardSyncDefinitionAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the dashboard. | 
**description** | **str** | A description of the dashboard. | [optional] 
**root_panel** | [**ContainerPanel**](ContainerPanel.md) |  | [optional] 
**theme** | **str** | Theme for the dashboard. Must be &#x60;light&#x60; or &#x60;dark&#x60;. | [optional]  if omitted the server will use the default value of "light"
**topology_label_map** | [**TopologyLabelMap**](TopologyLabelMap.md) |  | [optional] 
**refresh_interval** | **int** | Interval of time (in seconds) to automatically refresh the dashboard. A value of 0 means we never automatically refresh the dashboard. | [optional] 
**time_range** | [**ResolvableTimeRange**](ResolvableTimeRange.md) |  | [optional] 
**layout** | [**Layout**](Layout.md) |  | [optional] 
**panels** | [**[Panel]**](Panel.md) | Children panels that the container panel contains. | [optional] 
**variables** | [**[Variable]**](Variable.md) | Variables that could be applied to the panel&#39;s children. | [optional] 
**coloring_rules** | [**[ColoringRule]**](ColoringRule.md) | Coloring rules to color the panel/data with. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



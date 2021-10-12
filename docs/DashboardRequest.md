# DashboardRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the dashboard. | 
**time_range** | [**ResolvableTimeRange**](ResolvableTimeRange.md) |  | 
**description** | **str** | Description of the dashboard. | [optional] 
**folder_id** | **str** | The identifier of the folder to save the dashboard in. By default it is saved in your personal folder.  | [optional] 
**topology_label_map** | [**TopologyLabelMap**](TopologyLabelMap.md) |  | [optional] 
**domain** | **str** | If set denotes that the dashboard concerns a given domain (e.g. &#x60;aws&#x60;, &#x60;k8s&#x60;, &#x60;app&#x60;). | [optional]  if omitted the server will use the default value of ""
**refresh_interval** | **int** | Interval of time (in seconds) to automatically refresh the dashboard. A value of 0 means we never automatically refresh the dashboard. Allowed values are &#x60;0&#x60;, &#x60;30&#x60;, &#x60;60&#x60;, 120&#x60;, &#x60;300&#x60;, &#x60;900&#x60;, &#x60;3600&#x60;, &#x60;86400&#x60;.  | [optional] 
**panels** | [**[Panel]**](Panel.md) | Panels in the dashboard. | [optional] 
**layout** | [**Layout**](Layout.md) |  | [optional] 
**variables** | [**[Variable]**](Variable.md) | Variables to apply to the panels. | [optional] 
**theme** | **str** | Theme for the dashboard. Either &#x60;Light&#x60; or &#x60;Dark&#x60;. | [optional]  if omitted the server will use the default value of "Light"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CSEWindowsWriteQueueFilesToSensorDirectoryFailedTracker


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracker_id** | **str** | Name that uniquely identifies the health event. It focuses on what happened rather than why. | 
**error** | **str** | Description of the underlying reason for the event change. | 
**description** | **str** | A more elaborate description of why the event occurred. | 
**event_type** | **str** | Event type. | [optional] 
**sensor_id** | **str** | The sensor ID. | [optional] 
**sensor_hostname** | **str** | The sensor&#39;s hostname. | [optional] 
**sensor_user_name** | **str** | The sensor&#39;s user name. | [optional] 
**folder_path** | **str** | The path of the folder. | [optional] 
**file_path** | **str** | The complete file path. | [optional] 
**source** | **str** | The HostName + EventLog name for EventLogs and Domain name for Directory.. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AppInstallRequest

JSON object containing name, description, destinationFolderId, and dataSourceType.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Preferred name of the app to be installed. This will be the name of the app in the selected installation folder. | 
**description** | **str** | Preferred description of the app to be installed. This will be displayed as the app description in the selected installation folder. | 
**destination_folder_id** | **str** | Identifier of the folder in which the app will be installed in hexadecimal format. | 
**data_source_values** | **{str: (str,)}** | Dictionary of properties specifying log-source name and value. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AlertsLibraryBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the alert or folder. | 
**type** | **str** | Type of the object model. Valid values:   1) AlertsLibraryAlert   2) AlertsLibraryFolder | 
**description** | **str** | Description of the alert or folder. | [optional]  if omitted the server will use the default value of ""
**is_locked** | **bool** | Locking/Unlocking requires the &#x60;LockAlerts&#x60; capability. Locked objects can only be &#x60;Localized&#x60;. Updating or moving requires unlocking the object. Locking/Unlocking recursively locks all of the objects children. All children of a locked object must be locked. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



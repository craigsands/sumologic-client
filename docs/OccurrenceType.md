# OccurrenceType

The criteria to evaluate the threshold and thresholdType in the given time range. Valid values:   1. `AtLeastOnce`: Trigger if the threshold is met at least once. (NOTE: This is the only valid value if monitorType is `Metrics`.)   2. `Always`: Trigger if the threshold is met continuously. (NOTE: This is the only valid value if monitorType is `Metrics`.)   3. `ResultCount`: Trigger if the threshold is met against the count of results. (NOTE: This is the only valid value if monitorType is `Logs`.)   4. `MissingData`: Trigger if the data is missing. (NOTE: This is valid for both `Logs` and `Metrics` monitorTypes)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The criteria to evaluate the threshold and thresholdType in the given time range. Valid values:   1. &#x60;AtLeastOnce&#x60;: Trigger if the threshold is met at least once. (NOTE: This is the only valid value if monitorType is &#x60;Metrics&#x60;.)   2. &#x60;Always&#x60;: Trigger if the threshold is met continuously. (NOTE: This is the only valid value if monitorType is &#x60;Metrics&#x60;.)   3. &#x60;ResultCount&#x60;: Trigger if the threshold is met against the count of results. (NOTE: This is the only valid value if monitorType is &#x60;Logs&#x60;.)   4. &#x60;MissingData&#x60;: Trigger if the data is missing. (NOTE: This is valid for both &#x60;Logs&#x60; and &#x60;Metrics&#x60; monitorTypes) | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



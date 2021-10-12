# NotificationThresholdSyncDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_type** | **str** | Threshold type. Possible values are:  1. &#x60;message&#x60;  2. &#x60;group&#x60;  Use &#x60;group&#x60; as threshold type if the search query is of aggregate type. For non-aggregate queries, set it to &#x60;message&#x60;. | 
**operator** | **str** | Criterion to be applied when comparing actual result count with expected count. Possible values are:  1. &#x60;eq&#x60;  2. &#x60;gt&#x60;  3. &#x60;ge&#x60;  4. &#x60;lt&#x60;  5. &#x60;le&#x60; | 
**count** | **int** | Expected result count. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



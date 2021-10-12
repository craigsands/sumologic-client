# StaticThresholdType

The comparison type for the `threshold` evaluation. This defines how you want the data value compared. Valid values:   1. `LessThan`: Less than than the configured threshold.   2. `GreaterThan`: Greater than the configured threshold.   3. `LessThanOrEqual`: Less than or equal to the configured threshold.   4. `GreaterThanOrEqual`: Greater than or equal to the configured threshold. ThresholdType value is not applicable for `MissingData` and `ResolvedMissingData` triggerTypes and will be ignored if specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The comparison type for the &#x60;threshold&#x60; evaluation. This defines how you want the data value compared. Valid values:   1. &#x60;LessThan&#x60;: Less than than the configured threshold.   2. &#x60;GreaterThan&#x60;: Greater than the configured threshold.   3. &#x60;LessThanOrEqual&#x60;: Less than or equal to the configured threshold.   4. &#x60;GreaterThanOrEqual&#x60;: Greater than or equal to the configured threshold. ThresholdType value is not applicable for &#x60;MissingData&#x60; and &#x60;ResolvedMissingData&#x60; triggerTypes and will be ignored if specified. | defaults to "GreaterThanOrEqual"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



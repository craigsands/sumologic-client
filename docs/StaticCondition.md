# StaticCondition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | **str** | The relative time range of the monitor. | 
**occurrence_type** | [**OccurrenceType**](OccurrenceType.md) |  | 
**trigger_source** | [**TriggerSource**](TriggerSource.md) |  | 
**trigger_type** | **str** | The type of trigger condition. Valid values:   1. &#x60;Critical&#x60;: A critical condition to trigger on.   2. &#x60;Warning&#x60;: A warning condition to trigger on.   3. &#x60;MissingData&#x60;: A condition that indicates data is missing.   4. &#x60;ResolvedCritical&#x60;: A condition to resolve a Critical trigger on.   5. &#x60;ResolvedWarning&#x60;: A condition to resolve a Warning trigger on.   6. &#x60;ResolvedMissingData&#x60;: A condition to resolve a MissingData trigger. | 
**threshold** | **float** | The data value for the condition. This defines the threshold for when to trigger. Threshold value is not applicable for &#x60;MissingData&#x60; and &#x60;ResolvedMissingData&#x60; triggerTypes and will be ignored if specified. | [optional]  if omitted the server will use the default value of 0.0
**threshold_type** | [**StaticThresholdType**](StaticThresholdType.md) |  | [optional] 
**field** | **str** | The name of the field that the trigger condition will alert on. The trigger could compare the value of specified field with the threshold. If &#x60;field&#x60; is not specified, monitor would default to result count instead. | [optional] 
**detection_method** | **str** | Detection method of the trigger condition. Valid values:   1. &#x60;StaticCondition&#x60;: A condition that triggers based off of a static threshold.   2. &#x60;LogsStaticCondition&#x60;: A logs condition that triggers based off of a static threshold. Currently LogsStaticCondition is available in closed beta (Notify your Sumo Logic representative in order to get the early access).   3. &#x60;MetricsStaticCondition&#x60;: A metrics condition that triggers based off of a static threshold. Currently MetricsStaticCondition is available in closed beta (Notify your Sumo Logic representative in order to get the early access).   4. &#x60;LogsOutlierCondition&#x60;: A logs condition that triggers based off of a dynamic outlier threshold. Currently LogsOutlierCondition is available in closed beta (Notify your Sumo Logic representative in order to get the early access).   5. &#x60;MetricsOutlierCondition&#x60;: A metrics condition that triggers based off of a dynamic outlier threshold. Currently MetricsOutlierCondition is available in closed beta (Notify your Sumo Logic representative in order to get the early access).   6. &#x60;LogsMissingDataCondition&#x60;: A logs missing data condition that triggers based off of no data available. Currently LogsMissingDataCondition is available in closed beta (Notify your Sumo Logic representative in order to get the early access).   7. &#x60;MetricsMissingDataCondition&#x60;: A metrics missing data condition that triggers based off of no data available. Currently MetricsMissingDataCondition is available in closed beta (Notify your Sumo Logic representative in order to get the early access). | [optional]  if omitted the server will use the default value of "StaticCondition"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



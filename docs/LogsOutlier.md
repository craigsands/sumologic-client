# LogsOutlier

The parameters extracted from the logs outlier query.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trimmed_query** | **str** | The query string after trimming out the outlier clause. | [optional] 
**window** | **int** | Sets the trailing number of data points to calculate mean and sigma. | [optional]  if omitted the server will use the default value of 10
**consecutive** | **int** | Sets the required number of consecutive indicator data points (outliers) to trigger a violation. | [optional]  if omitted the server will use the default value of 1
**direction** | **str** | Specifies which direction should trigger violations. Valid values:   1. &#x60;Both&#x60;: Both positive and negative deviations   2. &#x60;Up&#x60;: Positive deviations only   3. &#x60;Down&#x60;: Negative deviations only example: \&quot;Up\&quot; pattern: \&quot;^(Both|Up|Down)$\&quot; default: \&quot;Both\&quot; x-pattern-message: \&quot;should be one of the following: &#39;Both&#39;, &#39;Up&#39;, &#39;Down&#39;\&quot; | [optional] 
**threshold** | **float** | Sets the number of standard deviations for calculating violations. | [optional]  if omitted the server will use the default value of 3.0
**field** | **str** | The name of the field that the trigger condition will alert on. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MetricsQueryRow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **str** | Row id for the query row, A to Z letter. | 
**query** | **str** | A metric query consists of a metric, one or more filters and optionally, one or more [Metrics Operators](https://help.sumologic.com/?cid&#x3D;10144). Strictly speaking, both filters and operators are optional.  Most of the [Metrics Operators](https://help.sumologic.com/?cid&#x3D;10144) are allowed in the query string except &#x60;fillmissing&#x60;, &#x60;outlier&#x60;, &#x60;quantize&#x60; and &#x60;timeshift&#x60;.    * &#x60;fillmissing&#x60;: Not supported in API.   * &#x60;outlier&#x60;: Not supported in API.   * &#x60;quantize&#x60;: Only supported through &#x60;quantization&#x60; param.   * &#x60;timeshift&#x60;: Only supported through &#x60;timeshift&#x60; param.   In practice, your metric queries will almost always contain filters that narrow the scope of your query. For more information about the query language see [Metrics Queries](http://help.sumologic.com/?cid&#x3D;1079). | 
**quantization** | **int** | Segregates time series data by time period. This allows you to create aggregated results in buckets of fixed intervals (for example, 5-minute intervals). The value is in milliseconds. | [optional] 
**rollup** | **str** | We use the term rollup to refer to the aggregation function Sumo Logic uses when quantizing metrics. Can be &#x60;Avg&#x60;, &#x60;Sum&#x60;, &#x60;Min&#x60;, &#x60;Max&#x60;, &#x60;Count&#x60; or &#x60;None&#x60;. | [optional] 
**timeshift** | **int** | Shifts the time series from your metrics query by the specified amount of time. This can help when comparing a time series across multiple time periods. Specified as a signed duration in milliseconds. | [optional] 
**transient** | **bool** | Determines if the row should be returned in the response. Can be used in conjunction with a join, if only the result of the join is needed, and not the intermediate rows. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



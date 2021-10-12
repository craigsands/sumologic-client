# RelativeTimeRangeBoundary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relative_time** | **str** | Relative time as a string consisting of following elements: - &#x60;-&#x60; (optional): minus sign indicates time in the past, - &#x60;&lt;number&gt;&#x60;: number of time units, - &#x60;&lt;time_unit&gt;&#x60;: time unit; possible values are: &#x60;w&#x60; (week), &#x60;d&#x60; (day), &#x60;h&#x60; (hour), &#x60;m&#x60; (minute), &#x60;s&#x60; (second). Multiple pairs of &#x60;&lt;number&gt;&lt;time_unit&gt;&#x60; may be provided, and they may be in any order. For example, &#x60;-2w5d3h&#x60; points to the moment in time 2 weeks, 5 days and 3 hours ago. | 
**type** | **str** | Type of the time range boundary. Value must be from list: - &#x60;RelativeTimeRangeBoundary&#x60;, - &#x60;EpochTimeRangeBoundary&#x60;, - &#x60;Iso8601TimeRangeBoundary&#x60;, - &#x60;LiteralTimeRangeBoundary&#x60;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



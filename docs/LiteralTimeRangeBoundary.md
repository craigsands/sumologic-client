# LiteralTimeRangeBoundary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range_name** | **str** | Name of the time range. Possible values are:   - &#x60;now&#x60;,   - &#x60;second&#x60;,   - &#x60;minute&#x60;,   - &#x60;hour&#x60;,   - &#x60;day&#x60;,   - &#x60;today&#x60;,   - &#x60;week&#x60;,   - &#x60;month&#x60;,   - &#x60;year&#x60; | 
**type** | **str** | Type of the time range boundary. Value must be from list: - &#x60;RelativeTimeRangeBoundary&#x60;, - &#x60;EpochTimeRangeBoundary&#x60;, - &#x60;Iso8601TimeRangeBoundary&#x60;, - &#x60;LiteralTimeRangeBoundary&#x60;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



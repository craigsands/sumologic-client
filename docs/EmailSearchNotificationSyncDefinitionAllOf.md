# EmailSearchNotificationSyncDefinitionAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_list** | **[str]** | A list of email recipients. | 
**subject_template** | **str** | If the notification is scheduled with a threshold, the default subject template will be \&quot;Search Alert: {{AlertCondition}} results found for {{SearchName}}\&quot;. For email notifications without a threshold, the default subject template is \&quot;Search Results: {{SearchName}}\&quot;. | [optional] 
**include_query** | **bool** | A boolean value to indicate if the search query should be included in the notification email. | [optional]  if omitted the server will use the default value of True
**include_result_set** | **bool** | A boolean value to indicate if the search result set should be included in the notification email. | [optional]  if omitted the server will use the default value of True
**include_histogram** | **bool** | A boolean value to indicate if the search result histogram should be included in the notification email. | [optional]  if omitted the server will use the default value of True
**include_csv_attachment** | **bool** | A boolean value to indicate if the search results should be included in the notification email as a CSV attachment. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



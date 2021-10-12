# SearchScheduleSyncDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parseable_time_range** | [**ResolvableTimeRange**](ResolvableTimeRange.md) |  | 
**time_zone** | **str** | Time zone identifier for time specification. Either an abbreviation such as \&quot;PST\&quot;, a full name such as \&quot;America/Los_Angeles\&quot;, or a custom ID such as \&quot;GMT-8:00\&quot;. Note that the support of abbreviations is for JDK 1.1.x compatibility only and full names should be used. | 
**notification** | [**ScheduleNotificationSyncDefinition**](ScheduleNotificationSyncDefinition.md) |  | 
**schedule_type** | **str** | Run schedule of the scheduled search. Set to \&quot;Custom\&quot; to specify the schedule with a CRON expression. Possible schedule types are:   - &#x60;RealTime&#x60;   - &#x60;15Minutes&#x60;   - &#x60;1Hour&#x60;   - &#x60;2Hours&#x60;   - &#x60;4Hours&#x60;   - &#x60;6Hours&#x60;   - &#x60;8Hours&#x60;   - &#x60;12Hours&#x60;   - &#x60;1Day&#x60;   - &#x60;1Week&#x60;   - &#x60;Custom&#x60; | 
**parameters** | [**[ScheduleSearchParameterSyncDefinition]**](ScheduleSearchParameterSyncDefinition.md) | A list of scheduled search parameters. | 
**cron_expression** | **str** | Cron-like expression specifying the search&#39;s schedule. Field scheduleType must be set to \&quot;Custom\&quot;, otherwise, scheduleType takes precedence over cronExpression. | [optional] 
**displayable_time_range** | **str** | A human-friendly text describing the query time range. For e.g. \&quot;-2h\&quot;, \&quot;last three days\&quot;, \&quot;team default time\&quot; | [optional] 
**threshold** | [**NotificationThresholdSyncDefinition**](NotificationThresholdSyncDefinition.md) |  | [optional] 
**mute_error_emails** | **bool** | If enabled, emails are not sent out in case of errors with the search. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Email


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **[str]** | A list of email addresses to send to when the rule fires. | 
**subject** | **str** | The subject line of the email. | 
**time_zone** | **str** | Time zone for the email content. All dates/times will be displayed in this timeZone in the email payload. Follow the format in the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). | 
**connection_type** | **str** | Connection type of the connection. Valid values:   1.  &#x60;Email&#x60;   2.  &#x60;AWSLambda&#x60;   3.  &#x60;AzureFunctions&#x60;   4.  &#x60;Datadog&#x60;   5.  &#x60;HipChat&#x60;   6.  &#x60;Jira&#x60;   7.  &#x60;NewRelic&#x60;   8.  &#x60;Opsgenie&#x60;   9.  &#x60;PagerDuty&#x60;   10. &#x60;Slack&#x60;   11. &#x60;MicrosoftTeams&#x60;   12. &#x60;ServiceNow&#x60;   13. &#x60;SumoCloudSOAR&#x60;   14. &#x60;Webhook&#x60; | 
**message_body** | **str** | The message body of the email to send. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



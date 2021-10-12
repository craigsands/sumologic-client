# PasswordPolicy

Password Policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_length** | **int** | The minimum length of the password. | [optional]  if omitted the server will use the default value of 8
**max_length** | **int** | The maximum length of the password. (Setting this to any value other than 128 is no longer supported; this field may be deprecated in the future.) | [optional]  if omitted the server will use the default value of 128
**must_contain_lowercase** | **bool** | If the password must contain lower case characters. | [optional]  if omitted the server will use the default value of True
**must_contain_uppercase** | **bool** | If the password must contain upper case characters. | [optional]  if omitted the server will use the default value of True
**must_contain_digits** | **bool** | If the password must contain digits. | [optional]  if omitted the server will use the default value of True
**must_contain_special_chars** | **bool** | If the password must contain special characters. | [optional]  if omitted the server will use the default value of True
**max_password_age_in_days** | **int** | Maximum number of days that a password can be used before user is required to change it. Put -1 if the user should not have to change their password. | [optional]  if omitted the server will use the default value of 365
**min_unique_passwords** | **int** | The minimum number of unique new passwords that a user must use before an old password can be reused. | [optional]  if omitted the server will use the default value of 10
**account_lockout_threshold** | **int** | Number of failed login attempts allowed before account is locked-out. | [optional]  if omitted the server will use the default value of 6
**failed_login_reset_duration_in_mins** | **int** | The duration of time in minutes that must elapse from the first failed login attempt after which failed login count is reset to 0. | [optional]  if omitted the server will use the default value of 10
**account_lockout_duration_in_mins** | **int** | The duration of time in minutes that a locked-out account remained locked before getting unlocked automatically. | [optional]  if omitted the server will use the default value of 30
**require_mfa** | **bool** | If MFA should be required to log in. By default, this field is set to &#x60;false&#x60;. | [optional]  if omitted the server will use the default value of False
**remember_mfa** | **bool** | If MFA should be remembered on the browser. | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SamlIdentityProviderRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_name** | **str** | Name of the SSO policy or another name used to describe the policy internally. | 
**issuer** | **str** | The unique URL assigned to the organization by the SAML Identity Provider. | 
**x509cert1** | **str** | The certificate is used to verify the signature in SAML assertions. | 
**sp_initiated_login_path** | **str** | This property has been deprecated and is no longer used. | [optional]  if omitted the server will use the default value of ""
**sp_initiated_login_enabled** | **bool** | True if Sumo Logic redirects users to your identity provider with a SAML AuthnRequest when signing in. | [optional]  if omitted the server will use the default value of False
**authn_request_url** | **str** | The URL that the identity provider has assigned for Sumo Logic to submit SAML authentication requests to the identity provider. | [optional]  if omitted the server will use the default value of ""
**x509cert2** | **str** | The backup certificate used to verify the signature in SAML assertions when x509cert1 expires. | [optional]  if omitted the server will use the default value of ""
**x509cert3** | **str** | The backup certificate used to verify the signature in SAML assertions when x509cert1 expires and x509cert2 is empty. | [optional]  if omitted the server will use the default value of ""
**on_demand_provisioning_enabled** | [**OnDemandProvisioningInfo**](OnDemandProvisioningInfo.md) |  | [optional] 
**roles_attribute** | **str** | The role that Sumo Logic will assign to users when they sign in. | [optional]  if omitted the server will use the default value of ""
**logout_enabled** | **bool** | True if users are redirected to a URL after signing out of Sumo Logic. | [optional]  if omitted the server will use the default value of False
**logout_url** | **str** | The URL that users will be redirected to after signing out of Sumo Logic. | [optional]  if omitted the server will use the default value of ""
**email_attribute** | **str** | The email address of the new user account. | [optional]  if omitted the server will use the default value of ""
**debug_mode** | **bool** | True if additional details are included when a user fails to sign in. | [optional]  if omitted the server will use the default value of False
**sign_authn_request** | **bool** | True if Sumo Logic will send signed Authn requests to the identity provider. | [optional]  if omitted the server will use the default value of False
**disable_requested_authn_context** | **bool** | True if Sumo Logic will include the RequestedAuthnContext element of the SAML AuthnRequests it sends to the identity provider. | [optional]  if omitted the server will use the default value of False
**is_redirect_binding** | **bool** | True if the SAML binding is of HTTP Redirect type. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



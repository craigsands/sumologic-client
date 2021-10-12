# AppManifest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the app. | 
**hover_text** | **str** | Text to be displayed when hovered over in UI. | 
**icon_url** | **str** | App icon URL. | 
**family** | **str** | The app family | [optional] 
**categories** | **[str]** | Categories that the app belongs to. | [optional] 
**screenshot_urls** | **[str]** | App screenshot URLs. | [optional] 
**help_url** | **str** | App help page URL. | [optional] 
**help_doc_id_map** | **{str: (str,)}** | the IDs of the docs pages for this app | [optional] 
**community_url** | **str** | App community page URL. | [optional] 
**requirements** | **[str]** | Requirements for the app. | [optional] 
**account_types** | **[str]** | Account types that are allowed to install the app | [optional] 
**requires_installation_instructions** | **bool** | Indicates whether installation instructions are required or not. | [optional] 
**installation_instructions** | **str** | Installation instructions for the app. | [optional] 
**parameters** | [**[ServiceManifestDataSourceParameter]**](ServiceManifestDataSourceParameter.md) | Content identifier of the app. | [optional] 
**author** | **str** | App author. | [optional] 
**author_website** | **str** | App author website URL. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Error


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error codes:  * &#x60;INTERNAL_ERROR&#x60; - Please contact the Prompt Wiz team for further support  * &#x60;INVALID_JSON&#x60; - The request body received is not a valid JSON object  * &#x60;PROMPT_DOES_NOT_EXIST&#x60; - No prompt associated with the given prompt ID  * &#x60;PROMPT_NOT_LIVE&#x60; - The prompt does not have an associated live prompt version  * &#x60;MISSING_MSG_VARIABLES&#x60; - Required values not provided for prompt variable(s)  * &#x60;MISSING_API_KEY&#x60; - Missing the &#x60;apiKey&#x60; parameter required to access PromptWiz. Please check the API Keys page on the PromptWiz web application  * &#x60;INVALID_API_KEY&#x60; - The API key provided is not valid. Please check the API Keys page on the PromptWiz web application  * &#x60;MISSING_MODEL_API_KEY&#x60; - An API key associated with your organisation to query the model has not been provided. Please provide the model API key using the API Keys page on the PromptWiz web application  * &#x60;MISSING_LINK_ID&#x60; - All queries must include the &#x60;linkId&#x60; parameter if one is provided in any query  * &#x60;DUPLICATE_LINK_ID&#x60; - The &#x60;linkId&#x60; parameter must be unique across all queries in a query set  * &#x60;MISSING_QUERY_SET&#x60; - The request does not contain a query set  * &#x60;ICORRECT_JSON_QUERY_SET&#x60; - The query set provided is not valid json  * &#x60;FAILED_MODEL_EVALUATION_SET&#x60; - Failed to query the model for some or all of the items in the query set. Set the &#x60;acceptPartial&#x60; parameter to &#x60;true&#x60; to receive partial result sets  * &#x60;FAILED_MODEL_EVALUATION&#x60; - Failed to query the model for an item | 
**description** | **str** |  | 

## Example

```python
from openapi_client.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print Error.to_json()

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_form_dict = error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



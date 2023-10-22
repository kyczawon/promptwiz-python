# QueryFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_id** | **int** | The ID of the prompt, available on the PromptWiz web application | 
**variables** | **Dict[str, str]** | A JSON of key-value pairs.&lt;br /&gt;&lt;br /&gt;  The keys are the prompt variables and the values are their assigned values.&lt;br /&gt;&lt;br /&gt;  A value must be assigned to every prompt parameter.&lt;br /&gt;&lt;br /&gt;  **This field can be omitted only if the prompt has no parameters.**&lt;br /&gt;&lt;br /&gt; | [optional] 
**link_id** | **int** | An ID used to link a result in the response to a query in the request. This simplifies matching request on your backend if you’re making more than 1 request at a time.&lt;br /&gt;&lt;br /&gt;  If this field is omitted, PromptWiz will assign each query its index as the link ID.&lt;br /&gt;&lt;br /&gt;  If this field is provided in any query in the query set, it must be provided on all.&lt;br /&gt;&lt;br /&gt;  If this field is provided in the queries, it must be unique across the queries.&lt;br /&gt;&lt;br /&gt; | [optional] 
**model_api_key** | **str** | An API key for the model service (e.g. OpenAI) to be queried. This allows for an override to the organisation’s API key saved under the [api_keys](https://promptwiz.co.uk/api_keys/) page. Please keep in mind if this parameter is used, the value may have to be updated if the model service is changed in a newer prompt version. | [optional] 
**result_size** | **int** | The number of results to generate. | [optional] 

## Example

```python
from openapi_client.models.query_fields import QueryFields

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFields from a JSON string
query_fields_instance = QueryFields.from_json(json)
# print the JSON string representation of the object
print QueryFields.to_json()

# convert the object into a dict
query_fields_dict = query_fields_instance.to_dict()
# create an instance of QueryFields from a dict
query_fields_form_dict = query_fields.from_dict(query_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Request


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | PromptWiz API Key available under [api_keys](https://promptwiz.co.uk/api_keys/) page | 
**query_set** | [**List[QueryFields]**](QueryFields.md) |  | 
**stream** | **bool** | Indicates whether the model output should be streamed.&lt;br /&gt;&lt;br /&gt; | [optional] [default to False]
**accept_partial** | **bool** | Indicates whether partially successful queries can be returned. When set to false the response will fail if ANY query for querySet fails.&lt;br /&gt;&lt;br /&gt;  **For streaming this input is unused.** | [optional] [default to False]

## Example

```python
from openapi_client.models.request import Request

# TODO update the JSON string below
json = "{}"
# create an instance of Request from a JSON string
request_instance = Request.from_json(json)
# print the JSON string representation of the object
print Request.to_json()

# convert the object into a dict
request_dict = request_instance.to_dict()
# create an instance of Request from a dict
request_form_dict = request.from_dict(request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



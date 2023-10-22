# Result


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_id** | **int** | The ID of the prompt, available on the PromptWiz web application | 
**prompt_id** | **int** | The ID of the prompt, available on the PromptWiz web application | 
**prompt_version_number** | **int** | The version of the prompt used, available on the PromptWiz web application | 
**results** | **Dict[str, str]** | The model responses indexed by choice as specified by results_size input parameter&lt;br /&gt;&lt;br /&gt;  **streaming:** the results will contain the deltas sent over by the model | 
**time** | **float** | The time the model evaluation took in seconds | 
**input_spend** | **float** | The cost of the input for the model evaluation in the model’s cost units (e.g. tokens) | 
**choices_spend** | **Dict[str, float]** | The cost of each choice output indexed by the same choices index as results.&lt;br /&gt;&lt;br /&gt;  **streaming:** this contains the accumulated cost up to and including the current delta in envelope | 
**output_spend** | **float** | The total cost of the output for the model evaluation in the model’s cost units (e.g. tokens). The sum of outputSpend equals&lt;br /&gt;&lt;br /&gt;  **streaming:** this contains the accumulated total cost. | 

## Example

```python
from openapi_client.models.result import Result

# TODO update the JSON string below
json = "{}"
# create an instance of Result from a JSON string
result_instance = Result.from_json(json)
# print the JSON string representation of the object
print Result.to_json()

# convert the object into a dict
result_dict = result_instance.to_dict()
# create an instance of Result from a dict
result_form_dict = result.from_dict(result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



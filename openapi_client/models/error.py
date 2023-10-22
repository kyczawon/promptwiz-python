# coding: utf-8

"""
    PromptWiz API - OpenAPI 3.1

    ### Context PromptWiz API provides a way to execute prompts defined in the UI. The API will return the results from OpenAI with fields populated based on your inputs and the result will be stored in PromptWiz for the purpose of analysis  ### Pre-requisites 1. You must create a prompt, and prompt version (and save it) 2. A prompt version must be set as ‘active’ in the prompt page 3. You must have a Open API Key set under api_keys page ## API modes 1. **Full result** - when stream is False, the API returns a single JSON response with the outcome of each query from querySet.     - Multiple requests are done in concurrent fashion for optimal response times 2. **Streaming** - when stream is True, the API returns multiple JSON responses through a Streaming response. The response body will have the exact same envelope as the full result mode, with the only difference being that the results field will contain the deltas that have been streamed by the model.     - Multiple requests are done in concurrent fashion & the streams will return on ‘first come first served’ basis. This means that envelopes might arrive out of order and you should rely on linkid to combine responses correctly.

    The version of the OpenAPI document: 0.1
    Contact: contact@promptwiz.co.uk
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class Error(BaseModel):
    """
    Error
    """
    code: StrictStr = Field(..., description="Error codes:  * `INTERNAL_ERROR` - Please contact the Prompt Wiz team for further support  * `INVALID_JSON` - The request body received is not a valid JSON object  * `PROMPT_DOES_NOT_EXIST` - No prompt associated with the given prompt ID  * `PROMPT_NOT_LIVE` - The prompt does not have an associated live prompt version  * `MISSING_MSG_VARIABLES` - Required values not provided for prompt variable(s)  * `MISSING_API_KEY` - Missing the `apiKey` parameter required to access PromptWiz. Please check the API Keys page on the PromptWiz web application  * `INVALID_API_KEY` - The API key provided is not valid. Please check the API Keys page on the PromptWiz web application  * `MISSING_MODEL_API_KEY` - An API key associated with your organisation to query the model has not been provided. Please provide the model API key using the API Keys page on the PromptWiz web application  * `MISSING_LINK_ID` - All queries must include the `linkId` parameter if one is provided in any query  * `DUPLICATE_LINK_ID` - The `linkId` parameter must be unique across all queries in a query set  * `MISSING_QUERY_SET` - The request does not contain a query set  * `ICORRECT_JSON_QUERY_SET` - The query set provided is not valid json  * `FAILED_MODEL_EVALUATION_SET` - Failed to query the model for some or all of the items in the query set. Set the `acceptPartial` parameter to `true` to receive partial result sets  * `FAILED_MODEL_EVALUATION` - Failed to query the model for an item")
    description: StrictStr = Field(...)
    __properties = ["code", "description"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Error:
        """Create an instance of Error from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Error:
        """Create an instance of Error from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Error.parse_obj(obj)

        _obj = Error.parse_obj({
            "code": obj.get("code"),
            "description": obj.get("description")
        })
        return _obj


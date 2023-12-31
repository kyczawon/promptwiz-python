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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openapi_client.models.query_fields import QueryFields

class Request(BaseModel):
    """
    Request
    """
    api_key: StrictStr = Field(..., alias="apiKey", description="PromptWiz API Key available under [api_keys](https://promptwiz.co.uk/api_keys/) page")
    query_set: conlist(QueryFields) = Field(..., alias="querySet")
    stream: Optional[StrictBool] = Field(False, description="Indicates whether the model output should be streamed.<br /><br />")
    accept_partial: Optional[StrictBool] = Field(False, alias="acceptPartial", description="Indicates whether partially successful queries can be returned. When set to false the response will fail if ANY query for querySet fails.<br /><br />  **For streaming this input is unused.**")
    __properties = ["apiKey", "querySet", "stream", "acceptPartial"]

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
    def from_json(cls, json_str: str) -> Request:
        """Create an instance of Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in query_set (list)
        _items = []
        if self.query_set:
            for _item in self.query_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['querySet'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Request:
        """Create an instance of Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Request.parse_obj(obj)

        _obj = Request.parse_obj({
            "api_key": obj.get("apiKey"),
            "query_set": [QueryFields.from_dict(_item) for _item in obj.get("querySet")] if obj.get("querySet") is not None else None,
            "stream": obj.get("stream") if obj.get("stream") is not None else False,
            "accept_partial": obj.get("acceptPartial") if obj.get("acceptPartial") is not None else False
        })
        return _obj



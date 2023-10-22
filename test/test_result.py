# coding: utf-8

"""
    PromptWiz API - OpenAPI 3.1

    ### Context PromptWiz API provides a way to execute prompts defined in the UI. The API will return the results from OpenAI with fields populated based on your inputs and the result will be stored in PromptWiz for the purpose of analysis  ### Pre-requisites 1. You must create a prompt, and prompt version (and save it) 2. A prompt version must be set as ‘active’ in the prompt page 3. You must have a Open API Key set under api_keys page ## API modes 1. **Full result** - when stream is False, the API returns a single JSON response with the outcome of each query from querySet.     - Multiple requests are done in concurrent fashion for optimal response times 2. **Streaming** - when stream is True, the API returns multiple JSON responses through a Streaming response. The response body will have the exact same envelope as the full result mode, with the only difference being that the results field will contain the deltas that have been streamed by the model.     - Multiple requests are done in concurrent fashion & the streams will return on ‘first come first served’ basis. This means that envelopes might arrive out of order and you should rely on linkid to combine responses correctly.

    The version of the OpenAPI document: 0.1
    Contact: contact@promptwiz.co.uk
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.result import Result  # noqa: E501

class TestResult(unittest.TestCase):
    """Result unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Result:
        """Test Result
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Result`
        """
        model = Result()  # noqa: E501
        if include_optional:
            return Result(
                link_id = 56,
                prompt_id = 56,
                prompt_version_number = 56,
                results = {
                    'key' : ''
                    },
                time = 1.337,
                input_spend = 1.337,
                choices_spend = {
                    'key' : 1.337
                    },
                output_spend = 1.337
            )
        else:
            return Result(
                link_id = 56,
                prompt_id = 56,
                prompt_version_number = 56,
                results = {
                    'key' : ''
                    },
                time = 1.337,
                input_spend = 1.337,
                choices_spend = {
                    'key' : 1.337
                    },
                output_spend = 1.337,
        )
        """

    def testResult(self):
        """Test Result"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

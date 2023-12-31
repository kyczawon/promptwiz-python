# openapi-client
### Context
PromptWiz API provides a way to execute prompts defined in the UI. The API will return the results from OpenAI with fields populated based on your inputs and the result will be stored in PromptWiz for the purpose of analysis

### Pre-requisites
1. You must create a prompt, and prompt version (and save it)
2. A prompt version must be set as ‘active’ in the prompt page
3. You must have a Open API Key set under api_keys page
## API modes
1. **Full result** - when stream is False, the API returns a single JSON response with the outcome of each query from querySet.

   - Multiple requests are done in concurrent fashion for optimal response times
2. **Streaming** - when stream is True, the API returns multiple JSON responses through a Streaming response. The response body will have the exact same envelope as the full result mode, with the only difference being that the results field will contain the deltas that have been streamed by the model.
    - Multiple requests are done in concurrent fashion & the streams will return on ‘first come first served’ basis. This means that envelopes might arrive out of order and you should rely on linkid to combine responses correctly.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://promptwiz.co.uk/api/v0.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://promptwiz.co.uk/api/v0.1"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    request = openapi_client.Request() # Request | 

    try:
        api_response = api_instance.evaluate(request)
        print("The response of DefaultApi->evaluate:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->evaluate: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://promptwiz.co.uk/api/v0.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**evaluate**](docs/DefaultApi.md#evaluate) | **POST** /evaluate | 


## Documentation For Models

 - [ApiResponse](docs/ApiResponse.md)
 - [Error](docs/Error.md)
 - [QueryFields](docs/QueryFields.md)
 - [Request](docs/Request.md)
 - [Result](docs/Result.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

contact@promptwiz.co.uk



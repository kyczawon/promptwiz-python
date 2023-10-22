# openapi_client.DefaultApi

All URIs are relative to *https://promptwiz.co.uk/api/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluate**](DefaultApi.md#evaluate) | **POST** /evaluate | 


# **evaluate**
> ApiResponse evaluate(request)



### Sample Curl request  ``` curl -H 'Content-Type: application/json' \\ -d '{ \"apiKey\":\"d91a37db-a16b-4108-8485-f88496b30886\", \"querySet\": [{\"promptId\":\"5\",\"variables\":{\"PERSON\":\"Einstein\",\"QUESTION TO ASK\":\"What is 1+1?\"}}, {\"promptId\":\"5\",\"variables\":{\"PERSON\":\"Borris Johnson\",\"QUESTION TO ASK\":\"What is 1+1?\"}, \"resultsSize\":2}]}' \\ -N -X POST \\ http://www.promptwiz.co.uk/api/v0.1/evaluate/ ```

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.request import Request
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
    except Exception as e:
        print("Exception when calling DefaultApi->evaluate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evaluate Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


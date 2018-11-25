import os, requests, uuid, json

class Translation:
    text = None

class TranslationHandlerClass(object):

    def translate(self):
        # Checks to see if the Translator Text subscription key is available
        # as an environment variable. If you are setting your subscription key as a
        # string, then comment these lines out.
        if 'MS_TRANSLATOR_KEY' in os.environ:
            subscriptionKey = os.environ['MS_TRANSLATOR_KEY']
        else:
            print('Environment variable for TRANSLATOR_TEXT_KEY is not set.')
            return

        # If you encounter any issues with the base_url or path, make sure
        # that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
        base_url = 'https://api.cognitive.microsofttranslator.com'
        path = '/translate?api-version=3.0'
        params = '&to=en'
        constructed_url = base_url + path + params

        headers = {
            'Ocp-Apim-Subscription-Key': subscriptionKey,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text' : Translation.text
        }]
        if Translation.text is not None:
            request = requests.post(constructed_url, headers=headers, json=body)
            response = request.json()
            
            return response[0]["translations"][0]['text']

        else:
            return

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

MODEL_ID = 'en-fr'
TEXT_TO_TRANSLATE = 'Hello, how are you?'

authenticator = IAMAuthenticator('finJqxeDvQZkseC3Boc7jNSnVU-JBF6kctMRcaFxgGEr')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.'
    'ibm.com/instances/1ca951d8-7c06-4227-9f41-ae3cae3c1b16')

def english_to_french(_english_text='Hello, how are you?'):
    #write the code here
    """Translates english to french
    """
    french_text=language_translator.translate(
        text='Hello, how are you?',
        model_id='en-fr').get_result()
    print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text

def french_to_english(_french_text='Bonjour, comment ça va?'):
    #write the code here
    """Translates french to english
    """
    english_text=language_translator.translate(
        text='Bonjour, comment ça va?',
        model_id='fr-en').get_result()
    print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text

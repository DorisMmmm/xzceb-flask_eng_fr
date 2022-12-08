'''French English translator'''

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('url')

def english_to_french(english_text):
    '''Takes English input text and returns French text'''
    french_text = from_to(english_text, 'fr-en')
    return french_text

def french_to_english(french_text):
    '''Takes French input text and returns English text'''
    english_text = from_to(french_text, 'en-fr')
    return english_text
    
def from_to(input_text, mymodel_id):
    '''Takes input text and returns translated text'''
    result_text = ''
    if input_text != '':
        lang_tr = language_translator.translate(text=input_text, model_id=mymodel_id)
        result = lang_tr.get_result()
        dump_json= json.dumps(result, indent=2, ensure_ascii=False)
        result_dict = json.loads(dump_json)
        result_translations= result_dict['translations'][0]
        result_text= result_translations['translation']
    return result_text

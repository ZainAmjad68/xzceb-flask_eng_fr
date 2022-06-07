"""
adds support for converting text from one language to another
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv('apikey')
url = os.getenv('url')

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    a function to convert english text to french using Watson Translation API
    """
    if (isinstance(english_text, str)):
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = json.dumps(translation["translations"][0]["translation"])
        return french_text
    return 'Invalid Argument'


def french_to_english(french_text):
    """
    a function to convert french text to english using Watson Translation API
    """
    if (isinstance(french_text, str)):
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = json.dumps(
            translation["translations"][0]["translation"])
        return english_text
    return 'Invalid Argument'

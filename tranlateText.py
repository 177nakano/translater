import deepl
from deepl.exceptions import DeepLException
import os
from dotenv import load_dotenv

def translate(text):
    load_dotenv()
    translater = deepl.Translator(os.getenv("DEEPL_API_KEY"))

    try:
        translated_text = translater.translate_text(text,target_lang="JA")
    except DeepLException as e:
        return e
    
    return translated_text

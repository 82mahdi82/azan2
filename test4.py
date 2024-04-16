
import requests
from googletrans import Translator
def detect_language(text):
    translator = Translator()
    result = translator.detect(text)
    return result.lang

def translate_text(text, dest_language='en', source_language='fa'):
    if source_language=="اوتوماتیک":
        check=text.split(" ")[0]
        source_language=detect_language(check)
    base_url = 'https://api.mymemory.translated.net/get'
    params = {
        'q': text,
        'langpair': f'{source_language}|{dest_language}'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        translation = response.json()['responseData']['translatedText']
        return translation
    else:
        return "Translation failed!"

# text_to_translate = "کی میری تهران؟"
# translated_text = translate_text(text_to_translate)
# print("متن ترجمه شده:", translated_text)

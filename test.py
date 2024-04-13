from googletrans import Translator
from gtts import gTTS
import os

def get_language_options():
    print("Select the destination language:")
    print("1. Persian")
    print("2. French")
    print("3. Spanish")
    # اضافه کردن زبان‌های دیگر به دلخواه شما
    choice = input("Enter the number of your choice: ")
    languages = {'1': 'fa', '2': 'fr', '3': 'es'}  # اینجا شما می‌توانید کدهای زبان‌ها را تغییر دهید
    return languages.get(choice, 'en')  # اگر گزینه‌ی انتخابی نامعتبر باشد، به زبان انگلیسی ترجمه خواهد شد

def translate_word(word, dest_lang='en'):
    translator = Translator()
    translation = translator.translate(word, dest=dest_lang)
    return translation.text

def play_audio(name,text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save(f"{name}.mp3")
    # os.system("mpg123 translation.mp3")  # برای لینوکس
    # os.system("start translation.mp3")  # برای ویندوز
    return f"{name}.mp3"

# word = input("Enter a word: ")
# destination_language = get_language_options()
# translated_word = translate_word(word, destination_language)
# print("Translation of", word, "in", destination_language, ":", translated_word)

# play_audio(translated_word, destination_language)






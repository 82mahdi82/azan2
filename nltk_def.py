from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())

    list_=list(set(synonyms))[:10] 
    text="<pre>" + "<b>مترادف</b>\n"+"\n".join(list_) + "</pre>"
    return text


from nltk.corpus import wordnet

def get_antonyms(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

    list_= list(set(antonyms))[:10]
    return "\n".join(list_)

# word = "خوشحال"
# antonyms = get_antonyms(word)
# print("متضادهای کلمه '{}':".format(word))
# for antonym in antonyms:
#     print(antonym)


# word = "hi"
# synonyms = get_synonyms(word)
# print("مترادف‌های کلمه '{}':".format(word))
# for synonym in synonyms:
#     print(synonym)
# from hazm import synonyms

# word = "خوشحال"
# synonyms_list = synonyms(word)
# print("مترادف‌های کلمه '{}':".format(word))
# for synonym in synonyms_list:
#     print(synonym)

# import requests

# def get_synonyms(word):
#     url = f"https://api.vajehyab.com/v3/search?query={word}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         if data.get('data') and data['data'].get('synonyms'):
#             return data['data']['synonyms']
#     return []

# word = input("لطفاً کلمه‌ای را وارد کنید: ")
# synonyms = get_synonyms(word)
# if synonyms:
#     print(f"مترادف‌های کلمه '{word}':")
#     for synonym in synonyms:
#         print(synonym)
# else:
#     print("مترادفی برای این کلمه یافت نشد.")




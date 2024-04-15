from googletrans import Translator

def get_definition(langu,word):
    print(langu,word)
    translator = Translator()
    translation = translator.translate(word, src=langu, dest='en')
    english_definition = translation.extra_data["parsed"]#['definitions'][0]
    definition = english_definition
    text=""
    for i in definition[3][1][0]:
        text+= "<pre><b><i>"+i[1][0][0]+ "</i></b></pre>"+"\n"
        # text+="<i>"+f'"{i[1][0][1]}"'+"</i>"+"\n"
        text+=f'"{i[1][0][1]}"'+"\n"
        text+="〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰\n"
        # print(i[1])
    return text

# word="word"
# get_definition(word)
import requests
from bs4 import BeautifulSoup

def fon(word):
    # print(iner_str)
    # آدرس URL صفحه وب مورد نظر
    url = f"https://abadis.ir/entofa/{word}/"
    print(url)

    # درخواست GET برای دریافت محتوای صفحه
    response = requests.get(url)

    # بررسی موفقیت درخواست
    if response.status_code == 200:
        # تحلیل محتوای صفحه با BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        divs_with_class = soup.find_all('div', id="pho")

        list_=[]
        # چاپ محتوای موجود در هر دیو
        for div in divs_with_class:
            list_.append(div.text)
        if len(list_)>0:
            list_2=list_[0].split("//")
            text=f"""
US {list_2[0]+"/"}
UK {"/"+list_2[1]}
"""         
            return text



def get_synonyms(word):
    # print(iner_str)
    # آدرس URL صفحه وب مورد نظر
    url = f"https://abadis.ir/entofa/{word}/"
    print(url)

    # درخواست GET برای دریافت محتوای صفحه
    response = requests.get(url)

    # بررسی موفقیت درخواست
    if response.status_code == 200:
        # تحلیل محتوای صفحه با BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        divs_with_class = soup.find_all('div', class_="boxLtr")
        divs_with_class2 = soup.find_all('article')
        list_=[]

        # چاپ محتوای موجود در هر دیو
        for div in divs_with_class:
            list_.append(div.text)


        print("list_",list_)
        if len(list_)==1:
            return "no"
        
        elif len(list_)>=3:
            text=f"""
<b>مترادف</b>
<pre>
{list_[1]}
〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰
{list_[2]}</pre>
"""
        else:
            text=f"""
<b>مترادف</b>
<pre>
{list_[1]}</pre>
"""
        return text
        # print(divs_with_class2)


# get_synonyms("whit")
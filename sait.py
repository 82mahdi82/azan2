import requests
from bs4 import BeautifulSoup

def example(origin,teget,text):
    print(origin,teget,text)
    inter=text.split(" ")
    iner_str="%20".join(inter)
    # print(iner_str)
    # آدرس URL صفحه وب مورد نظر
    url = f"https://glosbe.com/{origin}/{teget}/{iner_str}"

    # درخواست GET برای دریافت محتوای صفحه
    response = requests.get(url)

    # بررسی موفقیت درخواست
    if response.status_code == 200:
        # تحلیل محتوای صفحه با BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        divs_with_class = soup.find_all('div', class_="odd:bg-slate-100")

        list_=[]
        # چاپ محتوای موجود در هر دیو
        for div in divs_with_class:
            list_.append(div.text)
            # print(div.text)
        # چاپ تمام محتوای متنی صفحه
        # print(soup.get_text())
        print(list_[0].split("\n"))
        text=""
        for i in list_[:6]:
            list_text=i.split("\n")
            num=0
            for b in list_text:
                if num==2:
                    break
                if b !="" :
                    if not b.startswith("OpenSub"):
                        num+=1
                        if num==1:
                            text+=b+"\n\n"
                        else:text+=b+"\n"
                        
            text+="➖➖➖➖➖➖➖➖➖"+"\n"
        return text

    else:
        print('درخواست ناموفق بود.')

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from datetime import datetime
from googletrans import Translator
import test
import nltk_def
import os
import fontic
import databases
import sait
import sitetarif
import test4
import threading

databases.creat_database_tables()

from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')


TOKEN ='5067354118:AAEJmoFKEX8wifnCKPZXHS7YXE-CdaNAY8I'

admin=120389165
channel_id= -1001898964360
channel1_id = -1002016755212  # Replace with your channel1 ID
channel2_id = -1001992750806  # Replace with your channel2 ID
chanal_base=-1002029203141
name_saite=""
userStep={}
dict_channel={} #{"name":"utl"}
text_fot_trean={}#cid:text
dict_synonym={}
dict_opposite={}
dict_cid_language_dest={}
dict_cid_language_source={}
button_site={}
languages_aks = {
    'fa': 'فارسی',
    'en': 'انگلیسی',
    'de': 'آلمانی',
    'it': 'ایتالیایی',
    'es': 'اسپانیایی',
    'ko': 'کره‌ای',
    'ja': 'ژاپنی',
    'zh-cn': 'چینی (ساده شده)',
    'zh-tw': 'چینی (سنتی)',
    'pt': 'پرتغالی',
    'ar': 'عربی',
    'tr': 'ترکی',
    'ru': 'روسی',
    'af': 'افریکانس',
    'sq': 'البانیایی',
    'am': 'امهری',
    'hy': 'ارمنی',
    'az': 'آذربایجانی',
    'eu': 'باسکی',
    'be': 'بلاروسی',
    'bn': 'بنگالی',
    'bs': 'بوسنیایی',
    'bg': 'بلغاری',
    'ca': 'کاتالان',
    'ceb': 'سبوآنو',
    'ny': 'چیچوا',
    'co': 'کرسی',
    'hr': 'کرواتی',
    'cs': 'چک',
    'da': 'دانمارکی',
    'nl': 'هلندی',
    'eo': 'اسپرانتو',
    'et': 'استونیایی',
    'tl': 'فیلیپینی',
    'fi': 'فنلاندی',
    'fr': 'فرانسوی',
    'fy': 'فریسی',
    'gl': 'گالیسیایی',
    'ka': 'گرجی',
    'el': 'یونانی',
    'gu': 'گجراتی',
    'ht': 'کریول هائیتی',
    'ha': 'هوسا',
    'haw': 'هاوایی',
    'iw': 'عبری',
    'hi': 'هندی',
    'hmn': 'همونگ',
    'hu': 'مجاری',
    'is': 'ایسلندی',
    'ig': 'ایبو',
    'id': 'اندونزیایی',
    'ga': 'ایرلندی',
    'jw': 'جاوه‌ای',
    'kn': 'کانارا',
    'kk': 'قزاقی',
    'km': 'خمر',
    'ku': 'کردی (کورمانجی)',
    'ky': 'قرقیزی',
    'lo': 'لائو',
    'la': 'لاتین',
    'lv': 'لتونیایی',
    'lt': 'لیتوانیایی',
    'lb': 'لوکزامبورگی',
    'mk': 'مقدونی',
    'mg': 'مالاگاسی',
    'ms': 'مالایی',
    'ml': 'مالایالام',
    'mt': 'مالتی',
    'mi': 'مائوری',
    'mr': 'مراتی',
    'mn': 'مغولی',
    'my': 'میانمار (برمه‌ای)',
    'ne': 'نپالی',
    'no': 'نروژی',
    'or': 'اودیا',
    'ps': 'پشتو',
    'pl': 'لهستانی',
    'pa': 'پنجابی',
    'ro': 'رومانیایی',
    'sm': 'ساموآیی',
    'gd': 'اسکاتلندی گیلیک',
    'sr': 'صربی',
    'st': 'سوتویی',
    'sn': 'شونایی',
    'sd': 'سندی',
    'si': 'سینهالا',
    'sk': 'اسلواکی',
    'sl': 'اسلوونیایی',
    'so': 'سومالیایی',
    'su': 'سوندانی',
    'sw': 'سواحلی',
    'sv': 'سوئدی',
    'tg': 'تاجیکی',
    'ta': 'تامیلی',
    'te': 'تلوگو',
    'th': 'تایلندی',
    'uk': 'اوکراینی',
    'ur': 'اردو',
    'ug': 'اویغوری',
    'uz': 'ازبکی',
    'vi': 'ویتنامی',
    'cy': 'ولزی',
    'xh': 'خوسایی',
    'yi': 'یدیش',
    'yo': 'یوروبا',
    'zu': 'زولو',
    "اوتوماتیک":'اوتوماتیک'
}

languages = {
    'فارسی': 'fa',
    'انگلیسی': 'en',
    'آلمانی': 'de',
    'ایتالیایی': 'it',
    'اسپانیایی': 'es',
    'کره‌ای': 'ko',
    'ژاپنی': 'ja',
    'چینی (ساده شده)': 'zh-cn',
    'چینی (سنتی)': 'zh-tw',
    'پرتغالی': 'pt',
    'عربی': 'ar',
    'ترکی': 'tr',
    'روسی': 'ru',


    'افریکانس': 'af',
    'البانیایی': 'sq',
    'امهری': 'am',
    
    'ارمنی': 'hy',
    'آذربایجانی': 'az',
    'باسکی': 'eu',
    'بلاروسی': 'be',
    'بنگالی': 'bn',
    'بوسنیایی': 'bs',
    'بلغاری': 'bg',
    'کاتالان': 'ca',
    'سبوآنو': 'ceb',
    'چیچوا': 'ny',

    'کرسی': 'co',
    'کرواتی': 'hr',
    'چک': 'cs',
    'دانمارکی': 'da',
    'هلندی': 'nl',
    'اسپرانتو': 'eo',
    'استونیایی': 'et',
    'فیلیپینی': 'tl',
    'فنلاندی': 'fi',
    'فرانسوی': 'fr',
    'فریسی': 'fy',
    'گالیسیایی': 'gl',
    'گرجی': 'ka',
    'یونانی': 'el',
    'گجراتی': 'gu',
    'کریول هائیتی': 'ht',
    'هوسا': 'ha',
    'هاوایی': 'haw',
    'عبری': 'iw',
    'هندی': 'hi',
    'همونگ': 'hmn',
    'مجاری': 'hu',
    'ایسلندی': 'is',
    'ایبو': 'ig',
    'اندونزیایی': 'id',
    'ایرلندی': 'ga',
    
    
    'جاوه‌ای': 'jw',
    'کانارا': 'kn',
    'قزاقی': 'kk',
    'خمر': 'km',
    
    'کردی (کورمانجی)': 'ku',
    'قرقیزی': 'ky',
    'لائو': 'lo',
    'لاتین': 'la',
    'لتونیایی': 'lv',
    'لیتوانیایی': 'lt',
    'لوکزامبورگی': 'lb',
    'مقدونی': 'mk',
    'مالاگاسی': 'mg',
    'مالایی': 'ms',
    'مالایالام': 'ml',
    'مالتی': 'mt',
    'مائوری': 'mi',
    'مراتی': 'mr',
    'مغولی': 'mn',
    'میانمار (برمه‌ای)': 'my',
    'نپالی': 'ne',
    'نروژی': 'no',
    'اودیا': 'or',
    'پشتو': 'ps',
    'لهستانی': 'pl',
    'پنجابی': 'pa',
    'رومانیایی': 'ro',
    
    'ساموآیی': 'sm',
    'اسکاتلندی گیلیک': 'gd',
    'صربی': 'sr',
    'سوتویی': 'st',
    'شونایی': 'sn',
    'سندی': 'sd',
    'سینهالا': 'si',
    'اسلواکی': 'sk',
    'اسلوونیایی': 'sl',
    'سومالیایی': 'so',
    
    'سوندانی': 'su',
    'سواحلی': 'sw',
    'سوئدی': 'sv',
    'تاجیکی': 'tg',
    'تامیلی': 'ta',
    'تلوگو': 'te',
    'تایلندی': 'th',
    
    'اوکراینی': 'uk',
    'اردو': 'ur',
    'اویغوری': 'ug',
    'ازبکی': 'uz',
    'ویتنامی': 'vi',
    'ولزی': 'cy',
    'خوسایی': 'xh',
    'یدیش': 'yi',
    'یوروبا': 'yo',
    'زولو': 'zu'
}
def vois(dict_,word_translate,language):
    path_vois=test.play_audio(word_translate.split(" ")[0],word_translate,language)
    dict_.setdefault("vois","")
    dict_["vois"]=path_vois

def def_fontic(dict_,word_translate):
    dict_.setdefault("fontic","")
    dict_["fontic"]=fontic.get_ipa(word_translate)[0]
def def_example(dict_,source_language,language,text):
    example=sait.example(source_language,language,text)
    dict_.setdefault("example","")
    dict_["example"]=example



def detect_language(text):
    translator = Translator()
    result = translator.detect(text)
    return result.lang

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            print(str(m.chat.first_name) +
                  " [" + str(m.chat.id) + "]: " + m.text)
        elif m.content_type == 'photo':
            print(str(m.chat.first_name) +
                  " [" + str(m.chat.id) + "]: " + "New photo recieved")
        elif m.content_type == 'document':
            print(str(m.chat.first_name) +
                  " [" + str(m.chat.id) + "]: " + 'New Document recieved')


bot = telebot.TeleBot(TOKEN,num_threads=3)
bot.set_update_listener(listener)

#-----------------------------------------------------------------def----------------------------------------------------------
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        userStep[uid] = 0
        return 0
def is_user_member(user_id, channel_id):
    try:
        chat_member = bot.get_chat_member(channel_id, user_id)
        return chat_member.status == "member" or chat_member.status == "administrator" or chat_member.status == "creator"
    except Exception as e:
        #print(f"Error checking membership: {e}")
        return False
    

#------------------------------------------------------commands-------------------------------------------------
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    text_fot_trean.setdefault(cid,"")
    dict_cid_language_source.setdefault(cid,"اوتوماتیک")

    if cid != admin:
        databases.insert_users(cid)
        markup=ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("ترجمه")
        # if cid in dict_cid_language_dest:
        #     markup.add(f"ترجمه به: {languages_aks[dict_cid_language_dest[cid]]}")
        markup.add("مترادف و تعریف لغت")
        markup.add("ارتقا حساب ⬆️","لینک به سایت 🔗")
        bot.send_message(cid,f"""
سلام {m.chat.first_name} عزیز 
به ربات مترجم خوش آمدید
لطفا برای استفاده از ربات یکی از گزینه های زیر را انتخاب کنید
""",reply_markup=markup)
    else:
        
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('آمار تمامی کاربران',callback_data='panel_amar'))
        markup.add(InlineKeyboardButton('ارسال همگانی',callback_data='panel_brodcast'),InlineKeyboardButton('فوروارد همگانی',callback_data='panel_forall'))
        markup.add(InlineKeyboardButton("تنظیم دکمه",callback_data="seting"))
        bot.send_message(cid,"""
سلام ادمین گرامی 
برای مدیریت بازی از دکمه های زیر استفاده کنید
""",reply_markup=markup)

#---------------------------------------------------callback------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith("sends"))
def call_callback_panel_sends(call):
    global userstep
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")  
    count=0  
    count_black=0
    if data[1] =="brodcast":
        list_user=databases.use_users()
        for i in list_user:
            try:
                bot.copy_message(i,cid,int(data[-1]))
                count+=1
            except:
                databases.delete_users(i)
                count_black+=1
                # print("eror")
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        text=f"به {count} نفر ارسال شد"
        if count_black!=0:
            text=f"\n و به {count_black} نفر ارسال نشد احتمالا ربات را بلاک کرده اند و از دیتابیس ما حذف میشوند \n"
        bot.edit_message_text(text,cid,mid,reply_markup=markup)
    if data[1] =="forall":
        list_user=databases.use_users()
        for i in list_user:
            try:
                bot.forward_message(i,cid,int(data[-1]))
                count+=1
            except:
                databases.delete_users(i)
                count_black+=1
                # print("eror")
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        text=f"به {count} نفر ارسال شد"
        if count_black!=0:
            text=f"\n و به {count_black} نفر ارسال نشد احتمالا ربات را بلاک کرده اند و از دیتابیس ما حذف میشوند \n"
        bot.edit_message_text(text,cid,mid,reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data.startswith("back"))
def call_callback_panel_amar(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    userStep[cid]=0
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('آمار تمامی کاربران',callback_data='panel_amar'))
    markup.add(InlineKeyboardButton('ارسال همگانی',callback_data='panel_brodcast'),InlineKeyboardButton('فوروارد همگانی',callback_data='panel_forall'))
    markup.add(InlineKeyboardButton("تنظیم دکمه",callback_data="seting"))
    bot.edit_message_text("""
سلام ادمین گرامی 
برای مدیریت بازی از دکمه های زیر استفاده کنید
""",cid,mid,reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data.startswith("check"))
def call_callback_panel_amar(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    button_name = call.data.split("_")[-1]
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("بله",callback_data=f"delete_{button_name}"),InlineKeyboardButton("خیر",callback_data="seting"))
    bot.edit_message_text("آیا از حذف دکمه مطمئن هستید؟",cid,mid,reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("delete"))
def call_callback_panel_amar(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    button_name = call.data.split("_")[-1]
    button_site.pop(button_name)
    def_button_site(call)
    bot.answer_callback_query(call.id,"دکمه مورد نظر حذف شد")

@bot.callback_query_handler(func=lambda call: call.data.startswith("creat"))
def call_callback_panel_amar(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
    bot.edit_message_text("برای ساخت دکمه لینک لطفا ابتدا اسم دکمه را ارسال کنید:",cid,mid,reply_markup=markup)
    userStep[cid]=10
@bot.callback_query_handler(func=lambda call: call.data.startswith("seting"))
def def_button_site(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    if len(button_site)==0:
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text("برای ساخت دکمه لینک لطفا ابتدا اسم دکمه را ارسال کنید:",cid,mid,reply_markup=markup)
        userStep[cid]=10
    else:
        markup=InlineKeyboardMarkup()
        for i in button_site:
            markup.add(InlineKeyboardButton(i,callback_data=f"check_{i}"))
        markup.add(InlineKeyboardButton("ساخت دکمه جدید",callback_data="creat_button"))
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text("برای حذف هر دکمه روی آن کلیک کنید و برای ساخت دکمه جدید بر روی دکمه 'ساخت دکمه جدید' کلیک کنید",cid,mid,reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("sushow"))
def call_callback_panel_amar(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")[-1]
    markup=InlineKeyboardMarkup(row_width=4)
    list_murkup=[]
    for i in languages:
        list_murkup.append(InlineKeyboardButton(i, callback_data=f"sulanguage_{languages[i]}"))
    markup.add(*list_murkup)
    bot.edit_message_reply_markup(cid,mid,reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data.startswith("show"))
def call_callback_panel_amar(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")[-1]
    markup=InlineKeyboardMarkup(row_width=4)
    list_murkup=[]
    for i in languages:
        list_murkup.append(InlineKeyboardButton(i, callback_data=f"language_{languages[i]}"))
    markup.add(*list_murkup)
    bot.edit_message_reply_markup(cid,mid,reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: call.data.startswith("panel"))
def call_callback_panel_amar(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")[-1]
    countOfUsers=len(databases.use_users())
    if countOfUsers>0:
        if data=="amar":
            countOfUsers=len(databases.use_users())
            txt = f'آمار کاربران: {countOfUsers} نفر '
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
            bot.edit_message_text(txt,cid,mid,reply_markup=markup)
        elif data=="brodcast":
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
            bot.edit_message_text("برای ارسال همگانی پیام لطفا پیام خود را ارسال کنید و در غیر این صورت برای بازگشت به پنل از دکمه زیر استفاده کنید",cid,mid,reply_markup=markup)
            userStep[cid]=30
        elif data=="forall":
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
            bot.edit_message_text("برای فوروارد همگانی پیام لطفا پیام خود را ارسال کنید و در غیر این صورت برای بازگشت به پنل از دکمه زیر استفاده کنید",cid,mid,reply_markup=markup)
            userStep[cid]=31
    else:
        bot.answer_callback_query(call.id,"هنوز کاربری وجود ندارد")


@bot.callback_query_handler(func=lambda call: call.data.startswith("synonym"))
def languages_def(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    language=call.data.split("_")[1]
    dict_synonym.setdefault(cid,"")
    dict_synonym[cid]=language
    bot.edit_message_text("لطفا کلمه خود را ارسال کنید:",cid,mid)
    userStep[cid]=2
@bot.callback_query_handler(func=lambda call: call.data.startswith("opposite"))
def languages_def(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    language=call.data.split("_")[1]
    dict_opposite.setdefault(cid,"")
    dict_opposite[cid]=language
    bot.edit_message_text("لطفا کلمه خود را ارسال کنید:",cid,mid)
    userStep[cid]=3
@bot.callback_query_handler(func=lambda call: call.data.startswith("sulanguage"))
def languages_def(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    language=call.data.split("_")[1]
    dict_cid_language_source.setdefault(cid,"")
    dict_cid_language_source[cid]=language
    bot.delete_message(cid,mid)
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("✅ترجمه✅")
    if cid in dict_cid_language_dest:
        markup.add(f"ترجمه به: {languages_aks[dict_cid_language_dest[cid]]}",f"ترجمه از: {languages_aks[dict_cid_language_source[cid]]}")
    markup.add("مترادف و تعریف لغت")
    markup.add("ارتقا حساب ⬆️","لینک به سایت 🔗")
    bot.send_message(cid,"زبان شما انتخاب شد\nکلمه یا جمله خود را برای ترجمه ارسال کنید:",reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("language"))
def languages_def(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    language=call.data.split("_")[1]
    dict_cid_language_dest.setdefault(cid,"")
    dict_cid_language_dest[cid]=language
    bot.delete_message(cid,mid)
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("✅ترجمه✅")
    if cid in dict_cid_language_dest:
        markup.add(f"ترجمه به: {languages_aks[dict_cid_language_dest[cid]]}",f"ترجمه از: {languages_aks[dict_cid_language_source[cid]]}")
    markup.add("مترادف و تعریف لغت")
    markup.add("ارتقا حساب ⬆️","لینک به سایت 🔗")
    bot.send_message(cid,"زبان شما انتخاب شد\nکلمه یا جمله خود را برای ترجمه ارسال کنید:",reply_markup=markup)
    # word_translate=test.translate_word(text_fot_trean[cid],language)
#     if len(text_fot_trean[cid])>499:
#         word_translate=test.translate_word(text_fot_trean[cid],language)
#     else:
#         word_translate=test4.translate_text(text_fot_trean[cid],language,dict_cid_language_source[cid])
#     try:
#         print(word_translate)
#         if len(word_translate.split(" "))==1:
#             path_vois=test.play_audio(word_translate.split(" ")[0],word_translate,language)
#             if language=="en":
#                 bot.send_voice(cid,voice=open(path_vois,'rb'),caption=f"""
# تلفظ 👆   
# ➖➖➖➖➖➖➖➖➖
# <pre>ترجمه:
# {word_translate}</pre>
# """, parse_mode='HTML')


# #                 bot.send_voice(cid,voice=open(path_vois,'rb'),caption=f"""
# # تلفظ 👆   
# # ➖➖➖➖➖➖➖➖➖
# # <pre>فونتیک:
                
# # {fontic.get_ipa(word_translate)[0]}</pre>
# # ➖➖➖➖➖➖➖➖➖
# # <pre>ترجمه:
# # {word_translate}</pre>
# # """, parse_mode='HTML')
#             else:
#                 bot.send_voice(cid,voice=open(path_vois,'rb'),caption=f"""
# تلفظ 👆   
# ➖➖➖➖➖➖➖➖➖
# <pre>ترجمه:
# {word_translate}</pre>

# """, parse_mode='HTML')         

#         else:
#             path_vois=test.play_audio(word_translate.split(" ")[0],word_translate,language)
#             example=sait.example(detect_language(text_fot_trean[cid]),language,text_fot_trean[cid])
#             if example!=None:
#                 bot.send_voice(cid,voice=open(path_vois,'rb'),caption=f"""
# تلفظ 👆   
# ➖➖➖➖➖➖➖➖➖
# <pre>ترجمه:
# {word_translate}</pre>
# ➖➖➖➖➖➖➖➖➖
# مثال:
# {example}
# """, parse_mode='HTML')
#             else:
#                 bot.send_voice(cid,voice=open(path_vois,'rb'),caption=f"""
# تلفظ 👆   
# ➖➖➖➖➖➖➖➖➖
# <pre>ترجمه:
# {word_translate}</pre>
# """, parse_mode='HTML')
#         os.remove(path_vois)
#     except:
#         example=sait.example(detect_language(text_fot_trean[cid]),language,text_fot_trean[cid])
#         if example!=None:
#             bot.send_message(cid,f"""
# <pre>ترجمه:
# {word_translate}</pre>
# ➖➖➖➖➖➖➖➖➖
# مثال:
# {example}
# """, parse_mode='HTML')
#         else:
#             bot.send_message(cid,f"""
# ترجمه:
# {word_translate}
# """, parse_mode='HTML')
        
    









#----------------------------------------------------------m.text------------------------------------------------


@bot.message_handler(func=lambda m: m.text.startswith("ترجمه از:"))
def handel_text(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    markup=InlineKeyboardMarkup()
    list_murkup=[]
    num=1
    markup.add(InlineKeyboardButton("اوتوماتیک",callback_data='sulanguage_اوتوماتیک'))
    for i in languages:
        if num==15:
            break
        list_murkup.append(InlineKeyboardButton(i, callback_data=f"sulanguage_{languages[i]}"))
        num+=1
    list_murkup.append(InlineKeyboardButton("سایر زبان ها",callback_data="sushow_other"))
    markup.add(*list_murkup)
    bot.send_message(cid,"زبان ورودی خود را انتخاب کنید",reply_markup=markup)

@bot.message_handler(func=lambda m: m.text.startswith("ترجمه به:") )
def handel_text(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    markup=InlineKeyboardMarkup()
    list_murkup=[]
    num=1
    for i in languages:
        if num==15:
            break
        list_murkup.append(InlineKeyboardButton(i, callback_data=f"language_{languages[i]}"))
        num+=1
    list_murkup.append(InlineKeyboardButton("سایر زبان ها",callback_data="show_other"))
    markup.add(*list_murkup)
    bot.send_message(cid,"به چه زبانی ترجمه شود؟",reply_markup=markup)


@bot.message_handler(func=lambda m: m.text=="ترجمه" or m.text=="✅ترجمه✅")
def handel_text(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    userStep[cid]=0
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("✅ترجمه✅")
    dict_cid_language_source.setdefault(cid,"اوتوماتیک")
    dict_cid_language_dest.setdefault(cid,"en")

    if cid in dict_cid_language_dest:
        markup.add(f"ترجمه به: {languages_aks[dict_cid_language_dest[cid]]}",f"ترجمه از: {languages_aks[dict_cid_language_source[cid]]}")
    markup.add("مترادف و تعریف لغت")
    markup.add("ارتقا حساب ⬆️","لینک به سایت 🔗")
    bot.send_message(cid,"برای دریافت ترجمه کلمه یا جمله مورد نظر خود را ارسال کنید",reply_markup=markup)
    userStep[cid]=1

@bot.message_handler(func=lambda m: m.text=="مترادف و تعریف لغت" or m.text=="✅مترادف و تعریف لغت✅")
def handel_text(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    userStep[cid]=0
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ترجمه")
    markup.add('✅مترادف و تعریف لغت✅')
    markup.add("ارتقا حساب ⬆️","لینک به سایت 🔗")

    bot.send_message(cid,"لطفا برای دریافت تعریف لغت کلمه خود را ارسال کنید:",reply_markup=markup)
    userStep[cid]=2
@bot.message_handler(func=lambda m: m.text=="ارتقا حساب ⬆️")
def handel_text(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    userStep[cid]=0
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("یک ماهه : قیمت 00000 تومان")
    markup.add("سه ماهه : قیمت 00000 تومان")
    markup.add("سالیانه : قیمت 00000 تومان")
    markup.add("منو اصلی 📜")
    bot.send_message(cid,"برای ارتقا حساب خود یکی از پلن های زیر را انتخاب کنید: ",reply_markup=markup)


@bot.message_handler(func=lambda m: m.text=="منو اصلی 📜")
def handel_text(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    userStep[cid]=0
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ترجمه")
    if cid in dict_cid_language_dest:
        markup.add(f"ترجمه به: {languages_aks[dict_cid_language_dest[cid]]}",f"ترجمه از: {languages_aks[dict_cid_language_source[cid]]}")
    markup.add("مترادف و تعریف لغت")
    markup.add("ارتقا حساب ⬆️","لینک به سایت 🔗")
    bot.send_message(cid,"منو اصلی",reply_markup=markup)
@bot.message_handler(func=lambda m: m.text=="لینک به سایت 🔗")
def handel_text(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    userStep[cid]=0
    markup=InlineKeyboardMarkup()
    for i in button_site:
        markup.add(InlineKeyboardButton(i,url=button_site[i]))
    bot.send_message(cid,'برای مشاهده سایت از دکمه زیر استفاده کنید:',reply_markup=markup)


#---------------------------------------------------------userstep---------------------------------------------------
    
@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==1)
def send_music(m):
    cid=m.chat.id
    text=m.text
    message_=bot.send_message(cid,"درحال ترجمه 🔄")
    mid=message_.message_id
    text_fot_trean[cid]=text
    if dict_cid_language_source[cid]=="اوتوماتیک":
        check=text.split(" ")[0]
        source_language=detect_language(check)
    else:
        source_language=dict_cid_language_source[cid]

    list_info=databases.use_translations(text,source_language,dict_cid_language_dest[cid])
    if len(list_info)==1:
        dict_info=list_info[0]
        bot.copy_message(cid,channel_id,int(dict_info[3]))
        return

    language=dict_cid_language_dest[cid]
    # word_translate=test.translate_word(text_fot_trean[cid],language)
    
    if len(text)>499 or language==source_language:
        word_translate=test.translate_word(text_fot_trean[cid],language)
    else:
        word_translate=test4.translate_text(text_fot_trean[cid],language,source_language)
    try:
        if len(word_translate.split(" "))==1:
            if language=="en":
                results = {}
                thread1 = threading.Thread(target=vois, args=(results,word_translate,language))
                thread2 = threading.Thread(target=def_fontic, args=(results,word_translate))
                thread1.start()
                thread2.start()
                thread1.join()
                thread2.join()
                result1 = results["fontic"]
                result2 = results["vois"]
                message=bot.send_voice(cid,voice=open(result2,'rb'),caption=f"""
تلفظ 👆   
➖➖➖➖➖➖➖➖➖
<pre>فونتیک:
                
{result1}</pre>
➖➖➖➖➖➖➖➖➖
<pre>ترجمه:
{word_translate}</pre>

@novinzabanbot
""", parse_mode='HTML')
                chanel=bot.copy_message(channel_id,cid,message.message_id)
                databases.insert_translations(text,source_language,language,chanel.message_id)
                bot.delete_message(cid,mid)
                return
            else:
                path_vois=test.play_audio(word_translate.split(" ")[0],word_translate,language)
                message=bot.send_voice(cid,voice=open(path_vois,'rb'),caption=f"""
تلفظ 👆   
➖➖➖➖➖➖➖➖➖
<pre>ترجمه:
{word_translate}</pre>

@novinzabanbot
""", parse_mode='HTML') 
                chanel=bot.copy_message(channel_id,cid,message.message_id)   
                databases.insert_translations(text,source_language,language,chanel.message_id)
                bot.delete_message(cid,mid)
                return  
        else:
            if len(word_translate)>100:
                # results = {}
                # thread1 = threading.Thread(target=vois, args=(results,word_translate,language))
                # thread1.start()
                # thread1.join()
                # result2 = results["vois"]
                message=bot.edit_message_text(f"""
<pre>ترجمه:
{word_translate}</pre>

@novinzabanbot
""",cid,mid, parse_mode='HTML')
                return
#                 message=bot.send_voice(cid,voice=open(result2,'rb'),caption=f"""
# تلفظ 👆   
# ➖➖➖➖➖➖➖➖➖
# <pre>ترجمه:
# {word_translate}</pre>

# @novinzabanbot
# """, parse_mode='HTML')
            else:
                results = {}
                thread1 = threading.Thread(target=vois, args=(results,word_translate,language))
                thread3 = threading.Thread(target=def_example, args=(results,source_language,language,text_fot_trean[cid]))

                thread1.start()
                thread3.start()
                thread1.join()
                thread3.join()
                result2 = results["vois"]
                result3 = results["example"]
                if result3!=None:
                    message=bot.send_voice(cid,voice=open(result2,'rb'),caption=f"""
تلفظ 👆   
➖➖➖➖➖➖➖➖➖
<pre>ترجمه:
{word_translate}</pre>
➖➖➖➖➖➖➖➖➖
مثال:
{result3}

@novinzabanbot
""", parse_mode='HTML')
                    chanel=bot.copy_message(channel_id,cid,message.message_id)
                    databases.insert_translations(text,source_language,language,chanel.message_id)
                    bot.delete_message(cid,mid)
                    return
                else:
                    message=bot.send_voice(cid,voice=open(result2,'rb'),caption=f"""
تلفظ 👆   
➖➖➖➖➖➖➖➖➖
<pre>ترجمه:
{word_translate}</pre>

@novinzabanbot
""", parse_mode='HTML')
        os.remove(result2)
        chanel=bot.copy_message(channel_id,cid,message.message_id)
        databases.insert_translations(text,source_language,language,chanel.message_id)
        return
    except:
#         example=sait.example(detect_language(text_fot_trean[cid]),language,text_fot_trean[cid])
#         if example!=None:
#             message=bot.send_message(cid,f"""
# <pre>ترجمه:
# {word_translate}</pre>
# ➖➖➖➖➖➖➖➖➖
# مثال:
# {example}

# @novinzabanbot
# """, parse_mode='HTML')
#             chanel=bot.copy_message(channel_id,cid,message.message_id)
#             databases.insert_translations(text,source_language,language,chanel.message_id)
#             return
#         else:
        message=bot.edit_message_text(f"""
<pre>ترجمه:
{word_translate}</pre>

@novinzabanbot
""",cid,mid, parse_mode='HTML')
        chanel=bot.copy_message(channel_id,cid,message.message_id)
        databases.insert_translations(text,source_language,language,chanel.message_id)
        return 
    
@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==2)
def send_music(m):
    cid=m.chat.id
    text=m.text
    try:
        motraadef=nltk_def.get_synonyms(text)
        # motraadef="hi\n"
        print(motraadef)
        bot.send_message(cid,motraadef +"\n"+ "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"+"\n"+ sitetarif.get_definition(detect_language(text),text)+"\n\n"+"@novinzabanbot", parse_mode='HTML')
   

    except:
        bot.send_message(cid,"برای کلمه ای که ارسال کردید مترادفی پیدا نشد")


@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==10)
def send_music(m):
    global name_saite
    cid=m.chat.id
    text=m.text
    if text in button_site:
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.send_message(cid,"این اسم قبلا برای دکه دیگری انتخاب شده لطفا اسم دیگری ارسال کنید:",reply_markup=markup)
    else:
        name_saite=text
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.send_message(cid,"لطفا لینک سایت را ارسال کنید:",reply_markup=markup)
        userStep[cid]=20

@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==20)
def send_music(m):
    global name_saite
    cid=m.chat.id
    text=m.text
    button_site.setdefault(name_saite,text)
    bot.send_message(cid,"دکمه اضافه شد.")

    markup=InlineKeyboardMarkup()
    for i in button_site:
        markup.add(InlineKeyboardButton(i,callback_data=f"check_{i}"))
    markup.add(InlineKeyboardButton("ساخت دکمه جدید",callback_data="creat_button"))
    markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
    bot.send_message(cid,"برای حذف هر دکمه روی آن کلیک کنید و برای ساخت دکمه جدید بر روی دکمه 'ساخت دکمه جدید' کلیک کنید",reply_markup=markup)


@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==30)
def send_music(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    list_user=databases.use_users()
    count=0  
    count_black=0
    for i in list_user:
        try:
            bot.copy_message(i,cid,mid)
            count+=1
        except:
            databases.delete_users(i)
            count_black+=1
            # print("eror")
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
    text=f"به {count} نفر ارسال شد"
    if count_black!=0:
        text=f"\n و به {count_black} نفر ارسال نشد احتمالا ربات را بلاک کرده اند و از دیتابیس ما حذف میشوند \n"
    bot.send_message(cid,text,reply_markup=markup)


@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==31)
def send_music(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    list_user=databases.use_users()
    count=0  
    count_black=0
    for i in list_user:
        try:
            bot.copy_message(i,cid,mid)
            count+=1
        except:
            databases.delete_users(i)
            count_black+=1
            # print("eror")
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
    text=f"به {count} نفر ارسال شد"
    if count_black!=0:
        text=f"\n و به {count_black} نفر ارسال نشد احتمالا ربات را بلاک کرده اند و از دیتابیس ما حذف میشوند \n"
    bot.send_message(cid,text,reply_markup=markup)


# @bot.message_handler(func=lambda m: get_user_step(m.chat.id)==3)
# def send_music(m):
#     cid=m.chat.id
#     text=m.text
#     try:
#         bot.send_message(cid,nltk_def.get_antonyms(text))
#     except:
#         bot.send_message(cid,"برای کلمه ای که ارسال کردید متضادی پیدا نشد")
bot.infinity_polling()

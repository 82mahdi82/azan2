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

TOKEN ='7018847010:AAEMTrqs7mZRwxyaXE_XUgbyYPYzl_Twt3M'

admin=0#748626808
channel1_id = -1002016755212  # Replace with your channel1 ID
channel2_id = -1001992750806  # Replace with your channel2 ID
chanal_base=-1002029203141
userStep={}
dict_channel={} #{"name":"utl"}
text_fot_trean={}#cid:text
dict_synonym={}
dict_opposite={}
languages = {
    'فارسی': 'fa',
    'انگلیسی': 'en',
    'آلمانی': 'de',
    'پرتغالی': 'pt',
    'افریکانس': 'af',
    'البانیایی': 'sq',
    'امهری': 'am',
    'عربی': 'ar',
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
    'چینی (ساده شده)': 'zh-cn',
    'چینی (سنتی)': 'zh-tw',
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
    'ایتالیایی': 'it',
    'ژاپنی': 'ja',
    'جاوه‌ای': 'jw',
    'کانارا': 'kn',
    'قزاقی': 'kk',
    'خمر': 'km',
    'کره‌ای': 'ko',
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
    'روسی': 'ru',
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
    'اسپانیایی': 'es',
    'سوندانی': 'su',
    'سواحلی': 'sw',
    'سوئدی': 'sv',
    'تاجیکی': 'tg',
    'تامیلی': 'ta',
    'تلوگو': 'te',
    'تایلندی': 'th',
    'ترکی': 'tr',
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
    if cid != admin:
        markup=ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("ترجمه")
        markup.add("مترادف","متضاد")
        bot.send_message(cid,f"""
سلام {m.chat.first_name} عزیز 
به ربات مترجم خوش آمدید
لطفا برای استفاده از ربات یکی از گزینه های زیر را انتخاب کنید
""",reply_markup=markup)
    else:
        markup.add(InlineKeyboardButton('آمار تمامی کاربران',callback_data='panel_amar'))
        markup.add(InlineKeyboardButton('ارسال همگانی',callback_data='panel_brodcast'),InlineKeyboardButton('فوروارد همگانی',callback_data='panel_forall'))
        bot.send_message(cid,"""
سلام ادمین گرامی 
برای مدیریت بازی از دکمه های زیر استفاده کنید
""",reply_markup=markup)

#---------------------------------------------------callback------------------------------------------------------------


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
            userStep[cid]=11
        elif data=="forall":
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
            bot.edit_message_text("برای فوروارد همگانی پیام لطفا پیام خود را ارسال کنید و در غیر این صورت برای بازگشت به پنل از دکمه زیر استفاده کنید",cid,mid,reply_markup=markup)
            userStep[cid]=12
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
@bot.callback_query_handler(func=lambda call: call.data.startswith("language"))
def languages_def(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    language=call.data.split("_")[1]
    bot.delete_message(cid,mid)
    word_translate=test.translate_word(text_fot_trean[cid],language)
    try:
        print(word_translate)
        if len(word_translate.split(" "))==1:
            path_vois=test.play_audio(word_translate.split(" ")[0],word_translate,language)
            if language=="en":
                bot.send_voice(cid,voice=open(path_vois,'rb'),caption=f"""
تلفظ 👆   
➖➖➖➖➖➖➖➖➖
فونتیک:
{fontic.get_ipa(word_translate)}
➖➖➖➖➖➖➖➖➖
ترجمه:
{word_translate}
➖➖➖➖➖➖➖➖➖
""")
            else:
                bot.send_voice(cid,voice=open(path_vois,'rb'),caption=f"""
تلفظ 👆   
➖➖➖➖➖➖➖➖➖
ترجمه:
{word_translate}
➖➖➖➖➖➖➖➖➖
""")         

        else:
            path_vois=test.play_audio(word_translate.split(" ")[0],word_translate,language)
            example=sait.example(detect_language(text_fot_trean[cid]),language,text_fot_trean[cid])
            if example!=None:
                bot.send_voice(cid,voice=open(path_vois,'rb'),caption=f"""
تلفظ 👆   
➖➖➖➖➖➖➖➖➖
ترجمه:
{word_translate}
➖➖➖➖➖➖➖➖➖
مثال:
{example}
""")
            else:
                bot.send_voice(cid,voice=open(path_vois,'rb'),caption=f"""
تلفظ 👆   
➖➖➖➖➖➖➖➖➖
ترجمه:
{word_translate}
""")
        os.remove(path_vois)
    except:
        example=sait.example(detect_language(text_fot_trean[cid]),language,text_fot_trean[cid])
        if example!=None:
            bot.send_message(cid,f"""
ترجمه:
{word_translate}
➖➖➖➖➖➖➖➖➖
مثال:
{example}
""")
        else:
            bot.send_message(cid,f"""
ترجمه:
{word_translate}
""")
        
    









#----------------------------------------------------------m.text------------------------------------------------
@bot.message_handler(func=lambda m: m.text=="ترجمه" or m.text=="✅ترجمه✅")
def handel_text(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    userStep[cid]=0
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("✅ترجمه✅")
    markup.add("مترادف","متضاد")
    bot.send_message(cid,"برای دریافت ترجمه کلمه یا جمله مورد نظر خود را ارسال کنید",reply_markup=markup)
    userStep[cid]=1

@bot.message_handler(func=lambda m: m.text=="مترادف" or m.text=="✅مترادف✅")
def handel_text(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    userStep[cid]=0
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ترجمه")
    markup.add("✅مترادف✅","متضاد")
    bot.send_message(cid,"لطفا کلمه خود را ارسال کنید:",reply_markup=markup)
    userStep[cid]=2
    # markup=InlineKeyboardMarkup(row_width=4)
    # list_murkup=[]
    # for i in languages[:9]:
    #     list_murkup.append(InlineKeyboardButton(i, callback_data=f"synonym_{languages[i]}"))
    # markup.add(*list_murkup)
    # bot.send_message(cid,"برای دریافت مترادف کلمات لطفا ابتدا زبان مد نظر را انتخاب کنید",reply_markup=markup)
@bot.message_handler(func=lambda m: m.text=="متضاد" or m.text=="✅متضاد✅")
def handel_text(m):
    cid=m.chat.id
    text=m.text
    mid=m.message_id
    userStep[cid]=0
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ترجمه")
    markup.add("مترادف","✅متضاد✅")
    bot.send_message(cid,"لطفا کلمه خود را ارسال کنید:",reply_markup=markup)
    userStep[cid]=3
    # markup=InlineKeyboardMarkup(row_width=4)
    # list_murkup=[]
    # for i in languages[:9]:
    #     list_murkup.append(InlineKeyboardButton(i, callback_data=f"opposite_{languages[i]}"))
    # markup.add(*list_murkup)
    # bot.send_message(cid,"برای دریافت متضاد کلمات لطفا ابتدا زبان مد نظر را انتخاب کنید",reply_markup=markup)

#---------------------------------------------------------userstep---------------------------------------------------
    
@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==1)
def send_music(m):
    cid=m.chat.id
    text=m.text
    text_fot_trean[cid]=text
    markup=InlineKeyboardMarkup(row_width=4)
    list_murkup=[]
    for i in languages:
        list_murkup.append(InlineKeyboardButton(i, callback_data=f"language_{languages[i]}"))
    markup.add(*list_murkup)
    bot.send_message(cid,"به چه زبانی ترجمه شود؟",reply_markup=markup)
@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==2)
def send_music(m):
    cid=m.chat.id
    text=m.text
    try:
        bot.send_message(cid,nltk_def.get_synonyms(text))
    except:
        bot.send_message(cid,"برای کلمه ای که ارسال کردید مترادفی پیدا نشد")

@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==3)
def send_music(m):
    cid=m.chat.id
    text=m.text
    try:
        bot.send_message(cid,nltk_def.get_antonyms(text))
    except:
        bot.send_message(cid,"برای کلمه ای که ارسال کردید متضادی پیدا نشد")
bot.infinity_polling()
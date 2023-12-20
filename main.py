import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import azan
import databases
from datetime import datetime
import threading
from config import *
admins=748626808#975427911
channel1_id = -1002016755212  # Replace with your channel1 ID
channel2_id = -1001992750806  # Replace with your channel2 ID
chanal_base=-1002029203141
userstep=0
dict_channel={} #{"name":"utl"}
databases.creat_database_tables()
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


def admin_group(cid):
    if len(databases.use_table_admin_group(cid))==0:
        return False
    else:
        return True


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    databases.insert_users(cid)
    if m.chat.type == 'private':
        if admin_group(cid)==False :
            is_member_channel1 = is_user_member(cid,channel1_id)
            is_member_channel2 = is_user_member(cid, channel2_id)
            if is_member_channel1 and is_member_channel2:
                bot.send_message(cid,"لظفا برای استفاده از ربات آنرا داخل گروه خود ادد کرده و دستور /start را بزنید و مجددا روی دکمه کلیک کرده و کشور خود اتنظیم کنید")
            elif is_member_channel1:
                markup=InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton("کانال",url="https://t.me/+Bz0Yy93sijY3Mjdk"))
                markup.add(InlineKeyboardButton("تایید عضویت",callback_data="member_confirm"))
                bot.send_message(cid,"هنوز در کانال زیر عضو نشده اید",reply_markup=markup)
            elif is_member_channel2:
                markup=InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton("کانال",url="https://t.me/+o_41_HeewJVhZWI8"))
                markup.add(InlineKeyboardButton("تایید عضویت",callback_data="member_confirm"))
                bot.send_message(cid,"هنوز در کانال زیر عضو نشده اید",reply_markup=markup)
            else:
                markup=InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton("کانال",url="https://t.me/+Bz0Yy93sijY3Mjdk"))
                markup.add(InlineKeyboardButton("کانال",url="https://t.me/+o_41_HeewJVhZWI8"))
                markup.add(InlineKeyboardButton("تایید عضویت",callback_data="member_confirm"))
                bot.send_message( cid, "برای استفاده کامل، لطفاً در هر دو کانال عضو شوید.",reply_markup=markup)
        elif admin_group(cid):
            dict_in=databases.check_cid(cid)
            if len(dict_in)==1:
                for i in dict_in:
                    if i["country"]=="None":
                        markup=InlineKeyboardMarkup()
                        markup.add(InlineKeyboardButton("عراق",callback_data=f"select_country_Iraq_{i['chat_id']}"))
                        markup.add(InlineKeyboardButton("یمن",callback_data=f"select_country_Yemen_{i['chat_id']}"))
                        markup.add(InlineKeyboardButton("مصر",callback_data=f"select_country_Egypt_{i['chat_id']}"))
                        markup.add(InlineKeyboardButton("لیبی",callback_data=f"select_country_Libya_{i['chat_id']}"))
                        markup.add(InlineKeyboardButton("السعوديه",callback_data=f"select_country_Saudi_{i['chat_id']}"))
                        markup.add(InlineKeyboardButton("سوریه",callback_data=f"select_country_Syria_{i['chat_id']}"))
                        bot.send_message(cid,f'لطفا کشور خود را برای گپ {i["title"]} انتخاب نمایید',reply_markup=markup)
                        break
                    elif i["country"]!="None" and i["city"]=="None":
                        markup=InlineKeyboardMarkup()
                        markup.add(InlineKeyboardButton("انتخاب شهر",callback_data=f"select_country_{i['country']}_{i['chat_id']}"))
                        bot.send_message(cid,'لطفا شهر خود را انتخاب نمایید',reply_markup=markup)
                        break
                    elif i["city"]!="None":
                        markup2=InlineKeyboardMarkup()
                        markup2.add(InlineKeyboardButton("ویرایش اطلاعات",callback_data=f"confirm_{i['country']}_{i['city']}_{i['chat_id']}"))
                        markup2.add(InlineKeyboardButton("تغییر کشور",callback_data=f"change_country_{i['chat_id']}"))
                        bot.send_message(cid,'کشور شما و شهر شما در سیستم ثبت شده است برای ویرایش اطلاعات خود از دکمه زیر استفاده کنید',reply_markup=markup2)
                        break
            else:
                markup=InlineKeyboardMarkup()
                for i in dict_in:
                    markup.add(InlineKeyboardButton(i["title"],callback_data=f"choise_{i['chat_id']}"))
                bot.send_message(cid,"""⭐️خوش برگشتی⭐️
میخواهید تغییرات را برای کدام یک از گپ های خود انجام دهید""",reply_markup=markup)

@bot.message_handler(commands=['panel'])
def command_start_p(m):
    cid = m.chat.id
    if m.chat.type =="private":
        if cid == admins:
            keypanel = InlineKeyboardMarkup()
            keypanel.add(InlineKeyboardButton('آمار',callback_data='panel_amar'))
            keypanel.add(InlineKeyboardButton('ارسال همگانی',callback_data='panel_brodcast'),InlineKeyboardButton('فوروارد همگانی',callback_data='panel_forall'))
            keypanel.add(InlineKeyboardButton('ارسال به گروه ها',callback_data='panel_brgp'),InlineKeyboardButton('فوروارد به گروه ها',callback_data='panel_forgp'))
            keypanel.add(InlineKeyboardButton("تنظیمات دکمه های اذان",callback_data='setting'))
            bot.send_message(cid,'سلام ادمین گرامی خوش امدید لطفا انتخاب کنید',reply_markup=keypanel)


@bot.message_handler(func=lambda m: m.chat.type == 'group' or m.chat.type == 'supergroup' and m.text=="نصب")
def install_robot(m):
    group_id = m.chat.id
    bot_info=bot.get_me()
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("تنظیمات ربات",url=f"https://t.me/{bot_info.username}/?start=setting"))
    bot.copy_message(group_id,chanal_base,11,reply_markup=markup,reply_to_message_id=m.message_id)


@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def handle_new_member(m):
    group_id = m.chat.id
    cid=m.from_user.id
    bot_info=bot.get_me()
    if m.new_chat_members[0].username==bot_info.username:
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("تنظیمات ربات",url=f"https://t.me/{bot_info.username}/?start=setting"))
        bot.copy_message(group_id,chanal_base,2,reply_markup=markup)
    list_y=databases.select_all_info()
    insert=True
    for i in list_y:
        if i["cid"]==cid and i["chat_id"]==group_id:
            insert=False
    if insert:
        databases.insert_table_admin_group(cid,group_id,m.chat.title)
    # if group_id not in group_ids:
    #     chat_ids.append(chat_id)
    #     print(f"Added chat_id {chat_id} to the list.")

@bot.callback_query_handler(func=lambda call: call.data.startswith("member"))
def call_callback_data(call):
    cid = call.message.chat.id
    command_start(call.message)


def is_user_member(user_id, channel_id):
    try:
        chat_member = bot.get_chat_member(channel_id, user_id)
        return chat_member.status == "member" or chat_member.status == "administrator" or chat_member.status == "creator"
    except Exception as e:
        print(f"Error checking membership: {e}")
        return False


@bot.message_handler(content_types=['photo','video',"video_note","audio","voice","document","sticker","location","contact","text"])
def panel_set_photo(m):
    global userstep
    cid = m.chat.id
    mid = m.message_id
    if m.chat.type=="private":
        text=m.text
        if userstep==1:
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("تایید",callback_data=f"sends_brodcast_{mid}"))
            markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
            bot.send_message(cid,"پیام شما دریافت شد برای ارسال همگانی تایید را بزنید",reply_markup=markup)
            userstep=0
        elif userstep==2:
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("تایید",callback_data=f"sends_forall_{mid}"))
            markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
            bot.send_message(cid,"پیام شما دریافت شد برای فوروارد همگانی تایید را بزنید",reply_markup=markup)
            userstep=0
        elif userstep==3:
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("تایید",callback_data=f"sends_brgp_{mid}"))
            markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
            bot.send_message(cid,"پیام شما دریافت شد برای ارسال به گروه ها تایید را بزنید",reply_markup=markup)  
            userstep=0  
        elif userstep==4:
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("تایید",callback_data=f"sends_forgp_{mid}"))
            markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
            bot.send_message(cid,"پیام شما دریافت شد برای فوروارد به گروه ها تایید را بزنید",reply_markup=markup) 
            userstep=0
        elif userstep==10:
            dict_channel.setdefault(text,"")   
            bot.send_message(cid,"اسم دکمه اضافه شد حالا برای ساخت دکمه لینک گروه را ارسال کنید")
            userstep=20
        elif userstep==20:
            for i in dict_channel:
                if dict_channel[i]=="":
                    dict_channel[i]=text
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
            bot.send_message(cid,"دکمه اضافه شد",reply_markup=markup)
            userstep=0
        else:
            bot.send_message(cid,"مقدار وارد شده نامعتبر است لطفا طبق دستور /start مجددا امتحان کنید")   
            userstep=0



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
                print("eror")
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
                print("eror")
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        text=f"به {count} نفر ارسال شد"
        if count_black!=0:
            text=f"\n و به {count_black} نفر ارسال نشد احتمالا ربات را بلاک کرده اند و از دیتابیس ما حذف میشوند \n"
        bot.edit_message_text(text,cid,mid,reply_markup=markup)
    if data[1] =="brgp":
        list_group=databases.select_all_info()
        for i in list_group:
            try:
                bot.copy_message(i["chat_id"],cid,int(data[-1]))
                count+=1
            except:
                print("eror")
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text(f"به {count} گروه ارسال شد",cid,mid,reply_markup=markup)
    if data[1] =="forgp":
        list_group=databases.select_all_info()
        for i in list_group:
            try:
                bot.forward_message(i["chat_id"],cid,int(data[-1]))
                count+=1
            except:
                print("eror")
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text(f"به {count} گروه فوروارد شد",cid,mid,reply_markup=markup)
    count=0

@bot.callback_query_handler(func=lambda call: call.data.startswith("back"))
def call_callback_panel_amar(call):
    global userstep
    cid = call.message.chat.id
    mid = call.message.message_id
    userstep=0
    keypanel = InlineKeyboardMarkup()
    keypanel.add(InlineKeyboardButton('آمار',callback_data='panel_amar'))
    keypanel.add(InlineKeyboardButton('ارسال همگانی',callback_data='panel_brodcast'),InlineKeyboardButton('فوروارد همگانی',callback_data='panel_forall'))
    keypanel.add(InlineKeyboardButton('ارسال به گروه ها',callback_data='panel_brgp'),InlineKeyboardButton('فوروارد به گروه ها',callback_data='panel_forgp'))
    keypanel.add(InlineKeyboardButton("تنظیمات دکمه های اذان",callback_data='setting'))
    bot.edit_message_text(' لطفا انتخاب کنید',cid,mid,reply_markup=keypanel)


@bot.callback_query_handler(func=lambda call: call.data.startswith("hazf"))
def call_callback_panel_setting(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_") 
    dict_channel.pop(data[-1])
    markup=InlineKeyboardMarkup()
    for i in dict_channel:
        txt="حذف" + i
        markup.add(InlineKeyboardButton(txt,dict_channel[i],callback_data=f"hazf_{i}"))
    markup.add(InlineKeyboardButton("اضافه کردن دکمه",callback_data="aadding"))
    bot.edit_message_text("با استفاده از دکمه های زیر میتوانید دکمه‌هایی را که برای اطلاع رسانی اذان ساخته شده ویرایش کنید",cid,mid,reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("setting"))
def call_callback_panel_setting(call):
    global userstep
    cid = call.message.chat.id
    mid = call.message.message_id
    if len(dict_channel)==0:
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text("لطفا برای اضافه کردن دکمه نام دکمه را وارد کنید و در غیر این صورت به پنل برگردید",cid,mid,reply_markup=markup)
        userstep=10
    elif len(dict_channel)>=1:
        markup=InlineKeyboardMarkup()
        for i in dict_channel:
            txt=" حذف" +" "+ i
            markup.add(InlineKeyboardButton(txt,callback_data=f"hazf_{i}"))
        markup.add(InlineKeyboardButton("اضافه کردن دکمه",callback_data="aadding"))
        bot.edit_message_text("با استفاده از دکمه های زیر میتوانید دکمه‌هایی را که برای اطلاع رسانی اذان ساخته شده ویرایش کنید",cid,mid,reply_markup=markup)
def setting_markup():
    if len(dict_channel)==0:
        return None
    else:
        markup=InlineKeyboardMarkup()
        for i in dict_channel:
            markup.add(InlineKeyboardButton(i,url=dict_channel[i]))
        return markup
    
@bot.callback_query_handler(func=lambda call: call.data.startswith("aadding"))
def call_callback_panel_sends(call):
    global userstep
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")  
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
    bot.edit_message_text("لطفا برای اضافه کردن دکمه نام دکمه را وارد کنید و در غیر این صورت به پنل برگردید",cid,mid,reply_markup=markup)
    userstep=10
    
@bot.callback_query_handler(func=lambda call: call.data.startswith("panel"))
def call_callback_panel_amar(call):
    global userstep
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")[-1]
    if data=="amar":
        countOfUsers=len(databases.use_users())

        countOfGp=len(databases.select_all_info())
        txt = f'آمار کاربران: {countOfUsers}\n آمار گروه ها : {countOfGp}'
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text(txt,cid,mid,reply_markup=markup)
    elif data=="brodcast":
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text("برای ارسال همگانی پیام لطفا پیام خود را ارسال کنید و در غیر این صورت برای بازگشت به پنل از دکمه زیر استفاده کنید",cid,mid,reply_markup=markup)
        userstep=1
    elif data=="forall":
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text("برای فوروارد همگانی پیام لطفا پیام خود را ارسال کنید و در غیر این صورت برای بازگشت به پنل از دکمه زیر استفاده کنید",cid,mid,reply_markup=markup)
        userstep=2
    elif data=="brgp":
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text("برای ارسال پیام به گروه ها لطفا پیام خود را ارسال کنید و در غیر این صورت برای بازگشت به پنل از دکمه زیر استفاده کنید",cid,mid,reply_markup=markup)
        userstep=3    
    elif data=="forgp":
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text("برای فوروارد پیام به گروه ها لطفا پیام خود را ارسال کنید و در غیر این صورت برای بازگشت به پنل از دکمه زیر استفاده کنید",cid,mid,reply_markup=markup)
        userstep=4     




@bot.callback_query_handler(func=lambda call: call.data.startswith("choise"))
def call_callback_data_choise(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")
    dict_in=databases.check_cid_chat_id(cid,int(data[-1]))
    for i in dict_in:
        if str(i["chat_id"])==str(data[-1]):
            if i["country"]=="None":
                markup=InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton("عراق",callback_data=f"select_country_Iraq_{data[-1]}"))
                markup.add(InlineKeyboardButton("یمن",callback_data=f"select_country_Yemen_{data[-1]}"))
                markup.add(InlineKeyboardButton("مصر",callback_data=f"select_country_Egypt_{data[-1]}"))
                markup.add(InlineKeyboardButton("لیبی",callback_data=f"select_country_Libya_{data[-1]}"))
                markup.add(InlineKeyboardButton("السعوديه",callback_data=f"select_country_Saudi_{data[-1]}"))
                markup.add(InlineKeyboardButton("سوریه",callback_data=f"select_country_Syria_{data[-1]}"))
                bot.edit_message_text(f'لطفا کشور خود را برای گپ {i["title"]} انتخاب نمایید',cid,mid,reply_markup=markup)
                break
            elif i["country"]!="None" and i["city"]=="None":
                markup=InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton("انتخاب شهر",callback_data=f"select_country_{i['country']}_{data[-1]}"))
                bot.edit_message_text('لطفا شهر خود را انتخاب نمایید',cid,mid,reply_markup=markup)
                break
            elif i["city"]!="None":
                markup2=InlineKeyboardMarkup()
                markup2.add(InlineKeyboardButton("ویرایش اطلاعات",callback_data=f"confirm_{i['country']}_{i['city']}_{data[-1]}"))
                markup2.add(InlineKeyboardButton("تغییر کشور",callback_data=f"change_country_{data[-1]}"))
                bot.edit_message_text('کشور شما و شهر شما در سیستم ثبت شده است برای ویرایش اطلاعات خود از دکمه زیر استفاده کنید',cid,mid,reply_markup=markup2)
                break



def gen_markup(country):
    country=country.split("_")
    if country[0]=="Iraq":
        iraq_cities = ["Baghdad", "Al Basrah", "Diyala", "Karbala", "Najaf", "Babil"]
        markup = InlineKeyboardMarkup()
        for city in iraq_cities:
            markup.add(InlineKeyboardButton(city, callback_data=f"select_city_Iraq_{city}_{country[-1]}"))
        return markup
    elif country[0]=="Yemen":
        yemen_cities = ["Sanaa", "Aden","Al Hudaydah", "Ta'izz","Al Mahrah","Ibb"]
        markup = InlineKeyboardMarkup()
        for city in yemen_cities:
            markup.add(InlineKeyboardButton(city, callback_data=f"select_city_Yemen_{city}_{country[-1]}"))
        return markup
    elif country[0]=="Egypt":
        egypt_cities = ["Cairo", "Giza", "Sohag", "Al Gharbiyah", "Al Minufiyah", "Ash Sharqiyah"]
        markup = InlineKeyboardMarkup()
        for city in egypt_cities:
            markup.add(InlineKeyboardButton(city, callback_data=f"select_city_Egypt_{city}_{country[-1]}"))
        return markup
    elif country[0]=="Libya":
        libya_cities = ["Tripoli", "Benghazi", "Sabha", "Bani Walid", "Zliten", "Tarhuna"]
        markup = InlineKeyboardMarkup()
        for city in libya_cities:
            markup.add(InlineKeyboardButton(city, callback_data=f"select_city_Libya_{city}_{country[-1]}"))
        return markup
    elif country[0]=="saudi":
        saudi_cities = ["Riyadh", "Makkah", "Madinah", "Dammam", "Abha", "Buraydah"]
        markup = InlineKeyboardMarkup()
        for city in saudi_cities:
            markup.add(InlineKeyboardButton(city, callback_data=f"select_city_Saudi_{city}_{country[-1]}"))
        return markup
    elif country[0]=="syria":
        syria_cities = ["Damascus", "Aleppo", "Homs", "Hama", "Tartus", "Idlib"]
        markup = InlineKeyboardMarkup()
        for city in syria_cities:
            markup.add(InlineKeyboardButton(city, callback_data=f"select_city_Syria_{city}_{country[-1]}"))
        return markup




@bot.callback_query_handler(func=lambda call: call.data.startswith("cooonfirm"))
def call_callback_data_cooooonfirm(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")
    azan_str=""""""
    dict_azan=databases.check_cid_chat_id(cid,int(data[-1]))
    for i in dict_azan:
        if i["fajr"]!="None":
            azan_str+='صبح : '+i["fajr"]+'\n'
        if i["dhuhr"]!="None":
            azan_str+='ظهر : '+i["dhuhr"]+'\n'
        if i["maghrib"]!="None":
            azan_str+='مغرب : '+i["maghrib"]+'\n'
        if i["isha"]!="None":
            azan_str+='عشاء : '+i["isha"]+'\n'
        if i["Asr"]!="None":
            azan_str+='عصر : '+i["Asr"]+'\n'
        break
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("منوی اصلی",callback_data="menu"))
    bot.edit_message_text(f"""✅تغییرات ذخیره شد✅

در گروه شما اذان های
{azan_str}
اطلاعات رسانی می‌شود
                          """,cid,mid)
    bot.send_message(int(data[-1]),f"""✅تغییرات ذخیره شد✅

در گروه شما اذان های
{azan_str}
اطلاعات رسانی می‌شود
                          """)
    azan_str=""""""


@bot.callback_query_handler(func=lambda call: call.data.startswith("change_country"))
def call_callback_data_change_country(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")
    databases.update_table_admin_group(cid,int(data[-1]),"country",'None')
    databases.update_table_admin_group(cid,int(data[-1]),"city",'None')
    databases.update_table_admin_group(cid,int(data[-1]),"fajr",'None')
    databases.update_table_admin_group(cid,int(data[-1]),"dhuhr",'None')
    databases.update_table_admin_group(cid,int(data[-1]),"maghrib",'None')
    databases.update_table_admin_group(cid,int(data[-1]),"isha",'None')
    databases.update_table_admin_group(cid,int(data[-1]),"Asr","None")
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("عراق",callback_data=f"select_country_Iraq_{data[-1]}"))
    markup.add(InlineKeyboardButton("یمن",callback_data=f"select_country_Yemen_{data[-1]}"))
    markup.add(InlineKeyboardButton("مصر",callback_data=f"select_country_Egypt_{data[-1]}"))
    markup.add(InlineKeyboardButton("لیبی",callback_data=f"select_country_Libya_{data[-1]}"))
    markup.add(InlineKeyboardButton("السعوديه",callback_data=f"select_country_Saudi_{data[-1]}"))
    markup.add(InlineKeyboardButton("سوریه",callback_data=f"select_country_Syria_{data[-1]}"))
    bot.edit_message_text(chat_id=cid,message_id=mid,text='لطفا کشور خود را انتخاب نمایید',reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("confirm"))
def call_callback_data_confirm(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")
    dict_time=azan.get_prayer_times(data[1], data[2])
    markup=InlineKeyboardMarkup()
    dict_info=databases.check_cid_chat_id(cid,int(data[-1]))
    for i in dict_info:
        if i["fajr"] == dict_time["Fajr"]:
            fajr="✅"
            markup.add(InlineKeyboardButton("حذف اذان صبح",callback_data=f"del_Fajr_{data[1]}_{data[2]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان صبح",callback_data=f"time_Fajr_{data[1]}_{data[2]}_{data[-1]}"))
            fajr="❌"
        if i["dhuhr"] == dict_time["Dhuhr"]:
            dhuhr="✅"
            markup.add(InlineKeyboardButton("حذف اذان ظهر",callback_data=f"del_Dhuhr_{data[1]}_{data[2]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان ظهر",callback_data=f"time_Dhuhr_{data[1]}_{data[2]}_{data[-1]}"))
            dhuhr="❌"
        if i["maghrib"] == dict_time["Maghrib"]:
            maghrib="✅"
            markup.add(InlineKeyboardButton("حذف اذان مغرب",callback_data=f"del_Maghrib_{data[1]}_{data[2]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان مغرب",callback_data=f"time_Maghrib_{data[1]}_{data[2]}_{data[-1]}"))
            maghrib="❌"
        if i["asr"] == dict_time["Asr"]:
            asr="✅"
            markup.add(InlineKeyboardButton("حذف اذان عصر",callback_data=f"del_Asr_{data[1]}_{data[2]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان عصر",callback_data=f"time_Asr_{data[1]}_{data[2]}_{data[-1]}"))
            asr="❌"
        if i["isha"] == dict_time["Isha"]:
            isha="✅"
            markup.add(InlineKeyboardButton("حذف اذان عشا",callback_data=f"del_Isha_{data[1]}_{data[2]}_{data[-1]}"))
        else:
            isha="❌"
            markup.add(InlineKeyboardButton("اذان عشا",callback_data=f"time_Isha_{data[1]}_{data[2]}_{data[-1]}"))
        markup.add(InlineKeyboardButton("ثبت تغییرات",callback_data=f"cooonfirm_{data[-1]}"))
    bot.edit_message_text(f"""
لطفا انتخاب کنید در زمان کدام اذان ها داخل گپ اطلاع رسانی شود

🕋تایم اذان🕋
اذان صبح: {dict_time["Fajr"]}   {fajr}

اذان ظهر: {dict_time["Dhuhr"]}   {dhuhr}

اذان مغرب: {dict_time["Maghrib"]}   {maghrib}

اذان عصر: {dict_time["Asr"]}       {asr}

اذان عشا: {dict_time["Isha"]}       {isha}

طلوع آفتاب: {dict_time["Sunrise"]}

""", cid, message_id=mid, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data.startswith("select"))
def call_callback_data(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")
    if data[1]=="country":
        if data[2] == 'Iraq':
            bot.edit_message_text("لطفا شهر خود را انتخاب نمایید", cid, message_id=mid, reply_markup=gen_markup(f'Iraq_{data[-1]}'))
        elif data[2] == 'Yemen':
            bot.edit_message_text("لطفا شهر خود را انتخاب نمایید", cid, message_id=mid, reply_markup=gen_markup(f'Yemen_{data[-1]}'))
        elif data[2] == 'Egypt':
            bot.edit_message_text("لطفا شهر خود را انتخاب نمایید", cid, message_id=mid, reply_markup=gen_markup(f'Egypt_{data[-1]}'))
        elif data[2] == 'Libya':
            bot.edit_message_text("لطفا شهر خود را انتخاب نمایید", cid, message_id=mid, reply_markup=gen_markup(f'Libya_{data[-1]}'))
        elif data[2] == "Saudi":
            bot.edit_message_text("لطفا شهر خود را انتخاب نمایید", cid, message_id=mid, reply_markup=gen_markup(f'saudi_{data[-1]}'))
        elif data[2] == "Syria":
            bot.edit_message_text("لطفا شهر خود را انتخاب نمایید", cid, message_id=mid, reply_markup=gen_markup(f'syria_{data[-1]}'))

    elif data[1]=="city":
        databases.update_table_admin_group(cid,int(data[-1]),"country",data[2])
        databases.update_table_admin_group(cid,int(data[-1]),"city",data[3])
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("تایید",callback_data=f"confirm_{data[2]}_{data[3]}_{data[-1]}"))
        markup.add(InlineKeyboardButton("تغییر کشور و شهر",callback_data=f"select_country_{data[-1]}"))
        bot.edit_message_text(f"شما کشور {data[2]} و شهر {data[3]} را اانتخاب کردید.", cid, message_id=mid, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("time") or call.data.startswith("del"))#"time_Fajr_Libya_jjjj"
def call_callback_time(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")
    dict_time=azan.get_prayer_times(data[2], data[3])
    databases.update_table_admin_group(cid,int(data[-1]),data[1],dict_time[data[1]])
    if data[0]=="del":
        databases.update_table_admin_group(cid,int(data[-1]),data[1],"None")
    if data[1]=="Fajr":
        bot.answer_callback_query(call.id,"اذان صبح ذخیره شد")
    elif data[1]=="Dhuhr":
        bot.answer_callback_query(call.id,"اذان ظهر ذخیره شد")
    elif data[1]=="Maghrib":
        bot.answer_callback_query(call.id,"اذان مغرب ذخیره شد")
    elif data[1]=="Asr":
        bot.answer_callback_query(call.id,"اذان عصر ذخیره شد")
    elif data[1]=="Isha":
        bot.answer_callback_query(call.id,"اذان عشا ذخیره شد")
    markup=InlineKeyboardMarkup()
    dict_info=databases.check_cid_chat_id(cid,int(data[-1]))
    for i in dict_info:
        if i["fajr"] == dict_time["Fajr"]:
            fajr="✅"
            markup.add(InlineKeyboardButton("حذف اذان صبح",callback_data=f"del_Fajr_{data[2]}_{data[3]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان صبح",callback_data=f"time_Fajr_{data[2]}_{data[3]}_{data[-1]}"))
            fajr="❌"
        if i["dhuhr"] == dict_time["Dhuhr"]:
            dhuhr="✅"
            markup.add(InlineKeyboardButton("حذف اذان ظهر",callback_data=f"del_Dhuhr_{data[2]}_{data[3]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان ظهر",callback_data=f"time_Dhuhr_{data[2]}_{data[3]}_{data[-1]}"))
            dhuhr="❌"
        if i["maghrib"] == dict_time["Maghrib"]:
            maghrib="✅"
            markup.add(InlineKeyboardButton("حذف اذان مغرب",callback_data=f"del_Maghrib_{data[2]}_{data[3]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان مغرب",callback_data=f"time_Maghrib_{data[2]}_{data[3]}_{data[-1]}"))
            maghrib="❌"
        if i["asr"] == dict_time["Asr"]:
            asr="✅"
            markup.add(InlineKeyboardButton("حذف اذان عصر",callback_data=f"del_Asr_{data[2]}_{data[3]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان عصر",callback_data=f"time_Asr_{data[2]}_{data[3]}_{data[-1]}"))
            asr="❌"
        if i["isha"] == dict_time["Isha"]:
            isha="✅"
            markup.add(InlineKeyboardButton("حذف اذان عشا",callback_data=f"del_Isha_{data[2]}_{data[3]}_{data[-1]}"))
        else:
            isha="❌"
            markup.add(InlineKeyboardButton("اذان عشا",callback_data=f"time_Isha_{data[2]}_{data[3]}_{data[-1]}"))
        markup.add(InlineKeyboardButton("ثبت تغییرات",callback_data=f"cooonfirm_{data[-1]}"))
    bot.edit_message_text(f"""
لطفا انتخاب کنید در زمان کدام اذان ها داخل گپ اطلاع رسانی شود

🕋تایم اذان🕋
اذان صبح: {dict_time["Fajr"]}   {fajr}

اذان ظهر: {dict_time["Dhuhr"]}   {dhuhr}

اذان مغرب: {dict_time["Maghrib"]}   {maghrib}

اذان عصر: {dict_time["Asr"]}       {asr}

اذان عشا: {dict_time["Isha"]}       {isha}

طلوع آفتاب: {dict_time["Sunrise"]}

""",cid,mid,reply_markup=markup)




def check_and_notify_thread():
    while True:
        print("ok")
        dict_ii=databases.select_all_info()
        for c in dict_ii:
            bot_user_id=bot.get_me().id
            try:
                chat_member=bot.get_chat_member(int(c["chat_id"]),bot_user_id)
                if chat_member.status in ["member","administrator","creator"]:
                    pass
            except:
                databases.delete_row(c["chat_id"])


        if datetime.now().strftime("%H:%M") == "00:05":
            dict_ii2=databases.select_all_info()
            for b in dict_ii2:
                if b["country"]!="None" and b["city"]!="None":
                    dict_time=azan.get_prayer_times(b["country"],b["city"])
                    if b["Fajr"]!="None":
                        databases.update_table_admin_group(b["cid"],b["chat_id"],"Fajr",dict_time["Fajr"])
                    if b["Dhuhr"]!="None":
                        databases.update_table_admin_group(b["cid"],b["chat_id"],"Dhuhr",dict_time["Dhuhr"])
                    if b["Maghrib"]!="None":
                        databases.update_table_admin_group(b["cid"],b["chat_id"],"Maghrib",dict_time["Maghrib"])
                    if b["Asr"]!="None":
                        databases.update_table_admin_group(b["cid"],b["chat_id"],"Asr",dict_time["Asr"])
                    if b["Isha"]!="None":
                        databases.update_table_admin_group(b["cid"],b["chat_id"],"Isha",dict_time["Isha"])

        rows = databases.select_all_info()
        dict_code_message={"Fajr":4,"Dhuhr":5,"Asr":6,"Maghrib":7,"Isha":8}
        current_time ="05:25" #datetime.now().strftime("%H:%M")
        print(rows)
        for row in rows:
            
            for i in ["Fajr","Dhuhr","Maghrib","Asr","Isha"]:
                print(row[i])
                if row[i] != "None":
                    if current_time == row[i]:
                        try:
                            bot.copy_message(row["chat_id"],chanal_base,dict_code_message[i],reply_markup=setting_markup())
                        except:
                            print("left")
        threading.Event().wait(55)


check_thread = threading.Thread(target=check_and_notify_thread)
check_thread.start()


bot.infinity_polling()



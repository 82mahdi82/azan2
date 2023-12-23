import telebot
import pytz
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import azan
import databases
from datetime import datetime
import threading
from config import *
admins=752815712
channel1_id = -1001463465504 # Replace with your channel1 ID
channel2_id = -1001064767998  # Replace with your channel2 ID
chanal_base=-1002029203141
userstep=0
dict_channel={} #{"name":"utl"}
databases.creat_database_tables()
# def listener(messages):
#     """
#     When new messages arrive TeleBot will call this function.
#     """
#     for m in messages:
#         cid = m.chat.id
#         if m.content_type == 'text':
#             print(str(m.chat.first_name) +
#                   " [" + str(m.chat.id) + "]: " + m.text)
#         elif m.content_type == 'photo':
#             print(str(m.chat.first_name) +
#                   " [" + str(m.chat.id) + "]: " + "New photo recieved")
#         elif m.content_type == 'document':
#             print(str(m.chat.first_name) +
#                   " [" + str(m.chat.id) + "]: " + 'New Document recieved')


bot = telebot.TeleBot(TOKEN,num_threads=3)
# bot.set_update_listener(listener)


def admin_group(cid):
    if len(databases.use_table_admin_group(cid))==0:
        return False
    else:
        return True


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if m.chat.type == 'private':
        databases.insert_users(cid)
        if admin_group(cid)==False :
            is_member_channel1 = is_user_member(cid,channel1_id)
            is_member_channel2 = is_user_member(cid, channel2_id)
            if is_member_channel1 and is_member_channel2:
                bot.send_message(cid,"#هلا_عمري 🤍🫂\n\n⌁ : تعرف على بوُت مواقيت الصلاه\n⌁ : قم بأضافه البوت ورفعه مشرف ثم اكتب تفعيل\n⌁ : أفضل بوت لأرسال ميديا وقت الصلاه لبلد العراق - السعوديه - مصر - اليمن - سوريا - ليبيا .\n┉ ≈ ┉ ≈ ┉ ≈ ┉ ≈ ┉ ≈ ┉\n⌁ : نقوم بتحديث بوت المواقيت بشكل شهري وعلا آخر اصدار للغه بايثون واضافه مميزات لا تتوفر في باقي البوتات 🍇  .")
            elif is_member_channel1:
                markup=InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton("قناتنا",url="https://t.me/+cZWUjoZShDtkOWZk"))
                markup.add(InlineKeyboardButton("تاكيد الانضمام",callback_data="member_confirm"))
                bot.send_message(cid,"- للاسف انت لم تقوم بالاشتراك للقناه",reply_markup=markup)
            elif is_member_channel2:
                markup=InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton("قناتنا",url="https://t.me/+Wy_FN4GkkBFmMTk0"))
                markup.add(InlineKeyboardButton("تاكيد الانضمام",callback_data="member_confirm"))
                bot.send_message(cid,"- للاسف انت لم تقوم بالاشتراك للقناه",reply_markup=markup)
            else:
                markup=InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton("قناتنا",url="https://t.me/+cZWUjoZShDtkOWZk"))
                markup.add(InlineKeyboardButton("قناتنا",url="https://t.me/+Wy_FN4GkkBFmMTk0"))
                markup.add(InlineKeyboardButton("تاكيد الانضمام",callback_data="member_confirm"))
                bot.send_message( cid, "⌁ : لاستخدام البوت عليك الاشتراك بالقناتين.",reply_markup=markup)
        elif admin_group(cid):
            dict_in=databases.check_cid(cid)
            if len(dict_in)==1:
                for i in dict_in:
                    if i["country"]=="None":
                        markup=InlineKeyboardMarkup()
                        markup.add(InlineKeyboardButton("العراق",callback_data=f"select_country_Iraq_{i['chat_id']}"))
                        markup.add(InlineKeyboardButton("اليمن",callback_data=f"select_country_Yemen_{i['chat_id']}"))
                        markup.add(InlineKeyboardButton("مصر",callback_data=f"select_country_Egypt_{i['chat_id']}"))
                        markup.add(InlineKeyboardButton("ليبيا",callback_data=f"select_country_Libya_{i['chat_id']}"))
                        markup.add(InlineKeyboardButton("السعودية",callback_data=f"select_country_Saudi_{i['chat_id']}"))
                        markup.add(InlineKeyboardButton("سوريا",callback_data=f"select_country_Syria_{i['chat_id']}"))
                        bot.send_message(cid,f'⌁ : اختر بلدك للمجموعه {i["title"]} 💬',reply_markup=markup)
                        break
                    elif i["country"]!="None" and i["city"]=="None":
                        markup=InlineKeyboardMarkup()
                        markup.add(InlineKeyboardButton("المدينه",callback_data=f"select_country_{i['country']}_{i['chat_id']}"))
                        bot.send_message(cid,'⌁ : حسننا اختر مدينتك الان',reply_markup=markup)
                        break
                    elif i["city"]!="None":
                        markup2=InlineKeyboardMarkup()
                        markup2.add(InlineKeyboardButton("تعديل",callback_data=f"confirm_{i['country']}_{i['city']}_{i['chat_id']}"))
                        markup2.add(InlineKeyboardButton("تغيير البلد",callback_data=f"change_country_{i['chat_id']}"))
                        bot.send_message(cid,'⌁ : تم تسجيل بلدك ومدينتك في السيرفر. استخدم الزر أدناه لتعديل معلوماتك',reply_markup=markup2)
                        break
            else:
                markup=InlineKeyboardMarkup()
                for i in dict_in:
                    markup.add(InlineKeyboardButton(i["title"],callback_data=f"choise_{i['chat_id']}"))
                bot.send_message(cid,"""⌁ : مرحبًا بعودتك أي من محادثاتك أو مجموعتك تريد إجراء تغييرات عليها؟""",reply_markup=markup)

@bot.message_handler(commands=['panel'])
def command_start_p(m):
    cid = m.chat.id
    if m.chat.type =="private":
        if cid == admins:
            keypanel = InlineKeyboardMarkup()
            keypanel.add(InlineKeyboardButton('الاحصائيات',callback_data='panel_amar'))
            keypanel.add(InlineKeyboardButton('توجیه',callback_data='panel_brodcast'),InlineKeyboardButton('اذاعه بالتوجيه',callback_data='panel_forall'))
            keypanel.add(InlineKeyboardButton('اذاعه للمجموعات',callback_data='panel_brgp'),InlineKeyboardButton('توجيه للمجموعات',callback_data='panel_forgp'))
            keypanel.add(InlineKeyboardButton("ضبط الازرار",callback_data='setting'))
            bot.send_message(cid,'⌁ : مرحبا عزيزي المطور في بوت الاذكار',reply_markup=keypanel)


@bot.message_handler(func=lambda m: m.chat.type == 'group' or m.chat.type == 'supergroup' and m.text=="تفعيل")
def install_robot(m):
    group_id = m.chat.id
    cid=m.from_user.id
    bot_info=bot.get_me()
    chat_member = bot.get_chat_member(group_id, cid)
    if chat_member.status=="member":
        return
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("الاعدادات",url=f"https://t.me/{bot_info.username}/?start=setting"))
    bot.copy_message(group_id,chanal_base,11,reply_markup=markup,reply_to_message_id=m.message_id)


@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def handle_new_member(m):
    group_id = m.chat.id
    cid=m.from_user.id
    bot_info=bot.get_me()
    if m.new_chat_members[0].username==bot_info.username:
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("الاعدادات",url=f"https://t.me/{bot_info.username}/?start=setting"))
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
        #print(f"Error checking membership: {e}")
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
            markup.add(InlineKeyboardButton("نعم",callback_data=f"sends_brodcast_{mid}"))
            markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
            bot.send_message(cid,"⌁ : لقد تم استلام رسالتك. انقر على نعم لإرسالها إلى للمشتركين",reply_markup=markup)
            userstep=0
        elif userstep==2:
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("نعم",callback_data=f"sends_forall_{mid}"))
            markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
            bot.send_message(cid,"⌁ : لقد تم استلام رسالتك. انقر على نعم لإرسالها بالتوجيه إلى للمشتركين",reply_markup=markup)
            userstep=0
        elif userstep==3:
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("نعم",callback_data=f"sends_brgp_{mid}"))
            markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
            bot.send_message(cid,"⌁ : لقد تم استلام رسالتك. انقر على نعم لإرسالها إلى المجموعات",reply_markup=markup)  
            userstep=0  
        elif userstep==4:
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("نعم",callback_data=f"sends_forgp_{mid}"))
            markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
            bot.send_message(cid,"⌁ : لقد تم استلام رسالتك. انقر على نعم لإرسالها بالتوجيه إلى المجموعات",reply_markup=markup) 
            userstep=0
        elif userstep==10:
            dict_channel.setdefault(text,"")   
            bot.send_message(cid,"⌁ : تم اضافه اسم الزر قم الان بارسال الرابط")
            userstep=20
        elif userstep==20:
            for i in dict_channel:
                if dict_channel[i]=="":
                    dict_channel[i]=text
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
            bot.send_message(cid,"⌁ : تم اضافه الزر",reply_markup=markup)
            userstep=0
        else:
            bot.send_message(cid,"⌁ : اوبس. عزيزي لم افهم شي قم بالضغط علي /start وراسل الدعم")   
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
                # print("eror")
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
        text=f"⌁ : إلى{count} مشترك تم ارسالها"
        if count_black!=0:
            text=f"\n ⌁ : و إلى {count_black} مشترك لم استطع ارسالها ، ربما قاموا بحظر البوت وسيتم حذفهم من قاعدة البيانات الخاصة بنا \n"
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
        markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
        text=f"⌁ : إلى{count} مشترك تم ارسالها"
        if count_black!=0:
            text=f"\n ⌁ : و إلى {count_black} مشترك لم استطع ارسالها ، ربما قاموا بحظر البوت وسيتم حذفهم من قاعدة البيانات الخاصة بنا \n"
        bot.edit_message_text(text,cid,mid,reply_markup=markup)
    if data[1] =="brgp":
        list_group=databases.select_all_info()
        for i in list_group:
            try:
                bot.copy_message(i["chat_id"],cid,int(data[-1]))
                count+=1
            except:
                pass
                # print("eror")
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
        bot.edit_message_text(f"⌁ : إلى{count} مجموعه تم ارسالها",cid,mid,reply_markup=markup)
    if data[1] =="forgp":
        list_group=databases.select_all_info()
        for i in list_group:
            try:
                bot.forward_message(i["chat_id"],cid,int(data[-1]))
                count+=1
            except:
                pass
                # print("eror")
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
        bot.edit_message_text(f"⌁ : إلى{count} مجموعه تم ارسال التوجيه",cid,mid,reply_markup=markup)
    count=0

@bot.callback_query_handler(func=lambda call: call.data.startswith("back"))
def call_callback_panel_amar(call):
    global userstep
    cid = call.message.chat.id
    mid = call.message.message_id
    userstep=0
    keypanel = InlineKeyboardMarkup()
    keypanel.add(InlineKeyboardButton('الاحصائيات',callback_data='panel_amar'))
    keypanel.add(InlineKeyboardButton('توجیه',callback_data='panel_brodcast'),InlineKeyboardButton('اذاعه بالتوجيه',callback_data='panel_forall'))
    keypanel.add(InlineKeyboardButton('اذاعه للمجموعات',callback_data='panel_brgp'),InlineKeyboardButton('توجيه للمجموعات',callback_data='panel_forgp'))
    keypanel.add(InlineKeyboardButton("ضبط الازرار",callback_data='setting'))
    bot.edit_message_text(' ⌁ : حسننا عزيزي قم بالاختيار الان',cid,mid,reply_markup=keypanel)


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
    markup.add(InlineKeyboardButton("اضافه زر",callback_data="aadding"))
    bot.edit_message_text("⌁ : باستخدام الأزرار الموجودة بالأسفل يمكنك تعديل الأزرار المخصصة لإشعار الأذان",cid,mid,reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("setting"))
def call_callback_panel_setting(call):
    global userstep
    cid = call.message.chat.id
    mid = call.message.message_id
    if len(dict_channel)==0:
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
        bot.edit_message_text("⌁ : حسننا عزيزي قم بارسال اسم الزر",cid,mid,reply_markup=markup)
        userstep=10
    elif len(dict_channel)>=1:
        markup=InlineKeyboardMarkup()
        for i in dict_channel:
            txt=" حذف" +" "+ i
            markup.add(InlineKeyboardButton(txt,callback_data=f"hazf_{i}"))
        markup.add(InlineKeyboardButton("اضافه زر",callback_data="aadding"))
        bot.edit_message_text("⌁ : باستخدام الأزرار الموجودة بالأسفل يمكنك تعديل الأزرار المخصصة لإشعار الأذان",cid,mid,reply_markup=markup)
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
    markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
    bot.edit_message_text("⌁ : حسننا عزيزي قم بارسال اسم الزر",cid,mid,reply_markup=markup)
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
        txt = f'المشتركين: {countOfUsers}\n المجموعات : {countOfGp}'
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
        bot.edit_message_text(txt,cid,mid,reply_markup=markup)
    elif data=="brodcast":
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
        bot.edit_message_text("⌁ : حسننا ارسل رسالتك الان",cid,mid,reply_markup=markup)
        userstep=1
    elif data=="forall":
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
        bot.edit_message_text("⌁ : حسننا ارسل رسالتك بالتوجيه الان",cid,mid,reply_markup=markup)
        userstep=2
    elif data=="brgp":
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
        bot.edit_message_text("⌁ : حسننا ارسل رسالتك الان",cid,mid,reply_markup=markup)
        userstep=3    
    elif data=="forgp":
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("عوده",callback_data="back_panel"))
        bot.edit_message_text("⌁ : حسننا ارسل رسالتك بالتوجيه الان",cid,mid,reply_markup=markup)
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
                markup.add(InlineKeyboardButton("العراق",callback_data=f"select_country_Iraq_{data[-1]}"))
                markup.add(InlineKeyboardButton("اليمن",callback_data=f"select_country_Yemen_{data[-1]}"))
                markup.add(InlineKeyboardButton("مصر",callback_data=f"select_country_Egypt_{data[-1]}"))
                markup.add(InlineKeyboardButton("ليبيا",callback_data=f"select_country_Libya_{data[-1]}"))
                markup.add(InlineKeyboardButton("السعودية",callback_data=f"select_country_Saudi_{data[-1]}"))
                markup.add(InlineKeyboardButton("سوريا",callback_data=f"select_country_Syria_{data[-1]}"))
                bot.edit_message_text(f'⌁ : اختر بلدك للمجموعه {i["title"]} 💬',cid,mid,reply_markup=markup)
                break
            elif i["country"]!="None" and i["city"]=="None":
                markup=InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton("المدينه",callback_data=f"select_country_{i['country']}_{data[-1]}"))
                bot.edit_message_text('⌁ : حسننا اختر مدينتك الان',cid,mid,reply_markup=markup)
                break
            elif i["city"]!="None":
                markup2=InlineKeyboardMarkup()
                markup2.add(InlineKeyboardButton("تعديل",callback_data=f"confirm_{i['country']}_{i['city']}_{data[-1]}"))
                markup2.add(InlineKeyboardButton("تغيير البلد",callback_data=f"change_country_{data[-1]}"))
                bot.edit_message_text('⌁ : تم تسجيل بلدك ومدينتك في السيرفر. استخدم الزر أدناه لتعديل معلوماتك',cid,mid,reply_markup=markup2)
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
            azan_str+='الفجر : '+i["fajr"]+'\n'
        if i["dhuhr"]!="None":
            azan_str+='الظهر : '+i["dhuhr"]+'\n'
        if i["maghrib"]!="None":
            azan_str+='المغرب : '+i["maghrib"]+'\n'
        if i["isha"]!="None":
            azan_str+='العشاءء : '+i["isha"]+'\n'
        if i["Asr"]!="None":
            azan_str+='العصر : '+i["Asr"]+'\n'
        break
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("الرئيسيه",callback_data="menu"))
    bot.edit_message_text(f"""⌁ : مرحبا عزيزي المالك تم تثبيت التوقيت للصلاة حسب طلبك بنجاح

{azan_str}
                          """,cid,mid)
    bot.send_message(int(data[-1]),f"""⌁ : مرحبا عزيزي المالك تم تثبيت التوقيت للصلاة حسب طلبك بنجاح

{azan_str}
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
    markup.add(InlineKeyboardButton("العراق",callback_data=f"select_country_Iraq_{data[-1]}"))
    markup.add(InlineKeyboardButton("اليمن",callback_data=f"select_country_Yemen_{data[-1]}"))
    markup.add(InlineKeyboardButton("مصر",callback_data=f"select_country_Egypt_{data[-1]}"))
    markup.add(InlineKeyboardButton("ليبيا",callback_data=f"select_country_Libya_{data[-1]}"))
    markup.add(InlineKeyboardButton("السعودية",callback_data=f"select_country_Saudi_{data[-1]}"))
    markup.add(InlineKeyboardButton("سوريا",callback_data=f"select_country_Syria_{data[-1]}"))
    bot.edit_message_text(chat_id=cid,message_id=mid,text='⌁ : حسننا اختر بلدك الان',reply_markup=markup)

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
            markup.add(InlineKeyboardButton("حذف اذان الفجر",callback_data=f"del_Fajr_{data[1]}_{data[2]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان الفجر",callback_data=f"time_Fajr_{data[1]}_{data[2]}_{data[-1]}"))
            fajr="❌"
        if i["dhuhr"] == dict_time["Dhuhr"]:
            dhuhr="✅"
            markup.add(InlineKeyboardButton("حذف اذان الظهر",callback_data=f"del_Dhuhr_{data[1]}_{data[2]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان الظهر",callback_data=f"time_Dhuhr_{data[1]}_{data[2]}_{data[-1]}"))
            dhuhr="❌"
        if i["maghrib"] == dict_time["Maghrib"]:
            maghrib="✅"
            markup.add(InlineKeyboardButton("حذف اذان المغرب",callback_data=f"del_Maghrib_{data[1]}_{data[2]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان المغرب",callback_data=f"time_Maghrib_{data[1]}_{data[2]}_{data[-1]}"))
            maghrib="❌"
        if i["asr"] == dict_time["Asr"]:
            asr="✅"
            markup.add(InlineKeyboardButton("حذف اذان العصر",callback_data=f"del_Asr_{data[1]}_{data[2]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان العصر",callback_data=f"time_Asr_{data[1]}_{data[2]}_{data[-1]}"))
            asr="❌"
        if i["isha"] == dict_time["Isha"]:
            isha="✅"
            markup.add(InlineKeyboardButton("حذف اذان العشاء",callback_data=f"del_Isha_{data[1]}_{data[2]}_{data[-1]}"))
        else:
            isha="❌"
            markup.add(InlineKeyboardButton("اذان العشاء",callback_data=f"time_Isha_{data[1]}_{data[2]}_{data[-1]}"))
        markup.add(InlineKeyboardButton("حفظ التغيرات",callback_data=f"cooonfirm_{data[-1]}"))
    bot.edit_message_text(f"""
⌁ : يرجى اختيار الوقت الذي سيتم فيه نشر الاذكار والاذان في الدردشة

🕋مواقيت الصلاه🕋
اذان الفجر: {dict_time["Fajr"]}   {fajr}

اذان الظهر: {dict_time["Dhuhr"]}   {dhuhr}

اذان المغرب: {dict_time["Maghrib"]}   {maghrib}

اذان العصر: {dict_time["Asr"]}       {asr}

اذان العشاء: {dict_time["Isha"]}       {isha}

الشروق: {dict_time["Sunrise"]}

""", cid, message_id=mid, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data.startswith("select"))
def call_callback_data(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")
    if data[1]=="country":
        if data[2] == 'Iraq':
            bot.edit_message_text("⌁ : حسننا اختر مدينتك(🇮🇶)\n1- بغداد (Baghdad)\n2- البصره (Al Basrah)\n3- ديالئ (Diyala)\n4- كربلاء (Karbala)\n5- نجف (Najaf)\n6- بابل (Babil)", cid, message_id=mid, reply_markup=gen_markup(f'Iraq_{data[-1]}'))
        elif data[2] == 'Yemen':
            bot.edit_message_text("⌁ : حسننا عزيزي اختر مدينتك(🇾🇪)\n1- صنعاء (Sanaa)\n2- عدن (Aden)\n3- الحديده (Al Hudaydah)\n4- تعز (Taizz)\n5- المهره (Al Mahrah)\n6- اب (Ibb)", cid, message_id=mid, reply_markup=gen_markup(f'Yemen_{data[-1]}'))
        elif data[2] == 'Egypt':
            bot.edit_message_text("⌁ : حسننا عزيزي اختر مدينتك(🇪🇬)\n1- القاهرة (Cairo)\n2- الجيزه (Giza)\n3- سوهاج (Sohag)\n4- الغربيه (Al Gharbiyah)\n5- المنوفية (Al Minufiyah)\n6- الشرقيه (Ash Sharqiyah)", cid, message_id=mid, reply_markup=gen_markup(f'Egypt_{data[-1]}'))
        elif data[2] == 'Libya':
            bot.edit_message_text("⌁ : حسننا عزيزي اختر مدينتك(🇱🇾)\n1- طرابلس (Tripoli)\n2-  بنغازي (Benghazi)\n3- سبها (Sabha)\n4-  بني وليد (Bani Walid)\n5- زليتن (Zliten)\n6- ترهونه (Tarhuna)", cid, message_id=mid, reply_markup=gen_markup(f'Libya_{data[-1]}'))
        elif data[2] == "Saudi":
            bot.edit_message_text("⌁ : حسننا اختر مدينتك الان", cid, message_id=mid, reply_markup=gen_markup(f'saudi_{data[-1]}'))
        elif data[2] == "Syria":
            bot.edit_message_text("⌁ : حسننا اختر مدينتك الان", cid, message_id=mid, reply_markup=gen_markup(f'syria_{data[-1]}'))

    elif data[1]=="city":
        databases.update_table_admin_group(cid,int(data[-1]),"country",data[2])
        databases.update_table_admin_group(cid,int(data[-1]),"city",data[3])
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("نعم",callback_data=f"confirm_{data[2]}_{data[3]}_{data[-1]}"))
        markup.add(InlineKeyboardButton("البلد والمدينه",callback_data=f"change_country_{data[-1]}"))
        bot.edit_message_text(f"⌁ : انت اخترت بلد {data[2]} والمدينة {data[3]} .", cid, message_id=mid, reply_markup=markup)


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
        bot.answer_callback_query(call.id,"اذان الفجر تم ضبطه بنجاح")
    elif data[1]=="Dhuhr":
        bot.answer_callback_query(call.id,"اذان الظهر تم ضبطه بنجاح")
    elif data[1]=="Maghrib":
        bot.answer_callback_query(call.id,"اذان المغرب تم ضبطه بنجاح")
    elif data[1]=="Asr":
        bot.answer_callback_query(call.id,"اذان العصر تم ضبطه بنجاح")
    elif data[1]=="Isha":
        bot.answer_callback_query(call.id,"اذان العشاء تم ضبطه بنجاح")
    markup=InlineKeyboardMarkup()
    dict_info=databases.check_cid_chat_id(cid,int(data[-1]))
    for i in dict_info:
        if i["fajr"] == dict_time["Fajr"]:
            fajr="✅"
            markup.add(InlineKeyboardButton("حذف اذان الفجر",callback_data=f"del_Fajr_{data[2]}_{data[3]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان الفجر",callback_data=f"time_Fajr_{data[2]}_{data[3]}_{data[-1]}"))
            fajr="❌"
        if i["dhuhr"] == dict_time["Dhuhr"]:
            dhuhr="✅"
            markup.add(InlineKeyboardButton("حذف اذان الظهر",callback_data=f"del_Dhuhr_{data[2]}_{data[3]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان الظهر",callback_data=f"time_Dhuhr_{data[2]}_{data[3]}_{data[-1]}"))
            dhuhr="❌"
        if i["maghrib"] == dict_time["Maghrib"]:
            maghrib="✅"
            markup.add(InlineKeyboardButton("حذف اذان المغرب",callback_data=f"del_Maghrib_{data[2]}_{data[3]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان المغرب",callback_data=f"time_Maghrib_{data[2]}_{data[3]}_{data[-1]}"))
            maghrib="❌"
        if i["asr"] == dict_time["Asr"]:
            asr="✅"
            markup.add(InlineKeyboardButton("حذف اذان العصر",callback_data=f"del_Asr_{data[2]}_{data[3]}_{data[-1]}"))
        else:
            markup.add(InlineKeyboardButton("اذان العصر",callback_data=f"time_Asr_{data[2]}_{data[3]}_{data[-1]}"))
            asr="❌"
        if i["isha"] == dict_time["Isha"]:
            isha="✅"
            markup.add(InlineKeyboardButton("حذف اذان العشاء",callback_data=f"del_Isha_{data[2]}_{data[3]}_{data[-1]}"))
        else:
            isha="❌"
            markup.add(InlineKeyboardButton("اذان العشاء",callback_data=f"time_Isha_{data[2]}_{data[3]}_{data[-1]}"))
        markup.add(InlineKeyboardButton("حفظ التغيرات",callback_data=f"cooonfirm_{data[-1]}"))
    bot.edit_message_text(f"""
⌁ : يرجى اختيار الوقت الذي سيتم فيه نشر الاذكار والاذان في الدردشة

🕋مواقيت الصلاه🕋
اذان الفجر: {dict_time["Fajr"]}   {fajr}

اذان الظهر: {dict_time["Dhuhr"]}   {dhuhr}

اذان المغرب: {dict_time["Maghrib"]}   {maghrib}

اذان العصر: {dict_time["Asr"]}       {asr}

اذان العشاء: {dict_time["Isha"]}       {isha}

الشروق: {dict_time["Sunrise"]}

""",cid,mid,reply_markup=markup)




def check_and_notify_thread():
    while True:
        # print("ok")
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
        current_utc_time = datetime.now(pytz.utc)
        tehran_timezone = pytz.timezone('Asia/Tehran')
        current_time = current_utc_time.astimezone(tehran_timezone).strftime("%H:%M")
        # current_time =datetime.now().strftime("%H:%M")
        for row in rows:          
            for i in ["Fajr","Dhuhr","Maghrib","Asr","Isha"]:
                if row[i] != "None":
                    if current_time == row[i]:
                        try:
                            bot.copy_message(row["chat_id"],chanal_base,dict_code_message[i],reply_markup=setting_markup())
                        except:
                            pass
                            # print("left")
        threading.Event().wait(55)


check_thread = threading.Thread(target=check_and_notify_thread)
check_thread.start()


bot.infinity_polling()



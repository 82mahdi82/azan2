import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import threading
import databases
import datetime
import pytz

admins=0
TOKEN ='6317356905:AAGQ2p8Lo0Kc4mkChTmE7ZbI2p1bzw9cIO8'

chanal_target={}
userStep={}
dict_user_budget={}#cid:5
block_list=[]
user_id_payment=0

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

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        userStep[uid] = 0
        return 0

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)

def is_user_member(user_id, channel_id):
    try:
        chat_member = bot.get_chat_member(channel_id, user_id)
        return chat_member.status == "member" or chat_member.status == "administrator" or chat_member.status == "creator"
    except Exception as e:
        #print(f"Error checking membership: {e}")
        return False


@bot.callback_query_handler(func=lambda call: call.data.startswith("delete"))
def delete_chanel(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    chanelid=int(call.data.split("_")[-1])
    chanal_target.pop(chanelid)
    bot.delete_message(cid,mid)
    bot.answer_callback_query(call.id,"کانال حذف شد")

@bot.callback_query_handler(func=lambda call: call.data.startswith("show"))
def show_money(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("بازگشت به منو",callback_data="menu"))
    bot.send_message(cid,f"موجودی شما : {dict_user_budget[cid]} تومان است",reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data.startswith("payment"))
def payment_admin(call):
    global user_id_payment
    cid = call.message.chat.id
    user_id=int(call.message.text.split("\n")[0])
    user_id_payment=user_id
    mid = call.message.message_id
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
    bot.send_message(cid,"ادمین گرامی لطفا پس از کارت به کارت عکس رسید را ارسال کنید",reply_markup=markup)
    userStep[cid]=200

@bot.callback_query_handler(func=lambda call: call.data.startswith("senumcart"))
def call_callback_panel_senumcart(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    if dict_user_budget[cid]>=100:
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به منو",callback_data="menu"))
        bot.send_message(int(cid),"لطفا شماره کارت خود را ارسال کنید:",reply_markup=markup)
        userStep[cid]=100
    else:
        bot.answer_callback_query(call.id,"برای دریافت پول باید حداقل موجودی شما 100 تومن باشد")

@bot.callback_query_handler(func=lambda call: call.data.startswith("menu"))
def menu(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    userStep[cid]=0
    markup=InlineKeyboardMarkup()
    num=1
    for i in chanal_target:
        markup.add(InlineKeyboardButton(f"کانال {num}",url=f"{chanal_target[i][1]}"))
        num+=1
    markup.add(InlineKeyboardButton("نمایش موجودی",callback_data="show"))
    markup.add(InlineKeyboardButton("ارسال شماره کارت برای ادمین",callback_data="senumcart"))
    bot.send_message(cid,"منو",reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data.startswith("back"))
def call_callback_panel_amar(call):
    global user_id_payment
    cid = call.message.chat.id
    mid = call.message.message_id
    user_id_payment=0
    userStep[cid]=0
    keypanel = InlineKeyboardMarkup()
    keypanel.add(InlineKeyboardButton('آمار کلی',callback_data='panel_amar'),InlineKeyboardButton("آمار جزئی",callback_data='panel_info'))
    keypanel.add(InlineKeyboardButton('ارسال همگانی',callback_data='panel_brodcast'),InlineKeyboardButton('فوروارد همگانی',callback_data='panel_forall'))
    keypanel.add(InlineKeyboardButton("مدیریت کانال ها",callback_data="panel_manage"))
    keypanel.add(InlineKeyboardButton("افزودن کانال",callback_data="panel_add"))
    bot.edit_message_text(' لطفا انتخاب کنید',cid,mid,reply_markup=keypanel)

@bot.callback_query_handler(func=lambda call: call.data.startswith("sends"))
def call_callback_panel_sends(call):
    global userStep
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")  
    count=0  
    count_black=0
    if data[1] =="brodcast":
        list_user=databases.use_users()
        for i in list_user:
            try:
                bot.copy_message(i[0],cid,int(data[-1]))
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
                bot.forward_message(i[0],cid,int(data[-1]))
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
@bot.callback_query_handler(func=lambda call: call.data.startswith("panel"))
def call_callback_panel_amar(call):
    global userStep
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data.split("_")[-1]
    if data=="amar":
        countOfUsers=len(databases.use_users())
        txt = f'آمار کاربران: {countOfUsers}'
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text(txt,cid,mid,reply_markup=markup)
    elif data=="info":
        list_users=databases.use_users()
        if len(list_users)>0:
            text=""
            number=1
            for i in list_users:
                text+=f"{number}.{i[1]} | موجودی:{dict_user_budget[i[0]]}"
                number+=1
        else:
            text="کاربری وجود ندارد"
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.send_message(cid,text,reply_markup=markup)
    elif data=="brodcast":
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text("برای ارسال همگانی پیام لطفا پیام خود را ارسال کنید و در غیر این صورت برای بازگشت به پنل از دکمه زیر استفاده کنید",cid,mid,reply_markup=markup)
        userStep[cid]=1
    elif data=="forall":
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.edit_message_text("برای فوروارد همگانی پیام لطفا پیام خود را ارسال کنید و در غیر این صورت برای بازگشت به پنل از دکمه زیر استفاده کنید",cid,mid,reply_markup=markup)
        userStep[cid]=2
    elif data=="manage":
        if len(chanal_target)==0:
            bot.answer_callback_query(call.id,"هنوز کانالی انتخاب نشده است")
        else:
            for i in chanal_target:
                markup=InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton("حذف کانال",callback_data=f"delete_{i}"))
                bot.send_message(cid,f"اسم کانال: {chanal_target[i][0]}",reply_markup=markup)
                
    elif data=="add":
        markup=InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
        bot.send_message(cid,f"""
برای افزودن کانال به ربات مراحل زیر را به ترتیب انجام دهید:
1.ربات را در مانال مورد نظر اد کنید
2.ربات را در کانال ادمین کنید
3.یک پیام از کانال را برای ربات فوروارد کنید
""",reply_markup=markup)
        userStep[cid]=10


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if admins==0:
        admins=cid
    if cid!=admins:
        databases.insert_users(cid,m.chat.first_name)
    dict_user_budget.setdefault(cid,0)
    if cid == admins:
        keypanel = InlineKeyboardMarkup()
        keypanel.add(InlineKeyboardButton('آمار کلی',callback_data='panel_amar'),InlineKeyboardButton("آمار جزئی",callback_data='panel_info'))
        keypanel.add(InlineKeyboardButton('ارسال همگانی',callback_data='panel_brodcast'),InlineKeyboardButton('فوروارد همگانی',callback_data='panel_forall'))
        keypanel.add(InlineKeyboardButton("مدیریت کانال ها",callback_data="panel_manage"))
        keypanel.add(InlineKeyboardButton("افزودن کانال",callback_data="panel_add"))
        bot.send_message(cid,'سلام ادمین گرامی خوش امدید لطفا انتخاب کنید',reply_markup=keypanel)
    else:
        markup=InlineKeyboardMarkup()
        num=1
        for i in chanal_target:
            markup.add(InlineKeyboardButton(f"کانال {num}",url=f"{chanal_target[i][1]}"))
            num+=1
        markup.add(InlineKeyboardButton("نمایش موجودی",callback_data="show"))
        markup.add(InlineKeyboardButton("ارسال شماره کارت برای ادمین",callback_data="senumcart"))
        bot.send_message(cid,f"""
سلام {m.chat.first_name} خوش آمدی 
برای استفاده از ربات و کسب درآمد فقط کافیه داخل کانال های زیر عضو بشی و به ازای هر روز عضویت در کانال ها 5 هزار تومن پول دریافت کنی
""",reply_markup=markup)



@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==10)
def add_new_chanel(m):
    cid = m.chat.id
    print(m)
    if m.forward_from_chat.id not in chanal_target:
        # bot.send_message(int(m.forward_from_chat.id), 'hi')
        link=bot.export_chat_invite_link(chat_id=int(m.forward_from_chat.id))
        chanal_target.setdefault(int(m.forward_from_chat.id),[m.forward_from_chat.title,link])
        print("link",link)
        bot.send_message(cid,"کانال اضافه شد")
    else:
        bot.send_message(cid,"این کانال قبلا اضافه شده است")

@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==100)
def get_mony(m):
    cid = m.chat.id
    text=m.text
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("پرداخت و ارسال رسید",callback_data="payment"))
    markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
    bot.send_message(admins,f"""
{cid}
نام کاربر:{m.chat.first_name}
موجودی : {dict_user_budget[cid]} تومن
شماره کارت : {text}
""",reply_markup=markup)
    bot.send_message(cid,"شماره کارت شما برای ادمین ارسال شد")


@bot.message_handler(content_types=['photo','video',"video_note","audio","voice","document","sticker","location","contact","text"])
def panel_set_photo(m):
    global userStep
    cid = m.chat.id
    mid = m.message_id
    if m.chat.type=="private":
        text=m.text
        if userStep[cid]==1:
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("تایید",callback_data=f"sends_brodcast_{mid}"))
            markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
            bot.send_message(cid,"پیام شما دریافت شد برای ارسال همگانی تایید را بزنید",reply_markup=markup)
            userStep[cid]=0
        elif userStep[cid]==2:
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("تایید",callback_data=f"sends_forall_{mid}"))
            markup.add(InlineKeyboardButton("بازگشت به پنل",callback_data="back_panel"))
            bot.send_message(cid,"پیام شما دریافت شد برای فوروارد همگانی تایید را بزنید",reply_markup=markup)
            userStep[cid]=0
        elif userStep[cid]==200:
            bot.copy_message(user_id_payment,cid,mid)
            dict_user_budget[user_id_payment]=0
            bot.send_message(cid,"پرداخت انجام شد و رسید برای کاربر ارسال شد")
            userStep[cid]=0
        else:
            bot.send_message(cid,"مقدار وارد شده نامعتبر است لطفا طبق دستور /start مجددا امتحان کنید")   
            userStep[cid]=0
def check_and_notify_thread():
    global block_list
    while True:
        current_utc_time = datetime.datetime.now(pytz.utc)
        tehran_timezone = pytz.timezone('Asia/Tehran')
        current_time = current_utc_time.astimezone(tehran_timezone).strftime("%H:%M")
        if current_time=="00:01":
            list_user=databases.use_users()
            for user in list_user:
                if user[0] not in block_list:
                    for chanel in chanal_target:
                        if is_user_member(user[0],chanel):
                            dict_user_budget[int(user[0])]+=5
                    bot.send_message(int(user[0]),f"موجودی شما : {dict_user_budget[int(user[0])]} تومان")
                    block_list.append(user)
                    if dict_user_budget[int(user[0])]==100:
                        markup=InlineKeyboardMarkup()
                        markup.add(InlineKeyboardButton("بازگشت به منو",callback_data="menu"))
                        bot.send_message(int(user[0]),"لطفا شماره کارت خود را برای دریافت پول ارسال کنید:",reply_markup=markup)
                        userStep[int(user)]=100

        if current_time=="00:05":
            block_list=[]
        threading.Event().wait(56)


check_thread = threading.Thread(target=check_and_notify_thread)
check_thread.start()
bot.infinity_polling()


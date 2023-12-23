import sqlite3
def creat_database_tables():
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS admin_group(cid int(25),chat_id int(25),title  VARCHAR(250) ,country VARCHAR(250) DEFAULT 'None',city VARCHAR(250) DEFAULT 'None',Fajr VARCHAR(25) DEFAULT 'None',Dhuhr VARCHAR(25) DEFAULT 'None',Maghrib VARCHAR(25) DEFAULT 'None',Asr VARCHAR(25) DEFAULT 'None',Isha VARCHAR(25) DEFAULT 'None')")
    cur.execute("CREATE TABLE IF NOT EXISTS users(cid int(25))")
    connect.commit()
    connect.close()

def use_table_admin_group(cid):
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute(f"select * from admin_group where cid={cid}")
    dict_info=cur.fetchall()
    connect.commit()
    connect.close()
    return dict_info
def insert_table_admin_group(cid,chat_id,title):
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute(f"""insert into admin_group (cid,chat_id,title) values ({cid},{chat_id},"{title}")""")
    connect.commit()
    connect.close()

def insert_users(cid):
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute(f"select * from users where cid={cid}")  
    f = cur.fetchall()
    if len(f)==0:
        cur.execute(f"insert into users (cid) values ({cid})")
    connect.commit()
    connect.close()

def delete_users(cid):
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute(f"delete from users where cid={cid}")
    connect.commit()
    connect.close()

def use_users():
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute(f"select * from users")   
    f = cur.fetchall()
    connect.commit()
    connect.close()
    return f


def update_table_admin_group(cid,chat_id,what,amount):
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute(f"""update admin_group set "{what}"="{amount}" where cid={cid} and chat_id={chat_id}""")
    connect.commit()
    connect.close()

def check_cid(cid):
    connect = sqlite3.connect("data.db")
    connect.row_factory = sqlite3.Row
    cur = connect.cursor()
    cur.execute(f"select * from admin_group where cid={cid}")   
    f = cur.fetchall()
    connect.commit()
    connect.close()
    return f

def check_cid_chat_id(cid,chat_id):
    connect = sqlite3.connect("data.db")
    connect.row_factory = sqlite3.Row
    cur = connect.cursor()
    cur.execute(f"select * from admin_group where cid={cid} and chat_id={chat_id}")   
    f = cur.fetchall()
    connect.commit()
    connect.close()
    return f



def select_all_info():
    connect = sqlite3.connect("data.db")
    connect.row_factory = sqlite3.Row
    cur = connect.cursor()
    cur.execute(f"select * from admin_group")   
    f = cur.fetchall()
    connect.commit()
    connect.close()
    return f

def delete_row(chat_id):
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute(f"delete from admin_group where chat_id={chat_id}")
    connect.commit()
    connect.close()

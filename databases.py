import sqlite3
def creat_database_tables():
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(cid int(25))")
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


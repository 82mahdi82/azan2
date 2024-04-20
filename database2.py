import mysql.connector
import time
def create_database():
    cnx = mysql.connector.connect(user='root', password='mDAg9x6Ictcx5MVLnuMf',host='myenux_db')
    cursor = cnx.cursor()
    cursor.execute("DROP database IF EXISTS data")
    cursor.execute("create database if not exists data")
    cursor.execute("use data")
    cursor.execute("CREATE TABLE IF NOT EXISTS users(cid VARCHAR(100))")
    cursor.execute("""CREATE TABLE IF NOT EXISTS translations(text TEXT, 
                   language VARCHAR(50), 
                   language_target VARCHAR(50), 
                   mid int(100));""")
    print("created")
    cursor.close()
    cnx.commit()

def insert_users(cid):
    cnx = mysql.connector.connect(user='root', password='mDAg9x6Ictcx5MVLnuMf',host='myenux_db',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from users where cid={cid}")  
    f = cursor.fetchall()
    if len(f)==0:
        cursor.execute(f"insert into users (cid) values ({cid});")
    cursor.close()
    cnx.commit()

def delete_users(cid):
    cnx = mysql.connector.connect(user='root', password='mDAg9x6Ictcx5MVLnuMf',host='myenux_db',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"delete from users where cid={cid}") 
    cursor.close()
    cnx.commit()

def use_users():
    cnx = mysql.connector.connect(user='root', password='mDAg9x6Ictcx5MVLnuMf',host='myenux_db',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from users") 
    dict_product=cursor.fetchall()
    cursor.close()
    cnx.commit()
    return dict_product

def insert_translations(text,language,language_target,mid):
    cnx = mysql.connector.connect(user='root', password='mDAg9x6Ictcx5MVLnuMf',host='myenux_db',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"insert into translations (text,language,language_target,mid) values ('{text}','{language}','{language_target}',{mid})")
    cursor.close()
    cnx.commit()

def use_translations(text,language,language_target):
    cnx = mysql.connector.connect(user='root', password='mDAg9x6Ictcx5MVLnuMf',host='myenux_db',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from translations where text='{text}' AND language='{language}' AND language_target='{language_target}'")   
    dict_product=cursor.fetchall()
    cursor.close()
    cnx.commit()
    return dict_product



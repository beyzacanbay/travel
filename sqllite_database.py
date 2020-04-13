import pprint
import sqlite3
import request
import json

conn=sqlite3.connect('database.db')

cursor=conn.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS places(id INT,city_name TEXT,region TEXT,description TEXT, lat REAL, lon REAL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS regions(Id INT,region TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS region(Id INT,region TEXT, photo TEXT)")

createTable()

def add_value():
    #cursor.execute("INSERT INTO places VALUES(25,'Van','Eastern Anatolia','desc', 38.503490, 43.396450)")
    #cursor.execute("INSERT INTO places VALUES(26,'Malatya','Eastern Anatolia','desc', 38.345750, 38.289710)")
    #cursor.execute("INSERT INTO places VALUES(27,'Bitlis','Eastern Anatolia','desc', 38.406070, 42.106160)")
    #cursor.execute("INSERT INTO places VALUES(28,'Ağrı','Eastern Anatolia','desc', 39.718490, 43.050870)")
    cursor.execute("INSERT INTO region VALUES(1,'Marmara','https://www.dunyaatlasi.com/wp-content/uploads/2018/07/marmara-bolgesinin-turistik-yerleri-nerelerdir.jpg')")
    cursor.execute("INSERT INTO region VALUES(2,'Aegean','https://www.makaleler.com/fotomakaleler/ege-bolgesindeki-korfezler-2087.jpg')")
    cursor.execute("INSERT INTO region VALUES(3,'Central Anatolia','https://www.camhotel.com.tr/uploads/gezilecek-yerleri-yemekleri-iklimi-ve-cok-daha-fazlasi-ile-ic-anadolu-bolgesi_1.jpg')")
    cursor.execute("INSERT INTO region VALUES(4,'Mediterranean','https://www.derszamani.net/wp-content/uploads/2017/03/s5-1.jpg')")
    cursor.execute("INSERT INTO region VALUES(5,'Black Sea','https://www.derszamani.net/wp-content/uploads/2017/03/c17-17.jpg')")
    cursor.execute("INSERT INTO region VALUES(6,'Southeastern Anatolia','https://www.msxlabs.org/forum/attachments/58287d1479556469-guneydogu-anadolu-bolgesi-genel-bilgi-gap-gezisi.jpg')")
    cursor.execute("INSERT INTO region VALUES(7,'Eastern Anatolia','https://img-s1.onedio.com/id-54da5068d44ba9af53901abc/rev-0/w-635/listing/f-jpg-webp/s-1ce7449d543f708b6cd5e2376da08da0e3517e75.jpg')")
    conn.commit()
    conn.close()



createTable()
add_value()
import pprint
import sqlite3
import request
import json

conn=sqlite3.connect('database.db')

cursor=conn.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS places(Id INT,city_name TEXT,region TEXT,description TEXT, lat REAL, lon REAL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS regions(Id INT,region TEXT)")

createTable()

def add_value():
    #cursor.execute("INSERT INTO places VALUES(25,'Van','Eastern Anatolia','desc', 38.503490, 43.396450)")
    #cursor.execute("INSERT INTO places VALUES(26,'Malatya','Eastern Anatolia','desc', 38.345750, 38.289710)")
    #cursor.execute("INSERT INTO places VALUES(27,'Bitlis','Eastern Anatolia','desc', 38.406070, 42.106160)")
    #cursor.execute("INSERT INTO places VALUES(28,'Ağrı','Eastern Anatolia','desc', 39.718490, 43.050870)")
    cursor.execute("INSERT INTO regions VALUES(1,'Marmara')")
    cursor.execute("INSERT INTO regions VALUES(2,'Aegean')")
    cursor.execute("INSERT INTO regions VALUES(3,'Central Anatolia')")
    cursor.execute("INSERT INTO regions VALUES(4,'Mediterranean')")
    cursor.execute("INSERT INTO regions VALUES(5,'Black Sea')")
    cursor.execute("INSERT INTO regions VALUES(6,'Southeastern Anatolia')")
    cursor.execute("INSERT INTO regions VALUES(7,'Eastern Anatolia')")
    conn.commit()
    conn.close()



conn.close()